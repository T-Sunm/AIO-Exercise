from autogen_core.models import ChatCompletionClient
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import Swarm
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
import asyncio

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

# Cấu hình cho mô hình "llama-3.2-3b-instruct"
config = {
    "provider": "OpenAIChatCompletionClient",
    "config": {
        "model": "llama-3.2-3b-instruct",
        "base_url": "http://127.0.0.1:1234/v1",
        "api_key": "lm-studio",
        "model_info": {
            "name": "llama-3.2-3b-instruct",  # Đã sửa từ "   " thành "name"
            "family": "openai",
            "supports_tool_calling": False,
            "supports_json_mode": False,
            "structured_output": True,
            "json_output": True,
            "function_calling": True,
            "vision": True,
        }
    }
}

# Khởi tạo model_client với cấu hình mới
model_client = ChatCompletionClient.load_component(config)

# Định nghĩa các agent
planner = AssistantAgent(
    "planner",
    model_client=model_client,
    handoffs=["financial_analyst", "news_analyst", "writer"],
    system_message="""You are a research planning coordinator.
    Coordinate market research by delegating to specialized agents:
    - Financial Analyst: For stock data analysis
    - News Analyst: For news gathering and analysis
    - Writer: For compiling final report
    Always send your plan first, then handoff to appropriate agent.
    Always handoff to a single agent at a time.
    Use TERMINATE when research is complete.""",
)

financial_analyst = AssistantAgent(
    "financial_analyst",
    model_client=model_client,
    handoffs=["planner"],
    tools=[get_stock_data],
    system_message="""You are a financial analyst.
    Analyze stock market data using the get_stock_data tool.
    Provide insights on financial metrics.
    Always handoff back to planner when analysis is complete.""",
)

news_analyst = AssistantAgent(
    "news_analyst",
    model_client=model_client,
    handoffs=["planner"],
    tools=[get_news],
    system_message="""You are a news analyst.
    Gather and analyze relevant news using the get_news tool.
    Summarize key market insights from news.
    Always handoff back to planner when analysis is complete.""",
)

writer = AssistantAgent(
    "writer",
    model_client=model_client,
    handoffs=["planner"],
    system_message="""You are a financial report writer.
    Compile research findings into clear, concise reports.
    Always handoff back to planner when writing is complete.""",
)

# Định nghĩa điều kiện dừng
text_termination = TextMentionTermination("TERMINATE")
termination = text_termination

# Khởi tạo Swarm
research_team = Swarm(
    participants=[planner, financial_analyst, news_analyst, writer],
    termination_condition=termination
)

# Nhiệm vụ
task = "Conduct market research for TSLA stock"

# Chạy Swarm
async def main():
  await Console(research_team.run_stream(task=task))
  await model_client.close()

if __name__ == "__main__":
  asyncio.run(main())
