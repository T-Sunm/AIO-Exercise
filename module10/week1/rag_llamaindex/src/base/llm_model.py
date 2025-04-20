from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.ollama import Ollama
import torch
from transformers import BitsAndBytesConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
# from langchain.llms.huggingface_pipeline import HuggingFacePipeline

nf4_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    bnb_4bit_compute_dtype=torch.bfloat16
)

def get_ollama_llms(model_name="qwen2.5:0.5b"):
  llm = Ollama(
      model=model_name,
      # Đảm bảo server Ollama đang chạy ở địa chỉ này
      base_url="http://127.0.0.1:12345",
      request_timeout=360.0
  )

  return llm


# def get_hf_llm(model_name: str = "meta-llama/Llama-3.2-3B-Instruct",
#                max_new_token=1024,
#                **kwargs):

#   model = AutoModelForCausalLM.from_pretrained(
#       model_name,
#       quantization_config=nf4_config,
#       low_cpu_mem_usage=True
#   )
#   tokenizer = AutoTokenizer.from_pretrained(model_name)

#   model_pipeline = pipeline(
#       "text-generation",
#       model=model,
#       tokenizer=tokenizer,
#       max_new_tokens=max_new_token,
#       pad_token_id=tokenizer.eos_token_id,
#       device_map="auto"
#   )

#   llm = HuggingFacePipeline(
#       pipeline=model_pipeline,
#       model_kwargs=kwargs
#   )

#   return llm
