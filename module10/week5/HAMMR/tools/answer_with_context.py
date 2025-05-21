from langchain_google_vertexai import VertexAI
import os
from google.cloud import aiplatform
from autogen_core.tools import FunctionTool
from autogen_core import CancellationToken

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../credentials/bwa-agents-54872988b93e.json"
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
  # Call Gemini or other LLM (vertex_ai_llm ở ngoài hàm để dùng lại)
  return vertex_ai_llm.invoke(prompt)


# Đăng ký tool với FunctionTool (cần description rõ ràng)
answer_with_context_tool = FunctionTool(
    answer_with_context,
    description="Answer a question using ONLY the provided context (no outside knowledge)."
)

# question = "What is the capital of France?"
# context = "France is a country in Europe. The capital of France is Paris."
# result = answer_with_context(question, context)
# print(result)
