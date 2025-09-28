from autogen_agentchat.agents import AssistantAgent

# 1. PointQALocalAgent
pointqa_local = AssistantAgent(
    name="PointQALocalAgent",
    system_message=(
        "You are a specialist agent for local pointing questions. "
        "Your task is to process questions about a specific location in the image, "
        "using tools such as CropImage, VQA, and DetectObject to reason about the cropped region."
    )
)

# 2. PointQALookTwiceAgent
pointqa_looktwice = AssistantAgent(
    name="PointQALookTwiceAgent",
    system_message=(
        "You handle questions that require both inspecting a local point in the image and reasoning about the entire image. "
        "First identify the object at the specified point, then determine a global property based on that. "
        "Tools used: CropImage, VQA, ObjectInImage."
    )
)
