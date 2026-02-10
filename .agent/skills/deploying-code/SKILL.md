---
name: deploying-code
description: Orchestrates safe production deployments by enforcing pre-flight checks, running tests, and requiring explicit user confirmation. Use when the user asks to deploy, publish, or release code.
---

# Deployment Guard

## When to use this skill
- When the user says "Deploy to production".
- When the user asks to "ship this code" or "make a release".
- When the user references specific deployment environment commands (e.g., `npm run deploy`, `docker push`).

## Workflow
- [ ] **Environment Check**: Identify target environment (Staging vs. Production) and verify permissions.
- [ ] **Sanity Check**: Ensure the git working directory is clean and strictly ahead of remote.
- [ ] **Build Verification**: Run the build script locally to ensure no compile-time errors.
- [ ] **Test Validation**: Execute critical unit/integration tests (`npm test` or equivalent).
- [ ] **Impact & Rollback Plan**: Summarize what is changing and identifying how to undo it if it fails.
- [ ] **Execution**: Run the actual deployment command only after specific user approval.

## Instructions

### strict-safety-rules
1.  **Never Skip Tests**: Unless explicitly overruled with a flag like `--force`, always run the test suite.
2.  **Clean State**: Do not deploy if there are uncommitted changes.
3.  **Explicit Approval**: Present a summary of changes and wait for the user to type "yes" or "approve".

### Pre-Flight Checklist Logic (Bash template)
```bash
# Example generic check
if [[ -n $(git status --porcelain) ]]; then
  echo "❌ Error: Working directory not clean."
  exit 1
fi

npm run build --dry-run
if [ $? -ne 0 ]; then
  echo "❌ Error: Build failed."
  exit 1
fi
```

### Rollback Strategy
- Before deploying, ask: *"Do we have a recent backup or tag?"*
- If the deployment command fails, attempt to restore the previous state immediately if applicable.

## Resources
- Ensure `package.json` has a standard `build` and `test` script.
