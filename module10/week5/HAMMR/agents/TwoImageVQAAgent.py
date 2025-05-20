from autogen_agentchat.agents import AssistantAgent

twoimage_vqa = AssistantAgent(
    name="TwoImageVQAAgent",
    system_message=(
        "You are responsible for answering questions that require comparing two images. "
        "Query each image individually, then combine the information to answer. "
        "Tools: VQA, Caption, DetectObject."
    )
)
