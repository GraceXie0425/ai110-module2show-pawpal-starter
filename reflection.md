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

- Did your design change during implementation?
Yes 
- If yes, describe at least one change and why you made it.
Removed `Scheduler.tasks`, added required constructor parameters
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
The scheduler only checks for exact time matches when detecting conflicts, rather than considering overlapping task durations or time ranges.

- Why is that tradeoff reasonable for this scenario?
This tradeoff keeps the conflict detection lightweight and simple, avoiding the complexity of time range calculations. In a pet care context, tasks are often short and flexible, so exact time conflicts serve as useful warnings without overcomplicating the scheduling logic for edge cases like partial overlaps.

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
