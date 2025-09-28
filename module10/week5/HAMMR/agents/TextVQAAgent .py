from autogen_agentchat.agents import AssistantAgent

textvqa = AssistantAgent(
    name="TextVQAAgent",
    system_message=(
        "You answer questions that require reading and interpreting text embedded in the image. "
        "Your job is to detect and OCR text regions and then reason over the extracted content. "
        "Tools: DetectObject, CropImage, OCR."
    )
)
