# Agent State - Quick Reference

Persistent tooling ecosystem for AI agents to store, share, and reuse scripts, tools, and data across sessions and even across different agents.

## Top-Level Directories

- **scripts/** - Helper scripts, API clients, utilities, and automation tools
- **memory/** - Persistent organizational memory (developers, PMs, systems, context)
- **docs/** - Extended documentation, onboarding guides, best practices
- **context/** - Organizational context, project metadata, domain knowledge
- **templates/** - Reusable templates for common tasks
- **examples/** - Usage examples, tutorials, best practices
- **exchange/** - TRACKED: Small sanitized data artifacts for cross-session sharing
- **workspace/** - UNTRACKED: Temporary files, large artifacts, scratch work

## Editing Rules

- UTF-8 encoding, minimal comments (only TODO for temporary code)
- Non-interactive scripts, JSON output by default, proper exit codes
- Never commit secrets, use env vars (JIRA_AUTH, DEVIN_API, etc.)
- Branch: `devin/{timestamp}-{slug}`, always PR with "devin" label
- exchange/ for small tracked artifacts, workspace/ for temp/large files
- Update folder AGENTS.md when adding tools

## Quick Start

1. Navigate by function (scripts, memory, docs, etc.)
2. Read folder AGENTS.md for available tools
3. Check env var requirements
4. Run tool with proper args
5. Share results via exchange/ (small) or workspace/ (temp)

