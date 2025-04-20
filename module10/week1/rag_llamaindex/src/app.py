from src.rag.main import build_rag_chain, InputQA, OutputQA
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import os
from llama_index.llms.ollama import Ollama
os.environ["TOKENIZERS_PARALLELISM"] = "false"


# Khởi tạo Ollama LLM cho agent với model đã có trên Ollama server
llm = Ollama(
    model="qwen2.5:0.5b",
    # Đảm bảo server Ollama đang chạy ở địa chỉ này
    base_url="http://127.0.0.1:12345",
    request_timeout=360.0
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(BASE_DIR, "..", "data_source")
print(f"Data dir: {data_dir}")
# --------- Chains ---------
genai_chain = build_rag_chain(llm, data_dir=data_dir)

# --------- App - FastAPI ---------
app = FastAPI(
    title="Llama index Server",
    version="1.0",
    description="A simple api server using llama index Runnable interfaces",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# --------- Routes - FastAPI ---------
@app.get("/check")
async def check():
  return {"status": "ok"}

@app.post("/generative_ai", response_model=OutputQA)
async def generative_ai(inputs: InputQA):
  agent_response, _ = await genai_chain.run(inputs.question)
  answer_text = agent_response.response.blocks[0].text
  return {"answer": answer_text}
