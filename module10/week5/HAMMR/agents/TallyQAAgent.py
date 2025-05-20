from autogen_agentchat.agents import AssistantAgent

tallyqa = AssistantAgent(
    name="TallyQAAgent",
    system_message=(
        "You handle questions that involve complex counting of specific objects in the image. "
        "Use object detection and reasoning to determine how many relevant items are present. "
        "Tools: DetectObject, CropImage, ObjectInImage."
    )
)
