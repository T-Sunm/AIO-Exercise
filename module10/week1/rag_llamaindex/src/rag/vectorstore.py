from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore
import chromadb
from llama_index.core import VectorStoreIndex
from src.rag.file_loader import PDFLoader
import asyncio

class VectorPipeline:
  def __init__(
      self,
      documents,
      embedding_model_name="BAAI/bge-small-en-v1.5",
      chunk_overlap=0,
      db_path="./alfred_chroma_db",
      collection_name="alfred",
  ) -> None:

    self.documents = documents
    self.embedding_model_name = embedding_model_name
    self.db_path = db_path
    self.collection_name = collection_name

    # Embedding
    self.embedding = HuggingFaceEmbedding(
        model_name=self.embedding_model_name)

    # Setup Chroma
    self.chroma_client = chromadb.PersistentClient(path=self.db_path)
    self.chroma_collection = self.chroma_client.get_or_create_collection(
        name=self.collection_name
    )
    self.vector_store = ChromaVectorStore(
        chroma_collection=self.chroma_collection)

    # Check nếu cần ingest
    if self._should_ingest():
      print("📥 Ingesting documents into vector store...")
      self.pipeline = IngestionPipeline(
          transformations=[
              SentenceSplitter(
                  chunk_overlap=chunk_overlap, chunk_size=300),
              self.embedding,
          ],
          vector_store=self.vector_store,
      )
      self._build_db()
    else:
      print("✅ Vector DB already exists – skip ingest.")

  def _should_ingest(self):
    try:
      return self.chroma_collection.count() == 0
    except Exception as e:
      print(f"⚠️ Lỗi khi kiểm tra collection: {e}")
      return True

  async def _build_db(self):
    await self.pipeline.arun(documents=self.documents)

  def get_query_engine(self, llm, search_type="similarity", search_kwargs={"k": 10}, response_mode="tree_summarize"):
    # Dùng lại vector store và embedding model
    index = VectorStoreIndex.from_vector_store(
        vector_store=self.vector_store,
        embed_model=self.embedding
    )
    return index.as_query_engine(
        llm=llm,
        search_type=search_type,
        search_kwargs=search_kwargs,
        response_mode=response_mode,
    )
