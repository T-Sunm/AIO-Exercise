from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from typing_extensions import Annotated
from autogen_core.tools import FunctionTool

def wikipedia_article(entity: Annotated[str, "Entity or topic to retrieve Wikipedia article for"]) -> str:
  """Tool: Retrieve Wikipedia article summary for given entity."""
  wikipedia_api = WikipediaAPIWrapper()
  return wikipedia_api.run(entity)


wikipedia_article_tool = FunctionTool(
    wikipedia_article,
    description="Retrieve Wikipedia article summary for a given entity or topic."
)
