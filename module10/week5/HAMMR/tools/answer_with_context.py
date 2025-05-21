from langchain_google_vertexai import VertexAI
import os
from google.cloud import aiplatform
from autogen_core.tools import FunctionTool
from pathlib import Path

CREDENTIALS_PATH = Path(__file__).parent.parent / \
    "credentials" / "bwa-agents-54872988b93e.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = str(CREDENTIALS_PATH.resolve())
aiplatform.init(project='bwa-agents',
                location='us-central1')


def answer_with_context(question: str, context: str) -> str:
  """
  Tool: Answer the question using the provided text context.
  """

  vertex_ai_llm = VertexAI(model_name="gemini-2.0-flash-lite-001")
  prompt = (
      f"You are an expert assistant. Answer the following question strictly using the provided context only.\n\n"
      f"Context:\n{context}\n\n"
      f"Question:\n{question}\n"
      "Answer:"
  )
  return vertex_ai_llm.invoke(prompt)


answer_with_context_tool = FunctionTool(
    answer_with_context,
    description="Answer a question using ONLY the provided context (no outside knowledge)."
)

# question = "What is the capital of France?"
# context = "France is a country in Europe. The capital of France is Paris."
# result = answer_with_context(question, context)
# print(result)
