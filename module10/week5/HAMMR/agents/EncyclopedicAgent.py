from autogen_agentchat.agents import AssistantAgent

# 3. SingleHopEncyclopedicAgent
singlehop_encyclopedic = AssistantAgent(
    name="SingleHopEncyclopedicAgent",
    system_message=(
        "You are responsible for answering factual questions about an object in the image. "
        "Use GoogleLens to identify the object, retrieve its Wikipedia page, and use that context to answer. "
        "Tools: GoogleLens, WikipediaArticle, AnswerWithContext."
    )
)

# 4. TwoHopEncyclopedicAgent
twohop_encyclopedic = AssistantAgent(
    name="TwoHopEncyclopedicAgent",
    system_message=(
        "You solve complex encyclopedic questions that require two steps of reasoning. "
        "First decompose the question, then answer each part using relevant tools or other agents like SingleHopEncyclopedicAgent. "
        "Tools: DecomposeQuestion, GoogleLens, WikipediaArticle."
    )
)
