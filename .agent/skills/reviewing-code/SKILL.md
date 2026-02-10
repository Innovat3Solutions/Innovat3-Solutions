---
name: reviewing-code
description: Reviews code changes for security, performance, readability, and correctness. Use when the user asks to review usage, check for bugs, or critique a specific file or block of code.
---

# Code Reviewer

## When to use this skill
- When the user asks "Review this code" or "What's wrong with this?".
- When the user provides a specific file or snippet and asks for feedback.
- When the user asks to check for security vulnerabilities or performance issues.

## Workflow
- [ ] **Context Analysis**: Identify technical constraints (language, framework) and user intent (security audit vs. style check).
- [ ] **Static Analysis**: Scan for syntax errors, logical bugs, and type mismatches.
- [ ] **Best Practices Check**: Verify adherence to standard patterns (e.g., DRY, SOLID) and specific framework idioms.
- [ ] **Security & Performance**: Look for common vulnerabilities (injection, XSS) and O(N^2) or worse complexities.
- [ ] **Report Generation**: Output findings categorized by severity (Critical, Warning, Nitpick).

## Instructions

### Review Priorities
1.  **Correctness**: Does the code do what it claims?
2.  **Security**: Are there any un-sanitized inputs or exposed secrets?
3.  **Performance**: Are there obvious bottlenecks?
4.  **Readability**: Is naming clear? Are functions small and focused?

### Feedback Style
- **Be Specific**: Quote the exact line number and code snippet.
- **Explain "Why"**: Don't just say "change this"; explain the benefit (e.g., "avoids a race condition").
- **Provide Alternatives**: Show a refactored version using a markdown code block.

### Output Format
For each issue found:
- **Severity**: [Critical/Warning/Info]
- **Location**: `filename:line`
- **Issue**: Brief description.
- **Recommendation**: Suggested fix.

Example:
> **Severity**: Critical
> **Location**: `server/auth.ts:42`
> **Issue**: Hardcoded secret key.
> **Recommendation**: Use `process.env.SECRET_KEY` instead.

## Resources
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) (General security reference)
