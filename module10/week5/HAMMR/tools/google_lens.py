from langchain_community.utilities.google_lens import GoogleLensAPIWrapper
from langchain_community.tools.google_lens.tool import GoogleLensQueryRun
from autogen_ext.tools.langchain import LangChainToolAdapter
import os
os.environ["SERPAPI_API_KEY"] = "8a63f4c93d83b786b9f3cdad06922bf0dea6330d4ec4269d7658b75c46538c6f"


def google_lens(image):
  """Tool: Google Lens – Identify named entity in image."""
  google_lens_api = GoogleLensAPIWrapper()
  google_lens_tool = LangChainToolAdapter(
      GoogleLensQueryRun(api_wrapper=google_lens_api)
  )
  return google_lens_tool.run(image=image)


print(google_lens("https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"))
