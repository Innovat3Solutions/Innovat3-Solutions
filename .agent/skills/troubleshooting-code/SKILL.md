---
name: troubleshooting-code
description: Uses master error handling patterns to troubleshoot applications and make them resilient. Use when implementing error handling, designing APIs, or debugging production issues.
---

# Error Handling Patterns & Troubleshooting

## When to use this skill
- When debugging production issues, improving application reliability, or fixing bugs.
- When designing APIs or implementing error handling logic.
- When creating retry mechanisms, circuit breakers, or robust error messages.
- When the user asks to "troubleshoot" an application.

## Workflow
- [ ] **Analyze**: Identify the type of error (Recoverable vs. Unrecoverable) and the context (Network, Validation, Programming bug).
- [ ] **Strategy Selection**: Choose the right pattern (Result Type vs. Exception) based on the language and severity.
- [ ] **Implementation**: Apply specific patterns like Retry with Backoff, Circuit Breaker, or Error Aggregation.
- [ ] **Validation**: Ensure errors are strictly typed, contexts are preserved, and resources are cleaned up.

## Instructions

### Core Philosophies
- **Exceptions**: For unexpected, exceptional conditions (e.g., Disk full).
- **Result Types**: For expected failures (e.g., Validation failed).
- **Fail Fast**: Validate input early.

### Language-Specific Implementations

**Python**
- **Skelton**: Use `ApplicationError` base class with `code` and `details`.
- **Pattern**: `database_transaction` context manager for auto-rollback.
- **Pattern**: `@retry` decorator with exponential backoff.

**TypeScript/JavaScript**
- **Skelton**: Custom `ApplicationError` extending `Error` with `statusCode`.
- **Pattern**: `Result<T, E>` type for functional error handling.
- **Pattern**: Global async error handler for Promises.

**Go**
- **Pattern**: Explicit error returns (`val, err := func()`).
- **Pattern**: Wrapped errors (`fmt.Errorf("...: %w", err)`).

### Universal Patterns
1.  **Circuit Breaker**: Detect cascading failures. State machine: Closed -> Open -> Half-Open.
2.  **Error Aggregation**: Collect multiple validation errors before failing (`ErrorCollector`).
3.  **Graceful Degradation**: `with_fallback(primary, fallback)`.

### Best Practices Checklist
- [ ] **Meaningful Messages**: Explain *what*, *why*, and *how to fix*.
- [ ] **Clean Up**: Always use `finally`, `defer`, or context managers.
- [ ] **No Silent Failures**: Never use empty catch blocks.
- [ ] **Type Safety**: Use custom error types/enums, not string matching.

## Resources
- **Checklist**: `assets/error-handling-checklist.md`
- **Guide**: `assets/error-message-guide.md`
