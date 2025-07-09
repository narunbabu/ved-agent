import pathlib
from ..core.agent_base import MCPAgent

class BuilderAgent(MCPAgent):
    def __init__(self):
        prompt = pathlib.Path("conf/prompts/builder.md").read_text()
        tools = ["str_replace_based_edit_tool", "bash", "task_done"]
        super().__init__(role="builder", system_prompt=prompt, allowed_tools=tools)
