import pathlib
from ..core.agent_base import MCPAgent

class QAAgent(MCPAgent):
    def __init__(self):
        prompt = pathlib.Path("conf/prompts/qa.md").read_text()
        tools = ["bash", "task_done"]
        super().__init__(role="qa", system_prompt=prompt, allowed_tools=tools)
