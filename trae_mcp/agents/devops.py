import pathlib
from ..core.agent_base import MCPAgent

class DevOpsAgent(MCPAgent):
    def __init__(self):
        prompt = pathlib.Path("conf/prompts/devops.md").read_text()
        tools = ["bash", "task_done"]
        super().__init__(role="devops", system_prompt=prompt, allowed_tools=tools)
