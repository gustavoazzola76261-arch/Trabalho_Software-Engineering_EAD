from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Task:
    id: int
    title: str
    description: str = ''
    status: str = 'todo'

    def to_dict(self):
        return {"id": self.id, "title": self.title, "description": self.description, "status": self.status}

class InMemoryStore:
    def __init__(self):
        self._data: Dict[int, Task] = {}
        self._next = 1

    def create(self, title: str, description: str = '') -> Task:
        t = Task(id=self._next, title=title, description=description)
        self._data[self._next] = t
        self._next += 1
        return t

    def list(self) -> List[Task]:
        return list(self._data.values())

    def get(self, id: int) -> Optional[Task]:
        return self._data.get(id)

    def update(self, task: Task) -> bool:
        if task.id in self._data:
            self._data[task.id] = task
            return True
        return False

    def delete(self, id: int) -> bool:
        return self._data.pop(id, None) is not None
