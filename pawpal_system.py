from typing import List, Dict, Any, Optional
from datetime import date


class Owner:
    def __init__(self):
        self.name: str = ""
        self.available_minutes_per_day: int = 0
        self.preferences: Dict[str, Any] = {}

    def set_available_time(self, minutes: int):
        pass

    def add_preference(self, key: str, value):
        pass


class Pet:
    def __init__(self):
        self.name: str = ""
        self.species: str = ""
        self.age: int = 0
        self.owner: Optional['Owner'] = None
        self.tasks: List['Task'] = []

    def add_task(self, task: 'Task'):
        pass

    def remove_task(self, task: 'Task'):
        pass

    def get_all_tasks(self) -> List['Task']:
        pass


class Task:
    def __init__(self):
        self.name: str = ""
        self.category: str = ""
        self.duration_minutes: int = 0
        self.priority: int = 0
        self.notes: str = ""

    def is_high_priority(self) -> bool:
        pass

    def summary(self) -> str:
        pass


class Scheduler:
    def __init__(self):
        self.pet: Optional['Pet'] = None
        self.available_minutes: int = 0
        self.tasks: List['Task'] = []

    def generate_plan(self) -> 'DailyPlan':
        pass

    def _rank_tasks(self) -> List['Task']:
        pass


class DailyPlan:
    def __init__(self):
        self.scheduled_tasks: List['Task'] = []
        self.skipped_tasks: List['Task'] = []
        self.total_time_used: int = 0
        self.date: Optional[date] = None

    def display(self) -> str:
        pass

    def explain(self) -> str:
        pass
