# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
The initial UML design centers on five classes with clearly separated responsibilities: `Owner`, `Pet`, `Task`, `Scheduler`, and `DailyPlan`. The diagram models a one-directional flow — owner context feeds into pet, pet holds tasks, the scheduler consumes the pet and tasks to produce a plan.

- What classes did you include, and what responsibilities did you assign to each?
`Owner` -- Stores who the user is and how much time they have available each day. Holds preferences (e.g., prefers morning walks). Responsible for configuring the time budget that constrains scheduling. 
`Pet` -- Represents the animal being cared for (name, species, age) and maintains the list of care tasks associated with it. Acts as the central container linking the owner to the tasks. 
`Task` -- Represents a single unit of care work (e.g., a walk, feeding, medication). Holds the duration and a numeric priority (1=critical, 2=important, 3=optional). Responsible for knowing whether it is high-priority and producing a human-readable summary of itself. 
`Scheduler` -- Contains the scheduling logic. Takes a `Pet` (and its tasks) plus an available-time budget, ranks tasks by priority and duration, and greedily selects tasks that fit within the budget. Responsible for producing a `DailyPlan`. 
`DailyPlan` -- The output of the scheduler. Holds two lists — tasks that made it into the schedule and tasks that were skipped — along with the total time used. Responsible for displaying the plan and explaining why each task was included or excluded. 

**b. Design changes**

Yes, the design changed in four ways after reviewing the initial stubs:

1. **Removed `Scheduler.tasks`** — The original design stored a separate `tasks` list on `Scheduler` in addition to `Scheduler.pet`. This created two sources of truth: if a task was added to the pet after the scheduler was constructed, the scheduler's copy would go stale silently. The fix was to remove `Scheduler.tasks` entirely and always source tasks from `self.pet.get_all_tasks()` at plan-generation time.

2. **Added required constructor parameters** — All `__init__` methods originally took no arguments, leaving every object in an invalid state after construction (e.g., `Task` with `duration_minutes=0`, `priority=0`). Required fields are now enforced in `__init__` so an object cannot exist without its essential data.

3. **Added `Owner.pets` list** — The UML showed a one-to-many relationship from `Owner` to `Pet`, but `Owner` had no attribute to hold pets. A `pets: List[Pet]` list was added, and `Pet.__init__` registers itself on the owner automatically, keeping the relationship consistent in both directions.

4. **Added `pet` reference to `DailyPlan`** — `DailyPlan` originally had no link back to the pet it was generated for, making it impossible to know context when calling `explain()`. A `pet` parameter was added to `DailyPlan.__init__` so the plan always knows which pet it belongs to.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
