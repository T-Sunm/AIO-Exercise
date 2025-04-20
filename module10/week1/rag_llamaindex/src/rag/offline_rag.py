import os
from llama_index.llms.ollama import Ollama
from src.rag.vectorstore import VectorPipeline
from llama_index.core.agent.workflow import (
    AgentWorkflow,
    FunctionAgent,
    ReActAgent,
)
from llama_index.core.tools import QueryEngineTool

from llama_index.core.workflow import Context
DB_PATH = "./alfred_chroma_db"
COLLECTION_NAME = "alfred"


class AlfredAgentSystem:
  def __init__(self, llm, query_engine):
    self.llm = llm
    self.query_engine = query_engine
    self.workflow = self._build_workflow()
    self.ctx = Context(self.workflow)

  async def query_with_state(self, ctx: Context, query: str) -> str:
    """Search and retrieve info from ML/DL research papers."""
    state = await ctx.get("state") or {}
    state["num_fn_calls"] = state.get("num_fn_calls", 0) + 1
    await ctx.set("state", state)
    response = self.query_engine.query(query)
    return str(response)

  async def add(self, ctx: Context, a: int, b: int) -> int:
    state = await ctx.get("state") or {}
    state["num_fn_calls"] = state.get("num_fn_calls", 0) + 1
    await ctx.set("state", state)
    return a + b

  async def subtract(self, ctx: Context, a: int, b: int) -> int:
    state = await ctx.get("state") or {}
    state["num_fn_calls"] = state.get("num_fn_calls", 0) + 1
    await ctx.set("state", state)
    return a - b

  async def multiply(self, ctx: Context, a: int, b: int) -> int:
    state = await ctx.get("state") or {}
    state["num_fn_calls"] = state.get("num_fn_calls", 0) + 1
    await ctx.set("state", state)
    return a * b

  def _build_workflow(self):
    # Agents
    calculator_agent = ReActAgent(
        name="calculator",
        description="Performs basic arithmetic operations",
        system_prompt="You are a calculator assistant. Use your tools for any math operation.",
        tools=[self.add, self.subtract, self.multiply],
        llm=self.llm,
    )

    query_agent = ReActAgent(
        name="ml_paper_agent",
        description="Agent that answers questions using information from machine learning and deep learning research papers.",
        system_prompt="You are an academic assistant. Use your tool to search through stored research papers related to machine learning and deep learning and return accurate, concise answers based on that information.",
        tools=[self.query_with_state],
        llm=self.llm,
    )

    # Workflow
    return AgentWorkflow(
        agents=[calculator_agent, query_agent],
        root_agent="ml_paper_agent",
        initial_state={"num_fn_calls": 0},
        state_prompt="You have access to state tracking. Current state: {state}. User message: {msg}",
    )

  async def run(self, user_msg: str):
    response = await self.workflow.run(user_msg=user_msg, ctx=self.ctx)
    state = await self.ctx.get("state")
    return response, state.get("num_fn_calls", 0)
