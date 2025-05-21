from autogen_core import Image, CancellationToken
from autogen_agentchat.messages import MultiModalMessage
import asyncio
from autogen_agentchat.agents import AssistantAgent
from tools.google_lens import google_lens_tool
from tools.wikipedia_article import wikipedia_article_tool
from tools.answer_with_context import answer_with_context_tool
from autogen_core.models import ChatCompletionClient
from autogen_agentchat.ui import Console
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

# 3. SingleHopEncyclopedicAgent
singlehop_encyclopedic = AssistantAgent(
    name="SingleHopEncyclopedicAgent",
    system_message=(
        "You are responsible for answering factual questions about an object in the image. "
        "Use GoogleLens to identify the object, retrieve its Wikipedia page, and use that context to answer. "
        "Tools: GoogleLens, WikipediaArticle, AnswerWithContext."
        "Always handoff back to Dispatcher when analysis is complete."
    ),
    tools=[google_lens_tool, wikipedia_article_tool, answer_with_context_tool],
    model_client=client,
    handoffs=["Dispatcher"],
)

# 4. TwoHopEncyclopedicAgent
twohop_encyclopedic = AssistantAgent(
    name="TwoHopEncyclopedicAgent",
    system_message=(
        "You solve complex encyclopedic questions that require two steps of reasoning. "
        "First decompose the question, then answer each part using relevant tools or other agents like SingleHopEncyclopedicAgent. "
        "Tools: DecomposeQuestion, GoogleLens, WikipediaArticle."
    ),
    model_client=client
)


# message = MultiModalMessage(
#     content=[
#         "Question: What breed is this cat?, Image_url: https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500",
#     ],
#     source="user"
# )
# async def main():
#   # (Tạo message như trên)
#   await Console(singlehop_encyclopedic.run_stream(task=message))

# if __name__ == "__main__":
#   asyncio.run(main())
