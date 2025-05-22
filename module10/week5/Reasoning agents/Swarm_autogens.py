from autogen_core.models import ChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import TextMentionTermination, MaxMessageTermination
from autogen_agentchat.ui import Console
import asyncio
import json
import re
# Định nghĩa các công cụ
async def get_stock_data(symbol: str) -> dict:
  """Get stock market data for a given symbol"""
  return {"price": 180.25, "volume": 1000000, "pe_ratio": 65.4, "market_cap": "700B"}

async def get_news(query: str) -> list:
  """Get recent news articles about a company"""
  return [
      {
          "title": "Tesla Expands Cybertruck Production",
          "date": "2024-03-20",
          "summary": "Tesla ramps up Cybertruck manufacturing capacity at Gigafactory Texas, aiming to meet strong demand.",
      },
      {
          "title": "Tesla FSD Beta Shows Promise",
          "date": "2024-03-19",
          "summary": "Latest Full Self-Driving beta demonstrates significant improvements in urban navigation and safety features.",
      },
      {
          "title": "Model Y Dominates Global EV Sales",
          "date": "2024-03-18",
          "summary": "Tesla's Model Y becomes best-selling electric vehicle worldwide, capturing significant market share.",
      },
  ]

config = {
    "provider": "OpenAIChatCompletionClient",
    "config": {
        "model": "qwen3-4b",
        "base_url": "http://127.0.0.1:1234/v1",
        "api_key": "lm-studio",
        "model_info": {
            "name": "qwen3-4b",
            "family": "openai",
            "supports_tool_calling": False,
            "supports_json_mode": True,
            "structured_output": True,
            "json_output": True,
            "function_calling": True,
            "vision": False,
            "parallel_tool_calls": False
        }
    }
}

# Khởi tạo model_client với cấu hình mới
model_client = ChatCompletionClient.load_component(config)

planner = AssistantAgent(
    "planner",
    model_client=model_client,
    handoffs=["financial_analyst", "news_analyst", "writer"],
    system_message="""You are a research planner working with:
        - Financial Analyst (stock metrics)
        - News Analyst (news insights)
        - Writer (compile final report)

        Your task has two phases:
        1. Send a short plan, then handoff to ONE agent at a time.
        2. After the Writer finishes the report:
        - Extract the report content from the writer's message.
        - Output a JSON in this exact format:
            {
            "final_output_marker": "FINAL_REPORT_FROM_PLANNER",
            "title": "Market Research Report: TSLA",
            "report_content": "[Writer's report here]"
            }
        - **Immediately after this JSON, on a separate line, you MUST output:** `TERMINATE`
        - Do NOT skip or forget to include the word TERMINATE. If you miss it, the task will not end.
        """
)


financial_analyst = AssistantAgent(
    "financial_analyst",
    model_client=model_client,
    handoffs=["planner"],
    tools=[get_stock_data],
    system_message="""You are a financial analyst.
        1. Use get_stock_data to get current metrics for TSLA.
        2. Summarize the key values: price, volume, PE ratio, market cap.
        3. After you send your summary, you MUST call the tool: transfer_to_planner().""",
)

news_analyst = AssistantAgent(
    "news_analyst",
    model_client=model_client,
    handoffs=["planner"],
    tools=[get_news],
    system_message="""You are a news analyst.
    1. Use get_news tool to find recent news about TSLA.
    2. Summarize the impact of these articles on the company.
    3. After you send your summary, you MUST call the tool: transfer_to_planner().""",
)

writer = AssistantAgent(
    "writer",
    model_client=model_client,
    handoffs=["planner"],
    system_message="""You are a financial report writer.
        1. Use earlier messages (financial data + news) to write a short, clear, professional market research report (max ~350 words).
        2. The report must be in plain text with no formatting or markdown.
        3. Immediately after sending the report, you MUST call the tool: transfer_to_planner().
        """,
)

# Định nghĩa điều kiện dừng
text_termination = TextMentionTermination("TERMINATE")
max_messages_termination = MaxMessageTermination(max_messages=25)
termination = text_termination | max_messages_termination

research_team = Swarm(
    participants=[planner, financial_analyst, news_analyst, writer],
    termination_condition=termination
)

# Nhiệm vụ
task = "Conduct market research for TSLA stock"

async def main():
  result = await research_team.run(task=task)
  last_msg = result.messages[-1]
  raw = last_msg.content

  print(">>> RAW CONTENT OF LAST MSG:\n", raw, "\n<<< END RAW >>>\n")
  # Tìm chỉ số bắt đầu của JSON và kết thúc của JSON trong toàn bộ 'raw'
  start = raw.find("{")
  # rfind để tìm dấu } cuối cùng, phòng trường hợp có } trong string của JSON
  end = raw.rfind("}")

  if start == -1 or end == -1 or end <= start:
    print(
        "Không tìm thấy cặp dấu ngoặc JSON hợp lệ trong message")
    return

  json_str = raw[start: end + 1]
  report = json.loads(json_str)

  print("=== Market Research Report: TSLA ===")
  print("Tiêu đề   :", report.get("title"))
  print("Nội dung  :\n", report.get("report_content"))

  await model_client.close()

if __name__ == "__main__":
  asyncio.run(main())
