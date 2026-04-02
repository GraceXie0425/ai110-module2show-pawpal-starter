import pytest
from datetime import time
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


def test_sorting_correctness():
    """Verify tasks are returned in chronological order."""
    owner = Owner("Test Owner", 120)
    pet = Pet("Test Pet", "Dog", 2, owner)
    
    # Create tasks with different times
    task1 = Task("Morning Walk", "Exercise", 30, 2, time=time(8, 0))
    task2 = Task("Feed Breakfast", "Nutrition", 10, 1, time=time(7, 0))
    task3 = Task("Evening Walk", "Exercise", 30, 2, time=time(18, 0))
    task4 = Task("No Time Task", "Other", 5, 3)  # No time specified
    
    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)
    pet.add_task(task4)
    
    scheduler = Scheduler(owner, 120)
    sorted_tasks = scheduler.sort_by_time()
    
    # Verify chronological order: 7:00, 8:00, 18:00, then no time (should be last)
    assert sorted_tasks[0].name == "Feed Breakfast"
    assert sorted_tasks[1].name == "Morning Walk"
    assert sorted_tasks[2].name == "Evening Walk"
    assert sorted_tasks[3].name == "No Time Task"


def test_recurrence_logic():
    """Confirm that marking a daily task complete creates a new task for the following day."""
    owner = Owner("Test Owner", 60)
    pet = Pet("Test Pet", "Dog", 2, owner)
    
    # Create a daily task
    task = Task("Daily Walk", "Exercise", 20, 2, frequency="daily")
    pet.add_task(task)
    
    initial_task_count = len(pet.tasks)
    
    # Mark the task complete
    task.mark_complete()
    
    # Verify a new task is created
    assert len(pet.tasks) == initial_task_count + 1
    new_task = pet.tasks[-1]  # The newly added task
    assert new_task.name == "Daily Walk"
    assert new_task.frequency == "daily"
    assert not new_task.completed
    assert new_task.pet == pet


def test_conflict_detection():
    """Verify that the Scheduler flags duplicate times."""
    owner = Owner("Test Owner", 120)
    pet = Pet("Test Pet", "Dog", 2, owner)
    
    # Create tasks at the same time
    task1 = Task("Morning Walk", "Exercise", 30, 2, time=time(8, 0))
    task2 = Task("Feed Breakfast", "Nutrition", 10, 1, time=time(8, 0))
    
    pet.add_task(task1)
    pet.add_task(task2)
    
    scheduler = Scheduler(owner, 120)
    plan = scheduler.generate_plan()
    
    # Verify conflict is detected
    assert len(plan.conflicts) > 0
    assert "Conflict at 08:00:00" in plan.conflicts[0] or "08:00:00" in plan.conflicts[0]
