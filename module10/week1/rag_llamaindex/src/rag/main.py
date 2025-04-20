from pydantic import BaseModel, Field

from src.rag.file_loader import Loader
from src.rag.vectorstore import VectorPipeline
from src.rag.offline_rag import AlfredAgentSystem
import os
import asyncio


DB_PATH = "./alfred_chroma_db"
class InputQA(BaseModel):
  question: str = Field(..., title="Question to ask the model")

class OutputQA(BaseModel):
  answer: str = Field(..., title="Answer from the model")

def build_rag_chain(llm, data_dir):
  db_exists = os.path.exists(DB_PATH) and len(os.listdir(DB_PATH)) > 0
  if not db_exists:
    doc_loaded = Loader(data_dir, workers=2).get_documents()
  else:
    doc_loaded = []

  query_engine = VectorPipeline(
      documents=doc_loaded, db_path=DB_PATH).get_query_engine(
          llm=llm,
          search_type="similarity",
          search_kwargs={"k": 10},
          response_mode="tree_summarize",
  )
  rag_chain = AlfredAgentSystem(llm, query_engine)
  return rag_chain
