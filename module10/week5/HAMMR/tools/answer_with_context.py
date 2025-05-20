from langchain_google_vertexai import VertexAI
import os
from google.cloud import aiplatform


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../credentials/bwa-agents-54872988b93e.json"
aiplatform.init(project='bwa-agents',
                location='us-central1')

vertex_ai_llm = VertexAI(model_name="gemini-2.0-flash-lite-001")
message = "What are some of the pros and cons of Python as a programming language?"
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = vertex_ai_llm.invoke(messages)
print(ai_msg)

def answer_with_context(question, context):
  """Tool: Answer question using text context."""
  pass
