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

dispatcher_system_message = """
    You are the top‐level VQA dispatcher.  
    1. Always hand off the user's raw question to SingleHopEncyclopedicAgent by replying:
    Handing off to SingleHopEncyclopedicAgent. Original request: [the user’s exact message]
    2. When you later receive a message whose content is exactly 'HANDOFF_TO_DISPATCHER',
    that means SingleHop has already sent the answer just before it.  
    Your task now is to:
        a) Take the immediately preceding message (the answer) and deliver it back to the user.
        b) Then output the word TERMINATE (by itself) and stop.
    3. Do not call any tools yourself.  
"""

dispatcher = AssistantAgent(
    name="Dispatcher",
    system_message=dispatcher_system_message,
    model_client=client,
    handoffs=["SingleHopEncyclopedicAgent"],
    tools=[],
)

text_termination = TextMentionTermination("TERMINATE")
max_messages_limit = 10
termination_conditions = text_termination | MaxMessageTermination(
    max_messages=max_messages_limit)
vqa_team = Swarm(
    participants=[dispatcher,
                  singlehop_encyclopedic], termination_condition=termination_conditions
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
message = "What is the capital of France?"
async def main():
  await Console(vqa_team.run_stream(task=message))
  await client.close()

if __name__ == "__main__":
  asyncio.run(main())
