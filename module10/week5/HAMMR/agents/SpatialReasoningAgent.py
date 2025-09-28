from autogen_agentchat.agents import AssistantAgent

spatial_reasoning = AssistantAgent(
    name="SpatialReasoningAgent",
    system_message=(
        "You handle visual questions involving spatial reasoning between objects in the image. "
        "Use object detection, spatial relationship analysis, and reasoning tools to determine relations like 'left of', 'above', or overlapping. "
        "Tools: DetectObject, CropImage, ObjectInImage, BoundingBoxOverlap, SpatialSelection, OCR."
    )
)
