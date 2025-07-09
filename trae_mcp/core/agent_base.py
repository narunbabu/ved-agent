import asyncio
from trae_agent.agent.trae_agent import TraeAgent
from trae_agent.utils.config import Config
from trae_agent.utils.llm_basics import LLMMessage
from .mcp import MCP

class MCPAgent(TraeAgent):
    def __init__(self, role: str, system_prompt: str, allowed_tools: list[str]):
        agent_config = Config({"default_provider": "anthropic", "max_steps": 25})
        super().__init__(agent_config)
        self.role = role
        self.base_system_prompt = system_prompt
        self.allowed_tools = allowed_tools

    def run_task(self, mcp_task: MCP) -> MCP:
        print(f"[{self.role.upper()}] Running task: {mcp_task.id}...")
        task_args = {"project_path": mcp_task.context.get("project_path", ".")}
        self.new_task(
            task=mcp_task.task_description,
            extra_args=task_args,
            tool_names=self.allowed_tools,
        )
        self.initial_messages[0] = LLMMessage(role="system", content=self.base_system_prompt)
        execution_result = asyncio.run(self.execute_task())
        mcp_task.status = "SUCCESS" if execution_result.success else "FAILED"
        mcp_task.result_details = {"summary": execution_result.final_result}
        print(
            f"[{self.role.upper()}] Finished task {mcp_task.id} with status: {mcp_task.status}"
        )
        return mcp_task
