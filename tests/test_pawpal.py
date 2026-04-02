import pytest
from pawpal_system import Owner, Pet, Task, Scheduler, DailyPlan


def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    task = Task("Feed", "Nutrition", 10, 1)
    assert not task.completed
    task.mark_complete()
    assert task.completed


def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    owner = Owner("Test Owner", 60)
    pet = Pet("Test Pet", "Dog", 2, owner)
    initial_count = len(pet.tasks)
    task = Task("Walk", "Exercise", 20, 2)
    pet.add_task(task)
    assert len(pet.tasks) == initial_count + 1
