---
name: writing-plans
description: Generates detailed implementation plans for multi-step tasks before coding. Use when you have a spec or requirements and need to break them down into bite-sized, test-driven steps.
---

# Writing Plans

## When to use this skill
- When you have a spec or requirements for a multi-step task.
- Before writing any code for a complex feature.
- When you need to document a plan for another agent or developer to execute.

## Workflow
- [ ] **Context Setup**: Ensure you are in a dedicated worktree or branch.
- [ ] **Header Creation**: Start with a standard header defining the goal, architecture, and tech stack.
- [ ] **Task Breakdown**: Break the feature into granular, bite-sized tasks (2-5 minutes execution time).
- [ ] **Review**: Validate the plan against DRY, YAGNI, and TDD principles.
- [ ] **Handoff**: Save the plan and offer execution options (Subagent-Driven vs. Parallel Session).

## Instructions

### Bite-Sized Task Granularity
Each step must be a single action taking 2-5 minutes:
1.  "Write the failing test"
2.  "Run it to make sure it fails"
3.  "Implement the minimal code to make the test pass"
4.  "Run the tests and make sure they pass"
5.  "Commit"

### Plan Document Header
Every plan MUST start with this header:

```markdown
# [Feature Name] Implementation Plan

> **For Agent:** REQUIRED SUB-SKILL: Use `executing-plans` (if available) to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

### Task Structure Template
```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test**
[Code Block]

**Step 2: Run test to verify it fails**
Run: `[Command]`
Expected: FAIL with "[Error]"

**Step 3: Write minimal implementation**
[Code Block]

**Step 4: Run test to verify it passes**
Run: `[Command]`
Expected: PASS

**Step 5: Commit**
```bash
git add [files]
git commit -m "feat: [message]"
```
```

### Execution Handoff
After saving the plan to `docs/plans/YYYY-MM-DD-<feature-name>.md`:
1.  **Subagent-Driven**: Dispatch fresh subagent per task.
2.  **Parallel Session**: Open new session with `executing-plans`.

## Resources
- Ensure `tests/` directory exists and is configured.
