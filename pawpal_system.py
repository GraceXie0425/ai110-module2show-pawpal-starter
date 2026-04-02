from typing import List, Dict, Any, Optional
from datetime import date


class Owner:
    def __init__(self, name: str, available_minutes_per_day: int):
        self.name: str = name
        self.available_minutes_per_day: int = available_minutes_per_day
        self.preferences: Dict[str, Any] = {}
        self.pets: List['Pet'] = []

    def set_available_time(self, minutes: int):
        """Set the available time per day in minutes."""
        self.available_minutes_per_day = minutes

    def add_preference(self, key: str, value):
        """Add or update a preference."""
        self.preferences[key] = value

    def get_all_tasks(self) -> List['Task']:
        """Get all tasks from all pets."""
        return [task for pet in self.pets for task in pet.get_all_tasks()]


class Pet:
    def __init__(self, name: str, species: str, age: int, owner: 'Owner'):
        self.name: str = name
        self.species: str = species
        self.age: int = age
        self.owner: Owner = owner
        self.tasks: List['Task'] = []
        owner.pets.append(self)

    def add_task(self, task: 'Task'):
        """Add a task to the pet."""
        self.tasks.append(task)

    def remove_task(self, task: 'Task'):
        """Remove a task from the pet if it exists."""
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self) -> List['Task']:
        """Get a copy of all tasks for the pet."""
        return self.tasks.copy()


class Task:
    def __init__(self, name: str, category: str, duration_minutes: int, priority: int, notes: str = "", frequency: str = "daily", completed: bool = False):
        self.name: str = name
        self.category: str = category
        self.duration_minutes: int = duration_minutes
        self.priority: int = priority  # 1=critical, 2=important, 3=optional
        self.notes: str = notes
        self.frequency: str = frequency
        self.completed: bool = completed

    def is_high_priority(self) -> bool:
        """Check if the task is high priority (priority 1)."""
        return self.priority == 1

    def summary(self) -> str:
        """Get a summary string of the task."""
        status = "completed" if self.completed else "pending"
        return f"{self.name} ({self.category}): {self.duration_minutes} min, priority {self.priority}, {self.frequency}, {status}"

    def mark_complete(self):
        """Mark the task as completed."""
        self.completed = True


class Scheduler:
    def __init__(self, owner: 'Owner', available_minutes: int):
        self.owner: Owner = owner
        self.available_minutes: int = available_minutes

    def generate_plan(self, plan_date: date = None) -> 'DailyPlan':
        """Generate a daily plan by ranking and scheduling tasks."""
        tasks = self.owner.get_all_tasks()
        ranked_tasks = self._rank_tasks(tasks)
        scheduled = []
        time_used = 0
        for task in ranked_tasks:
            if time_used + task.duration_minutes <= self.available_minutes:
                scheduled.append(task)
                time_used += task.duration_minutes
            else:
                break
        skipped = [t for t in ranked_tasks if t not in scheduled]
        plan_date = plan_date or date.today()
        return DailyPlan(scheduled, skipped, time_used, plan_date, None)

    def _rank_tasks(self, tasks: List['Task'] = None) -> List['Task']:
        """Rank tasks by priority then duration."""
        if tasks is None:
            tasks = self.owner.get_all_tasks()
        return sorted(tasks, key=lambda t: (t.priority, t.duration_minutes))


class DailyPlan:
    def __init__(self, scheduled_tasks: List['Task'], skipped_tasks: List['Task'],
                 total_time_used: int, plan_date: date, pet: Optional['Pet'] = None):
        self.scheduled_tasks: List[Task] = scheduled_tasks
        self.skipped_tasks: List[Task] = skipped_tasks
        self.total_time_used: int = total_time_used
        self.date: date = plan_date
        self.pet: Optional[Pet] = pet

    def display(self) -> str:
        """Display the daily plan as a formatted string."""
        pet_name = self.pet.name if self.pet else "all pets"
        scheduled_str = "\n".join([f"- {task.summary()}" for task in self.scheduled_tasks])
        skipped_str = "\n".join([f"- {task.summary()}" for task in self.skipped_tasks])
        return f"Daily Plan for {pet_name} on {self.date}:\nScheduled Tasks:\n{scheduled_str}\nSkipped Tasks:\n{skipped_str}\nTotal Time: {self.total_time_used} minutes"

    def explain(self) -> str:
        """Provide an explanation of the plan."""
        pet_ref = f" for {self.pet.name}" if self.pet else ""
        return f"This plan prioritizes critical tasks first, then important ones{pet_ref}, fitting as many as possible within available time. {len(self.scheduled_tasks)} tasks scheduled, {len(self.skipped_tasks)} skipped due to time constraints."
