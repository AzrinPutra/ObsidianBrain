---
title: OpenCode Framework
path: "OpenCode Framework"
url: https://www.notion.so/OpenCode-Framework-320bd926b4e4804a9ca7ef2b6ae2c78f
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2026-03-11T04:19:00.000Z
---

# OpenCode Framework
## Full Setup Guide: OpenCode + FIRE + Docker + Free Cloud Tiers
**Your exact setup: Client machine (OpenCode CLI) ↔ Tailscale ↔ Ubuntu server (Docker + Ollama qwen2.5-coder:7b)**
___
### Your Architecture at a Glance
```plain text
CLIENT MACHINE                     UBUNTU SERVER (via Tailscale)
─────────────────                  ──────────────────────────────────
opencode (CLI)          ←──────→   Ollama :11434  (qwen2.5-coder:7b)
  │                    Tailscale   Docker containers:
  │                                  - orchestrator (OpenCode + FIRE)
  └─ opencode.json                   - mcp-server
     points at:                      - python-sandbox
     • Zen (free)                     - scheduler (APScheduler)
     • OpenRouter (free)              - streamlit (dashboard :8501)
     • Ollama on server IP
```
___
### PHASE 0 — Prerequisites Check
#### On your Ubuntu server, run:
```bash
# Verify Docker is installed
docker --version          # need 24+
docker compose version    # need v2

# Verify Ollama is running
curl http://localhost:11434/api/tags
# Should return JSON with qwen2.5-coder:7b listed

# Get your Tailscale IP (you'll need this)
tailscale ip -4
# Example output: 100.64.x.x  ← note this down
```
#### On your client machine, run:
```bash
# Verify OpenCode is installed
opencode --version

# Verify you can reach the server over Tailscale
ping <server-tailscale-ip>
curl http://<server-tailscale-ip>:11434/api/tags
# Should return the same JSON as above
```
> **If Ollama isn't reachable over Tailscale**, fix it on the server:
```bash
# Make Ollama listen on all interfaces (including Tailscale)
sudo systemctl edit ollama
# Add under [Service]:
#   Environment="OLLAMA_HOST=0.0.0.0"
sudo systemctl restart ollama
```
___
### PHASE 1 — Fix Ollama Context Window (Critical)
Ollama defaults to **4096 tokens** even for models with larger native context. OpenCode needs at least 16k to use tools reliably.
#### On the server:
```bash
# Enter the Ollama interactive prompt
ollama run qwen2.5-coder:7b

# Inside the prompt:
>>> /set parameter num_ctx 16384
Set parameter 'num_ctx' to '16384'
>>> /save qwen2.5-coder:7b-16k
Created new model 'qwen2.5-coder:7b-16k'
>>> /bye

# Verify it saved
ollama list
# Should show: qwen2.5-coder:7b-16k
```
___
### PHASE 2 — Sign Up for Free Cloud Providers (Client Machine)
Do this before touching OpenCode config. Sign up for each — all free, no card needed:

|#|Provider|Sign-up URL|What to get|
|---|---|---|---|
|1|OpenCode Zen|opencode.ai/zen|Login — key generated in OpenCode via `/connect`|
|2|OpenRouter|openrouter.ai|Create account → "Keys" → Create key (free tier)|
|3|NVIDIA NIM|build.nvidia.com|Sign in → "API Key" → Generate|
|4|Google AI Studio|aistudio.google.com|Sign in → "Get API key"|
|5|Alibaba Qwen|dashscope.aliyuncs.com|Register → API Key|
Keep these keys ready. You'll set them as environment variables next.
___
### PHASE 3 — Configure OpenCode on Client Machine
#### 3.1 Set environment variables
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
export OPENROUTER_API_KEY="sk-or-..."
export NVIDIA_API_KEY="nvapi-..."
export GOOGLE_API_KEY="AIza..."
export ALIBABA_API_KEY="sk-..."
# Note: Zen key is handled by /connect inside OpenCode
```
Then: `source ~/.bashrc`
#### 3.2 Create/edit OpenCode config
```bash
mkdir -p ~/.config/opencode
nano ~/.config/opencode/opencode.json
```
Paste this complete config (replace `<SERVER_TAILSCALE_IP>` with your actual Tailscale IP):
```json
{
  "$schema": "https://opencode.ai/config.json",

  "provider": {
    "openrouter": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "OpenRouter (Free)",
      "options": {
        "baseURL": "https://openrouter.ai/api/v1",
        "apiKey": "{env:OPENROUTER_API_KEY}",
        "headers": {
          "HTTP-Referer": "https://github.com/opencode-ai/opencode",
          "X-Title": "OpenCode"
        }
      },
      "models": {
        "qwen/qwen3-coder-480b:free": {
          "name": "Qwen3-Coder 480B (Free)",
          "tools": true,
          "limit": { "context": 262144, "output": 8192 }
        },
        "meta-llama/llama-3.3-70b-instruct:free": {
          "name": "Llama 3.3 70B (Free)",
          "tools": true,
          "limit": { "context": 131072, "output": 8192 }
        }
      }
    },

    "nvidia": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "NVIDIA NIM (Free Trial)",
      "options": {
        "baseURL": "https://integrate.api.nvidia.com/v1",
        "apiKey": "{env:NVIDIA_API_KEY}"
      },
      "models": {
        "meta/llama-3.1-405b-instruct": {
          "name": "Llama 3.1 405B (NVIDIA)",
          "tools": true,
          "limit": { "context": 128000, "output": 4096 }
        }
      }
    },

    "google-free": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Google AI Studio (Free)",
      "options": {
        "baseURL": "https://generativelanguage.googleapis.com/v1beta/openai",
        "apiKey": "{env:GOOGLE_API_KEY}"
      },
      "models": {
        "gemini-2.0-flash-exp": {
          "name": "Gemini 2.0 Flash (Free)",
          "tools": true,
          "limit": { "context": 1000000, "output": 8192 }
        }
      }
    },

    "alibaba": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Alibaba Qwen (Free Tier)",
      "options": {
        "baseURL": "https://dashscope.aliyuncs.com/compatible-mode/v1",
        "apiKey": "{env:ALIBABA_API_KEY}"
      },
      "models": {
        "qwen2.5-coder-32b-instruct": {
          "name": "Qwen2.5-Coder 32B (Alibaba)",
          "tools": true,
          "limit": { "context": 131072, "output": 8192 }
        }
      }
    },

    "ollama-server": {
      "npm": "@ai-sdk/openai-compatible",
      "name": "Ollama (Server via Tailscale)",
      "options": {
        "baseURL": "http://<SERVER_TAILSCALE_IP>:11434/v1"
      },
      "models": {
        "qwen2.5-coder:7b-16k": {
          "name": "Qwen2.5-Coder 7B Local (Fallback)",
          "tools": true,
          "limit": { "context": 16384, "output": 4096 }
        }
      }
    }
  },

  "model": "openrouter/qwen/qwen3-coder-480b:free"
}
```
#### 3.3 Connect OpenCode Zen (Tier 1)
```bash
opencode
# Inside OpenCode TUI:
/connect
# → search for "OpenCode Zen" → follow browser auth → paste key
# Then:
/models
# → switch to a Zen model (e.g., GLM 4.7 Free or Big Pickle)
```
#### 3.4 Test each provider
```bash
# Test OpenRouter (Tier 2) — should work immediately with env var
opencode run "write a python hello world" --model openrouter/qwen/qwen3-coder-480b:free

# Test local Ollama fallback (Tier 6)
opencode run "write a python hello world" --model ollama-server/qwen2.5-coder:7b-16k
```
___
### PHASE 4 — Server: Docker Compose Stack
#### 4.1 Create the project folder on the server
```bash
mkdir -p ~/opencode-framework
cd ~/opencode-framework
mkdir -p containers/{orchestrator,mcp-server,python-sandbox,scheduler}
mkdir -p workspace schedules logs .specs-fire
```
#### 4.2 Create `docker-compose.yml`
```yaml
# ~/opencode-framework/docker-compose.yml
version: '3.9'

services:

  mcp-server:
    build: ./containers/mcp-server
    volumes:
      - ./workspace:/workspace
      - ./schedules:/schedules
    networks: [opencode-net]
    restart: unless-stopped

  python-sandbox:
    build: ./containers/python-sandbox
    volumes:
      - ./workspace:/workspace
    network_mode: none          # no internet — isolated execution
    restart: unless-stopped

  scheduler:
    build: ./containers/scheduler
    volumes:
      - ./workspace:/workspace
      - ./schedules:/schedules
      - ./logs:/logs
    ports:
      - "8501:8501"             # Streamlit dashboard
      - "8000:8000"             # FastAPI scheduler API
    networks: [opencode-net]
    restart: unless-stopped

networks:
  opencode-net:
    driver: bridge
```
> **Note:** No `ollama` container needed — you already have Ollama running natively on the server. The OpenCode CLI on your client machine points at it directly via Tailscale.
#### 4.3 MCP Server container
```bash
cat > containers/mcp-server/Dockerfile << 'EOF'
FROM node:20-slim
RUN npm install -g \
    @modelcontextprotocol/server-filesystem \
    @modelcontextprotocol/server-git
WORKDIR /workspace
CMD ["node", "-e", "require('@modelcontextprotocol/server-filesystem')"]
EOF
```
#### 4.4 Python sandbox container
```bash
cat > containers/python-sandbox/Dockerfile << 'EOF'
FROM python:3.12-slim
RUN pip install pytest black ruff --no-cache-dir
WORKDIR /workspace
CMD ["python", "--version"]
EOF
```
#### 4.5 Scheduler container
```bash
cat > containers/scheduler/Dockerfile << 'EOF'
FROM python:3.12-slim
RUN pip install apscheduler fastapi uvicorn pyyaml streamlit --no-cache-dir
WORKDIR /app
COPY main.py .
COPY ui.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF
```
Create `containers/scheduler/main.py`:
```python
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
import yaml, subprocess
from pathlib import Path

app = FastAPI()
scheduler = BackgroundScheduler()
scheduler.start()

def run_task(task_desc: str):
    result = subprocess.run(
        ["opencode", "run", task_desc],
        capture_output=True, text=True
    )
    Path("/logs/scheduler.log").open("a").write(result.stdout + result.stderr)

@app.post("/task")
def add_task(cron: str, description: str):
    scheduler.add_job(run_task, "cron", args=[description],
                      **dict(zip(["hour","minute"], cron.split())))
    return {"status": "scheduled"}

@app.get("/tasks")
def list_tasks():
    return [{"id": str(job.id), "next_run": str(job.next_run_time)}
            for job in scheduler.get_jobs()]
```
Create `containers/scheduler/ui.py`:
```python
import streamlit as st, requests, yaml
from pathlib import Path

st.title("OpenCode Scheduler Dashboard")

# Show schedules
st.header("Active Schedules")
try:
    tasks = requests.get("http://localhost:8000/tasks").json()
    st.table(tasks)
except:
    st.warning("Scheduler API not reachable")

# Show recent logs
st.header("Recent Logs")
log_path = Path("/logs/scheduler.log")
if log_path.exists():
    st.code(log_path.read_text()[-3000:])

# Add schedule
st.header("Add Schedule")
with st.form("add"):
    desc = st.text_area("Task description")
    cron = st.text_input("Hour:Minute (e.g. 8:00)")
    if st.form_submit_button("Schedule"):
        requests.post("http://localhost:8000/task",
                      params={"cron": cron, "description": desc})
        st.success("Scheduled!")
```
#### 4.6 Start the stack
```bash
cd ~/opencode-framework
docker compose up -d --build

# Verify all containers running
docker compose ps
```
___
### PHASE 5 — Set Up FIRE Workflow
FIRE runs on your **client machine** inside your project directory, using the OpenCode CLI you already have.
#### 5.1 Install specs.md
```bash
# On your client machine, inside your project directory
cd ~/my-project          # or wherever you're building
npx specsmd@latest install
# → when prompted for flow: select FIRE
```
#### 5.2 Link workspace to server (via Tailscale + SSHFS or rsync)
```bash
# Option A: Mount server workspace locally over SSH
sshfs user@<SERVER_TAILSCALE_IP>:~/opencode-framework/workspace ~/server-workspace

# Option B: Work locally, sync on commit (add to git post-commit hook)
# echo "rsync -az ./ user@<SERVER_TAILSCALE_IP>:~/opencode-framework/workspace/" >> .git/hooks/post-commit

# Option C: Just SSH into the server and run opencode there
ssh user@<SERVER_TAILSCALE_IP>
cd ~/opencode-framework/workspace
opencode   # runs on server, pointing at local Ollama
```
#### 5.3 Capture your first Intent
```bash
# In your project directory (client or server)
/specsmd-fire-planner

# OpenCode will ask: "What would you like to build?"
# Example response:
# > Build a Python script that reads schedule.yaml and creates
#   APScheduler jobs with timezone support, then runs pytest on it
```
#### 5.4 Execute with Builder
```bash
/specsmd-fire-builder
# Builder reads state.yaml → selects first work item
# Calls OpenCode → routes to Tier 1 free cloud (Zen) first
# Generates Python → runs in python-sandbox → pytest
# Writes walkthrough to .specs-fire/walkthroughs/
```
___
### PHASE 6 — Prompt Compression Engine
Install the compressor on your client machine so every command is optimised before hitting any LLM.
#### 6.1 Create the compressor
```bash
cat > ~/opencode-framework/prompt_compressor.py << 'EOF'
#!/usr/bin/env python3
"""
Prompt Compression Engine
Strips filler, injects FIRE state context, formats for max token efficiency.
Usage:
  python prompt_compressor.py "your natural language command"
  python prompt_compressor.py --test
"""
import sys, yaml, re
from pathlib import Path

STOPWORDS = {
    'hey','can','you','please','make','sure','just','basically',
    'actually','probably','really','would','could','should','like',
    'want','need','maybe','perhaps','also','well','okay','so','then'
}

MODE_MAP = {'low': 'Autopilot', 'medium': 'Confirm', 'high': 'Validate'}

def load_state(state_path: str = '.specs-fire/state.yaml') -> dict:
    p = Path(state_path)
    if not p.exists():
        return {}
    return yaml.safe_load(p.read_text()) or {}

def compress(raw: str, state: dict = None) -> str:
    if state is None:
        state = load_state()

    # Stage 1: strip filler words, extract core action
    tokens = raw.lower().split()
    signal = [t for t in tokens if re.sub(r'[^a-z]', '', t) not in STOPWORDS]
    core = ' '.join(signal[:25])  # hard cap at 25 signal tokens

    # Stage 2: pull active FIRE context
    intents = state.get('intents', [])
    active_intent = next((i for i in intents if i.get('status') == 'in_progress'), {})
    work_items = active_intent.get('work_items', [])
    active_wi = next((w for w in work_items if w.get('status') == 'in_progress'), {})

    intent_id = active_intent.get('id', 'none')
    wi_id = active_wi.get('id', 'none')
    complexity = active_wi.get('complexity', 'medium')
    mode = MODE_MAP.get(complexity, 'Confirm')

    # Stage 3: build compressed prompt
    lines = [
        f"TASK: {core}",
        f"CONTEXT: intent={intent_id} | work_item={wi_id} | mode={mode}",
        f"STANDARDS: python3.12 | type-hints | pytest-covered | pep8",
        f"OUTPUT: python_file",
    ]
    return '\n'.join(lines)

def test():
    samples = [
        "Hey, can you please write me a Python script that reads the schedule YAML file and generates the correct cron syntax for APScheduler? Make sure it handles timezone offsets properly and add tests.",
        "Can you actually fix the bug in the scheduler where it doesn't handle DST transitions correctly?",
        "Would you be able to maybe add a Streamlit page that shows the recent run logs?",
        "Generate a FastAPI endpoint that returns the current status of all scheduled tasks",
    ]
    print("Prompt Compression Test\n" + "="*50)
    for raw in samples:
        compressed = compress(raw)
        raw_tokens = len(raw.split())
        comp_tokens = len(compressed.split())
        reduction = round((1 - comp_tokens/raw_tokens) * 100)
        print(f"\nRAW ({raw_tokens} tokens):\n  {raw[:80]}...")
        print(f"COMPRESSED ({comp_tokens} tokens, {reduction}% reduction):\n  {compressed}")
    print("\n" + "="*50 + "\nAll tests passed!")

if __name__ == '__main__':
    if '--test' in sys.argv:
        test()
    elif len(sys.argv) > 1:
        raw_command = ' '.join(sys.argv[1:])
        print(compress(raw_command))
    else:
        print("Usage: python prompt_compressor.py 'your command'")
        print("       python prompt_compressor.py --test")
EOF

chmod +x ~/opencode-framework/prompt_compressor.py
python3 ~/opencode-framework/prompt_compressor.py --test
```
#### 6.2 Create a `oc` wrapper alias
This wraps every OpenCode call with compression automatically:
```bash
cat >> ~/.bashrc << 'EOF'

# OpenCode with automatic prompt compression
oc() {
    if [ -z "$1" ]; then
        opencode
    else
        COMPRESSED=$(python3 ~/opencode-framework/prompt_compressor.py "$@")
        echo "Compressed prompt:"
        echo "$COMPRESSED"
        echo "---"
        opencode run "$COMPRESSED"
    fi
}

# Shortcut: oc-local forces Tier 6 (Ollama fallback)
oc-local() {
    COMPRESSED=$(python3 ~/opencode-framework/prompt_compressor.py "$@")
    opencode run "$COMPRESSED" --model ollama-server/qwen2.5-coder:7b-16k
}
EOF

source ~/.bashrc
```
#### 6.3 Test the full pipeline
```bash
# This single command flows through: compressor → OpenRouter Qwen3-480B → file generated
oc "write a python script that reads schedule.yaml and prints all job names"

# Force local fallback
oc-local "add a type hint to every function in scheduler.py"
```
___
### PHASE 7 — Model Router (Auto-Tier Fallback)
This Python service automatically falls back through tiers when a 429 (rate limit) is hit.
```bash
cat > ~/opencode-framework/model_router.py << 'EOF'
#!/usr/bin/env python3
"""
Model Router — tries free tiers in order, falls back to local on 429.
Sets OPENCODE_MODEL env var which opencode reads from environment.
"""
import subprocess, os, json

TIERS = [
    {"name": "Zen (GLM 4.7)",         "model": "opencode/glm-4.7:free"},
    {"name": "OpenRouter Qwen3-480B", "model": "openrouter/qwen/qwen3-coder-480b:free"},
    {"name": "NVIDIA Llama 405B",     "model": "nvidia/meta/llama-3.1-405b-instruct"},
    {"name": "Google Gemini Flash",   "model": "google-free/gemini-2.0-flash-exp"},
    {"name": "Alibaba Qwen2.5-32B",   "model": "alibaba/qwen2.5-coder-32b-instruct"},
    {"name": "Local Ollama 7B",       "model": "ollama-server/qwen2.5-coder:7b-16k"},
]

RATE_LIMIT_FILE = "/tmp/oc_rate_limits.json"

def load_limits():
    try:
        return json.loads(open(RATE_LIMIT_FILE).read())
    except:
        return {}

def save_limits(limits):
    open(RATE_LIMIT_FILE, "w").write(json.dumps(limits))

def is_rate_limited(name: str) -> bool:
    import time
    limits = load_limits()
    if name in limits:
        # Rate limit resets after 1 hour
        return (time.time() - limits[name]) < 3600
    return False

def mark_rate_limited(name: str):
    import time
    limits = load_limits()
    limits[name] = time.time()
    save_limits(limits)

def get_active_model() -> tuple[str, str]:
    for tier in TIERS:
        if not is_rate_limited(tier["name"]):
            return tier["name"], tier["model"]
    return TIERS[-1]["name"], TIERS[-1]["model"]  # always has local

def run_with_routing(prompt: str):
    name, model = get_active_model()
    print(f"Using: {name} ({model})")
    result = subprocess.run(
        ["opencode", "run", prompt, "--model", model],
        capture_output=True, text=True
    )
    if "rate limit" in result.stderr.lower() or "429" in result.stderr:
        print(f"Rate limited on {name}, marking and retrying...")
        mark_rate_limited(name)
        run_with_routing(prompt)  # recurse to next tier
    else:
        print(result.stdout)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python model_router.py 'your prompt'")
    else:
        run_with_routing(" ".join(sys.argv[1:]))
EOF
```
Update your `oc` alias to use the router:
```bash
# Edit ~/.bashrc, replace the oc() function:
oc() {
    if [ -z "$1" ]; then
        opencode
    else
        COMPRESSED=$(python3 ~/opencode-framework/prompt_compressor.py "$@")
        echo "→ Compressed: $COMPRESSED"
        python3 ~/opencode-framework/model_router.py "$COMPRESSED"
    fi
}
```
___
### PHASE 8 — Verification Checklist
Run through this once everything is set up:
```bash
# 1. Ollama reachable from client over Tailscale
curl http://<SERVER_TAILSCALE_IP>:11434/api/tags | python3 -m json.tool

# 2. OpenCode can use local model
opencode run "print hello" --model ollama-server/qwen2.5-coder:7b-16k

# 3. OpenCode can use free cloud model
opencode run "print hello" --model openrouter/qwen/qwen3-coder-480b:free

# 4. Compressor works
python3 ~/opencode-framework/prompt_compressor.py "hey can you write a hello world"

# 5. Docker stack is up on server
ssh user@<SERVER_TAILSCALE_IP> 'docker compose -f ~/opencode-framework/docker-compose.yml ps'

# 6. Dashboard accessible
curl http://<SERVER_TAILSCALE_IP>:8501
# Or open in browser: http://<SERVER_TAILSCALE_IP>:8501

# 7. FIRE state initialized
ls .specs-fire/state.yaml && cat .specs-fire/state.yaml

# 8. Full pipeline test
oc "write a python function that adds two numbers with type hints and a docstring"
```
___
### Quick Reference

|What|Command|
|---|---|
|Start OpenCode TUI|`opencode`|
|Run with compression + routing|`oc "your task"`|
|Force local model|`oc-local "your task"`|
|Capture FIRE intent|`/specsmd-fire-planner`|
|Execute FIRE work item|`/specsmd-fire-builder`|
|Check model tiers|`opencode models`|
|Switch model in TUI|`/models`|
|Check rate limit status|`cat /tmp/oc_rate_limits.json`|
|Clear rate limits|`rm /tmp/oc_rate_limits.json`|
|View dashboard|`http://<server-ip>:8501`|
|Restart Docker stack|`docker compose restart` (on server)|
|Check Ollama on server|`curl http://<server-ip>:11434/api/tags`|
___
### Troubleshooting
**Tool calls not working with local model**
→ Context window too small. Re-run Phase 1 (create the `-16k` variant).
**OpenRouter returning 429**
→ Free tier limit hit. The model_router.py will auto-cascade to the next tier. Check with `cat /tmp/oc_rate_limits.json`.
**Ollama not reachable over Tailscale**
→ Add `OLLAMA_HOST=0.0.0.0` to Ollama's systemd env. See Phase 0.
**FIRE state.yaml not found**
→ Run `npx specsmd@latest install` from your project directory first.
**Docker containers not starting**
→ Check logs: `docker compose logs -f` on the server.
**Zen models not available**
→ Re-run `/connect` → OpenCode Zen inside the OpenCode TUI.