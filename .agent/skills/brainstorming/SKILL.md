---
name: brainstorming
description: Explores user intent, requirements, and design before implementation. Use before any creative work to turn ideas into fully formed designs and specs through natural collaborative dialogue.
---

# Brainstorming Ideas Into Designs

## When to use this skill
- Before creating features, building components, or adding functionality.
- When the user's requirements are vague or need refinement.
- When you need to understand the "why" and "how" before the "what".

## Workflow
- [ ] **Understanding**: Check current project state, ask questions one at a time to refine the idea.
- [ ] **Exploring**: Propose 2-3 different approaches with trade-offs.
- [ ] **Presenting**: specific design sections (200-300 words), validating each.
- [ ] **Documentation**: Write the validated design to `docs/plans/`.

## Instructions

### The Process

**1. Understanding the idea**
- Check out the current project state first (files, docs).
- Ask **one question per message**.
- Prefer multiple choice questions.
- Focus on purpose, constraints, and success criteria.

**2. Exploring approaches**
- Propose 2-3 different approaches.
- Present options conversationally with your recommendation and reasoning.
- Lead with your recommended option.

**3. Presenting the design**
- Break it into sections of 200-300 words.
- Ask after each section whether it looks right so far.
- Cover: architecture, components, data flow, error handling, testing.

### Key Principles
- **One question at a time**: Don't overwhelm.
- **YAGNI ruthlessly**: Remove unnecessary features.
- **Incremental validation**: particular sections at a time.
- **Be flexible**: Clarify if something doesn't make sense.

### After the Design
- Write the validated design to `docs/plans/YYYY-MM-DD-<topic>-design.md`.
- Commit the design document to git.
- **Transition**: Ask "Ready to set up for implementation?" and reference `writing-plans`.

## Resources
- Store designs in `docs/plans/` directory.
