from langchain_community.utilities.google_lens import GoogleLensAPIWrapper
from autogen_core.tools import FunctionTool


def google_lens(image: str):
  """Tool: Google Lens – Identify named entity in image."""
  google_lens_api = GoogleLensAPIWrapper(
      serp_api_key="8a63f4c93d83b786b9f3cdad06922bf0dea6330d4ec4269d7658b75c46538c6f")

  return google_lens_api.run(image)


google_lens_tool = FunctionTool(
    google_lens,
    description="Identify the main entity or object in the given image URL using Google Lens via SerpAPI."
)
# print(google_lens("https://images.pexels.com/photos/2071882/pexels-photo-2071882.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"))
