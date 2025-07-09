import json
import uuid
from dataclasses import dataclass, asdict

@dataclass
class MCP:
    id: str
    role: str
    task_description: str
    context: dict
    status: str = "PENDING"
    result_details: dict | None = None

    @classmethod
    def new(cls, role: str, task: str, context: dict | None = None):
        return cls(str(uuid.uuid4()), role, task, context or {})

    def to_json(self):
        return json.dumps(asdict(self))
