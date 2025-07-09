import pathlib
import time
from ..core.mcp import MCP
from .builder import BuilderAgent
from .qa import QAAgent
from .devops import DevOpsAgent

class Orchestrator:
    def __init__(self, spec_path: str):
        try:
            import yaml
        except ImportError as exc:
            raise ImportError(
                "PyYAML is required to parse backlog files. Install with 'pip install pyyaml'."
            ) from exc

        self.backlog = yaml.safe_load(pathlib.Path(spec_path).read_text())
        self.agents = {
            "builder": BuilderAgent(),
            "qa": QAAgent(),
            "devops": DevOpsAgent(),
        }
        print("\u2705 Orchestrator initialized.")

    def run(self):
        print("\ud83d\ude80 Starting project execution...")
        for i, task_info in enumerate(self.backlog):
            role = task_info.get("agent")
            description = task_info.get("description")
            print(f"\n---==[ Step {i+1}/{len(self.backlog)}: Running {role.upper()} ]==---")
            worker_agent = self.agents.get(role)
            if not worker_agent:
                print(f"\u274c ERROR: No agent for role '{role}'. Halting.")
                break
            mcp = MCP.new(role=role, task=description, context={"project_path": "."})
            result_mcp = worker_agent.run_task(mcp)
            if result_mcp.status != "SUCCESS":
                print(f"\u274c FATAL: Task {result_mcp.id} failed. Halting execution.")
                break
            time.sleep(1)
        print("\n\ud83c\udf89 Project backlog complete!")
