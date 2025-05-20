from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from autogen_ext.tools.langchain import LangChainToolAdapter

def wikipedia_article(entity):
  """Tool: Retrieve Wikipedia article for given entity."""
  wikipedia_tool = LangChainToolAdapter(WikipediaQueryRun())
  return wikipedia_tool.run(entity=entity)
