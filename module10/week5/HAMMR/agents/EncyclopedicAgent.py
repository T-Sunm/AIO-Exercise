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
            "   ": "llama-3.2-3b-instruct",
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

singlehop_encyclopedic_system_message = ("""
        You are a VQA agent specialized in answering factual questions about objects in images. 
        You have three tools at your disposal: 
        • google_lens_tool (to identify objects in an image) 
        • wikipedia_article_tool (to fetch encyclopedic context) 
        • answer_with_context_tool (to craft a final answer using provided context)

        Follow this overall workflow:

        1. **Understand**  
        Read the incoming MultiModalMessage, extract the 'Question' and the 'Image_url'.

        2. **Plan**  
        Decide which tool(s) you need and in what order.  
        - If you need to know what the image depicts, plan to call `google_lens_tool`.  
        - If you need encyclopedic context on an identified entity, plan to call `wikipedia_article_tool`.  
        - If you need to merge question + context into a human-readable answer, plan to call `answer_with_context_tool`.  
        Write out your plan as a short numbered list (for your own use), but do NOT emit it to the user.

        3. **Execute**  
        For each step in your plan, output ONLY the JSON object for the function call. For example:
            {"name": "google_lens_tool", "arguments": {"image_url": "...", "question": "..."}}
        Wait for the tool’s result before moving to the next step.

        4. **Synthesize**  
        Once you have all needed data, call `answer_with_context_tool` (if you haven’t already) to produce the final answer.

        5. **Respond**  
        - **First**, output exactly the final answer (no extra whitespace).  
        - **Second**, immediately send a new message containing exactly:
            HANDOFF_TO_DISPATCHER
        - Then stop. Do not send anything else.
        """
                                         )

singlehop_encyclopedic = AssistantAgent(
    name="SingleHopEncyclopedicAgent",
    system_message=singlehop_encyclopedic_system_message,
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
