import streamlit as st
from pawpal_system import Owner, Pet, Task

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs")
owner_name = st.text_input("Owner name", value="Jordan")
available_time = st.number_input("Available time per day (minutes)", min_value=1, max_value=480, value=120)

# Initialize Owner in session state
if 'owner' not in st.session_state:
    st.session_state.owner = Owner(owner_name, available_time)
elif st.session_state.owner.name != owner_name or st.session_state.owner.available_minutes_per_day != available_time:
    # Update if inputs changed
    st.session_state.owner = Owner(owner_name, available_time)

owner = st.session_state.owner

st.markdown("### Add a Pet")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
pet_age = st.number_input("Age", min_value=0, max_value=30, value=2)

if st.button("Add Pet"):
    Pet(pet_name, species, pet_age, owner)
    st.success(f"Added pet {pet_name}!")
    st.rerun()  # Refresh to show updated list

# Display current pets
if owner.pets:
    st.write("Current pets:")
    for pet in owner.pets:
        st.write(f"- {pet.name} ({pet.species}, {pet.age} years old)")
else:
    st.info("No pets added yet.")

st.markdown("### Add a Task")
if owner.pets:
    selected_pet = st.selectbox("Select pet for task", [pet.name for pet in owner.pets])
    task_name = st.text_input("Task name", value="Morning walk")
    category = st.selectbox("Category", ["Nutrition", "Exercise", "Hygiene", "Other"])
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority_options = {1: "Critical", 2: "Important", 3: "Optional"}
    priority = st.selectbox("Priority", list(priority_options.values()), index=1)
    priority_num = {v: k for k, v in priority_options.items()}[priority]
    notes = st.text_input("Notes", value="")

    if st.button("Add Task"):
        pet = next(p for p in owner.pets if p.name == selected_pet)
        task = Task(task_name, category, duration, priority_num, notes)
        pet.add_task(task)
        st.success(f"Added task '{task_name}' to {pet.name}!")
        st.rerun()

    # Display tasks for each pet
    for pet in owner.pets:
        if pet.tasks:
            st.write(f"Tasks for {pet.name}:")
            for task in pet.tasks:
                st.write(f"- {task.summary()}")
else:
    st.info("Add a pet first to add tasks.")

st.divider()

st.subheader("Generate Schedule")
st.caption("Generate a daily schedule based on your pets' tasks.")

if st.button("Generate Schedule"):
    if owner.pets and any(pet.tasks for pet in owner.pets):
        from pawpal_system import Scheduler
        scheduler = Scheduler(owner, owner.available_minutes_per_day)
        plan = scheduler.generate_plan()
        st.success("Schedule generated!")
        st.markdown("### Today's Schedule")
        st.code(plan.display())
        st.markdown("### Explanation")
        st.write(plan.explain())
    else:
        st.warning("Add pets and tasks first.")
