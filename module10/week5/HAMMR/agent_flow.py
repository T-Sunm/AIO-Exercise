from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import Swarm
from autogen_core.models import ChatCompletionClient
from agents.EncyclopedicAgent import singlehop_encyclopedic
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.messages import MultiModalMessage
from autogen_core import CancellationToken, Image
from pathlib import Path
import asyncio
from autogen_agentchat.ui import Console
from autogen_agentchat.conditions import MaxMessageTermination
config = {
    "provider": "OpenAIChatCompletionClient",
    "config": {
        "model": "llama-3.2-3b-instruct",
        "base_url": "http://127.0.0.1:1234/v1",
        "api_key": "lm-studio",
        "model_info": {
            "name": "llama-3.2-3b-instruct",
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

client = ChatCompletionClient.load_component(config)

dispatcher = AssistantAgent(
    name="Dispatcher",
    system_message=("""
        You are a VQA question dispatcher agent in a hierarchical multi-agent system.

        Your task is to:
        1. Analyze the user question and determine the type of VQA task (e.g., encyclopedic, OCR, counting, etc.)
        2. Based on your analysis, hand off the question to the appropriate specialist agent.

        You may only hand off to one of the following agents:
        - SingleHopEncyclopedicAgent

        Never invent tool names. Never attempt to call tools directly.

        Always:
        - Describe your plan first
        - Use a handoff to one of the listed agents (not a tool)
        - Use TERMINATE when research is complete.
        """),

    model_client=client,
    handoffs=["SingleHopEncyclopedicAgent"]
)

text_termination = TextMentionTermination("TERMINATE")
termination = text_termination
vqa_team = Swarm(
    participants=[dispatcher,
                  singlehop_encyclopedic], termination_condition=termination
)

# Đọc ảnh từ file
image_path = Path("cat.jpg")  # Đổi đường dẫn tới ảnh phù hợp
image = Image.from_file(image_path)

# Tạo message đầu vào dạng multimodal
# message = MultiModalMessage(
#     content=[
#         "Question: What breed is this cat?, Image_url: https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
#     ],
#     source="user"
# )
message = "Question: What breed is this cat?, Image_url: https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
async def main():
  # Bind the console to the async-stream
  await Console(vqa_team.run_stream(task=message))

  # Close the client when done
  await client.close()

if __name__ == "__main__":
  asyncio.run(main())
