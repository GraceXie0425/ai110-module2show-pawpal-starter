from pawpal_system import Owner, Pet, Task, Scheduler, DailyPlan
from datetime import date

# Create an Owner
owner = Owner("John Doe", 120)  # 120 minutes available per day

# Create at least two Pets
pet1 = Pet("Fluffy", "Cat", 3, owner)
pet2 = Pet("Rex", "Dog", 5, owner)

# Add at least three Tasks with different times to those pets
task1 = Task("Feed", "Nutrition", 10, 1, "Morning feed", "daily")
pet1.add_task(task1)

task2 = Task("Walk", "Exercise", 30, 2, "Evening walk", "daily")
pet2.add_task(task2)

task3 = Task("Groom", "Hygiene", 20, 3, "Weekly grooming", "weekly")
pet1.add_task(task3)

# Create Scheduler and generate today's plan
scheduler = Scheduler(owner, owner.available_minutes_per_day)
plan = scheduler.generate_plan(date.today())

# Print "Today's Schedule"
print("Today's Schedule")
print(plan.display())
print()
print("Explanation:")
print(plan.explain())
