from pawpal_system import Owner, Pet, Task, Scheduler, DailyPlan
from datetime import date, time

# Create an Owner
owner = Owner("John Doe", 120)  # 120 minutes available per day

# Create at least two Pets
pet1 = Pet("Fluffy", "Cat", 3, owner)
pet2 = Pet("Rex", "Dog", 5, owner)

# Add at least three Tasks with different times to those pets
task3 = Task("Groom", "Hygiene", 20, 3, "Weekly grooming", "weekly", False, time(14, 0))
pet1.add_task(task3)

task1 = Task("Feed", "Nutrition", 10, 1, "Morning feed", "daily", False, time(8, 0))
pet1.add_task(task1)

task2 = Task("Walk", "Exercise", 30, 2, "Evening walk", "daily", False, time(18, 0))
pet2.add_task(task2)

task4 = Task("Brush", "Hygiene", 15, 2, "Morning brush", "daily", False, time(8, 0))
pet2.add_task(task4)

# Create Scheduler and generate today's plan
scheduler = Scheduler(owner, owner.available_minutes_per_day)
plan = scheduler.generate_plan(date.today())

# Print "Today's Schedule"
print("Today's Schedule")
print(plan.display())
print()
print("Explanation:")
print(plan.explain())

# Demonstrate sorting and filtering
print("\nTasks sorted by time:")
sorted_tasks = scheduler.sort_by_time()
for task in sorted_tasks:
    print(f"- {task.summary()}")

print("\nPending tasks:")
pending_tasks = scheduler.filter_by_completion(False)
for task in pending_tasks:
    print(f"- {task.summary()}")

print("\nTasks for Fluffy:")
fluffy_tasks = scheduler.filter_by_pet("Fluffy")
for task in fluffy_tasks:
    print(f"- {task.summary()}")

# Mark the Feed task complete to test recurrence
task1.mark_complete()

print("\nAfter marking Feed complete, tasks for Fluffy:")
fluffy_tasks_after = scheduler.filter_by_pet("Fluffy")
for task in fluffy_tasks_after:
    print(f"- {task.summary()}")
