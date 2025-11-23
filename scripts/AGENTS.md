# Scripts

Helper scripts, API clients, utilities, and automation tools for agents.

## Available Scripts

### devin_api_client.py

**Purpose**: Devin API client for spawning and managing Devin sessions.

**Usage**:
```bash
python3 scripts/devin_api_client.py spawn --repo my-repo --task "Implement feature X"
```

**Env Vars**:
- `DEVIN_API` - Devin API authentication token

**Features**:
- Spawn new Devin sessions
- Monitor session status
- Create new sessions with context summarization
- Automatic session management for large tasks or context limits

## Adding New Scripts

When adding a new script:
1. Add it to this directory
2. Update this AGENTS.md with usage instructions
3. Document required environment variables
4. Ensure non-interactive operation with JSON output when possible

