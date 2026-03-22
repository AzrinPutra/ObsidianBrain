---
title: Complete Ollama + Open WebUI Setup & Troubleshooting Guide V2
path: "Complete Ollama + Open WebUI Setup & Troubleshooting Guide V2"
url: https://www.notion.so/Complete-Ollama-Open-WebUI-Setup-Troubleshooting-Guide-V2-30dbd926b4e48056b720ca3576caea71
created_by: Azrin Putra
last_edited_by: Azrin Putra
last_edited_time: 2026-02-20T15:26:00.000Z
---

# Complete Ollama + Open WebUI Setup & Troubleshooting Guide V2
This guide documents a **full, production-ready Ollama + Open WebUI setup** on Linux with GPU support, remote access via **Tailscale**, **custom models**, and **all troubleshooting steps**. It’s optimized for **self-hosted LLM deployments** and Notion copy/paste.
___
### 1. Target Architecture
```plain text
[ Remote Laptop ]
        │ (Tailscale)
        ▼
[ Open WebUI :8080 ] ──► [ Ollama :11434 ] ──► [ NVIDIA GPU ]
```
- Ollama runs **on host**
- Open WebUI runs **in Docker (host network)**
- GPU acceleration via **NVIDIA Container Toolkit**
- Remote access secured via **Tailscale**
___
### 2. System Requirements
#### OS
- Ubuntu / Debian-based Linux
#### Hardware
- NVIDIA GPU (tested: RTX 2060 6GB)
- ≥ 8GB RAM recommended
#### Software
- Docker
- NVIDIA driver installed (verify with `nvidia-smi`)
- Ollama installed on host
___
### 3. Install & Verify Ollama (Host)
```bash
curl -fsSL https://ollama.com/install.sh | sh
sudo systemctl enable ollama
sudo systemctl start ollama
ollama --version
```
#### Pull Base Models
```plain text
ollama pull mistral:7b
ollama pull qwen2.5-coder:7b
ollama pull llama3.1:8b
```
Verify:
```plain text
ollama list
```
___
### 4. Verify GPU Works (Critical)
```bash
nvidia-smi
docker run --rm --gpus all nvidia/cuda:12.2.0-runtime-ubuntu22.04 nvidia-smi
```
If this fails → **stop here**; Open WebUI needs GPU.
___
### 5. NVIDIA Container Toolkit Fix (Common)
```bash
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit.gpg
curl -fsSL https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
  | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit.gpg] https://#g' \
  | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
sudo apt update
sudo apt install -y nvidia-container-toolkit
sudo systemctl restart docker
```
___
### 6. Run Open WebUI
```bash
docker rm -f open-webui
docker run -d --network host --gpus all \
  --name open-webui \
  -e OLLAMA_BASE_URL=http://127.0.0.1:11434 \
  ghcr.io/open-webui/open-webui:main
```
Access via browser:
```plain text
http://<TAILSCALE_IP>:8080
```
___
### 7. Troubleshooting Common Errors
#### 500 Internal Server Error
- Open WebUI **requires authentication**
- Browser login or API token required
- Curl API without token → `{"detail":"Not authenticated"}`
#### Fix Option 1: Browser
- Open WebUI via browser (Tailscale)
- Register & log in
- ✅ Works, no 500, session cookie auto-attached
#### Fix Option 3: API Token
- Login via API, extract token
- Use in header: `Authorization: Bearer <token>`
___
### 8. Custom Models & Aliases (New Phase)
#### Core Concept
> **Modelfile = recipe → model = product → model name = what you call**
- You **never run a base model directly** for a specific task
- Create **custom models** from Modelfiles
- Assign **aliases** if desired
___
#### Step 1 — Create Modelfiles
#### SOC Analyst (`Modelfile.soc`)
```plain text
FROM llama3.1:8b
SYSTEM You are a SOC analyst assistant.
Analyze logs, alerts, and security events clearly and concisely.
```
#### Bash Tutor (`Modelfile.bash`)
```plain text
FROM llama3.1:8b
SYSTEM You are a Bash scripting tutor.
Explain commands, scripts, and troubleshooting.
```
#### Python Tutor (`Modelfile.python`)
```plain text
FROM llama3.1:8b
SYSTEM You are a Python programming tutor.
Provide examples, explain syntax, and best practices.
```
#### Logs Analyzer (`Modelfile.logs`)
```plain text
FROM mistral:7b
SYSTEM You are a log analysis assistant.
Aggregate, summarize, and detect anomalies in logs.
```
> Optional: Save all Modelfiles in `~/Modelfiles/`
___
#### Step 2 — Create Models
```bash
ollama create soc-f ~/Modelfiles/Modelfile.soc
ollama create bash-f ~/Modelfiles/Modelfile.bash
ollama create python-f ~/Modelfiles/Modelfile.python
ollama create logs-f ~/Modelfiles/Modelfile.logs
```
Verify:
```plain text
ollama list
```
Expected:
```plain text
soc
bash
python
logs
llama3.1:8b
mistral:7b
qwen2.5-coder:7b
```
___
#### Step 3 — Run Models
```bash
ollama run soc "Analyze this firewall log"
ollama run bash "Explain: for i in {1..5}; do echo $i; done"
ollama run python "Write a Python function to parse JSON logs"
ollama run logs "Summarize failed SSH login attempts"
```
___
#### Step 4 — Assign Aliases (Optional)
- Allows quick reference in scripts or UI
```plain text
ollama alias soc analyst
ollama alias bash shell
ollama alias python py
ollama alias logs logparser
```
Now you can:
```plain text
ollama run analyst "Check IDS alert"
ollama run py "Explain list comprehension"
```
___
#### Step 5 — Temperature & Context Tuning

|Model|Task|Temperature|Context Length (num_ctx)|Notes|
|---|---|---|---|---|
|soc|SOC analysis|0.3|4096|Conservative, avoid hallucination|
|bash|Bash learning|0.5|2048|Medium creativity for examples|
|python|Python tutor|0.5|2048|Medium creativity for examples|
|logs|Log analysis|0.2|4096|Deterministic summarization|
Set globally in `~/.ollama/config.yaml`:
```yaml
num_gpu_layers: 20
num_ctx: 4096
temperature: 0.3   # default, overridden per model if needed
```
___
### 9. API Access for Custom Models
#### Example (with token)
```plain text
TOKEN=<your_api_token>
curl http://127.0.0.1:11434/api/generate-H"Authorization: Bearer$TOKEN"-d'{
  "model": "soc",
  "prompt": "Analyze this IDS alert"
}'
```
___
### 10. Daily Workflow with Custom Models
1. Connect via Tailscale
2. Open WebUI
3. Select model: `soc`, `bash`, `python`, `logs`
4. Start chat with task-specific prompts
5. Optional: run automation scripts via API token
___
### 11. Troubleshooting & Debugging
#### Ollama Logs
```plain text
journalctl-u ollama-f
```
Check:
- GPU detected
- Models listed
- `/v1/models` works
#### Open WebUI Logs
```plain text
docker logs-f open-webui
```
Check for:
- Auth errors
- Model loading success
___
This now **completely integrates custom models, aliases, ready-made Modelfiles, and tuning**, making your Notion guide fully self-contained and production-ready.
___
If you want, I can also **add a Phase 12 “Example Prompts Library”** for your first 2–3 weeks focusing on Bash and Python, with ready-made practice prompts for rapid learning.
Do you want me to add that next?
yes
Perfect — I’ll create **Phase 12: Example Prompts Library** tailored for your **first 2–3 weeks** of learning Bash and Python. This will be Notion-ready, structured, and aligned with your custom model setup.
___
### **Phase 12 — Example Prompts Library (Bash & Python, Weeks 1–3)**
> These prompts are designed for hands-on practice with your **bash** and **python** custom models. Use in **Open WebUI** or via `ollama run bash` / `ollama run python`.
___
#### **Week 1 — Bash Fundamentals**

|Day|Prompt|Task|
|---|---|---|
|Mon|`Explain: ls -la /home`|Learn file listing flags|
|Tue|`Write a bash script to count number of files in /tmp`|Looping & counting|
|Wed|`Explain: for i in {1..5}; do echo $i; done`|Loop basics|
|Thu|`Write a script to delete log files older than 7 days in /var/log`|File find & cleanup|
|Fri|`Show how to redirect stdout and stderr to different files`|I/O redirection|
|Sat|`Explain: grep "Failed password" /var/log/auth.log|awk '{print $11}'|
|Sun|`Write a bash script to backup /etc to /tmp/etc_backup.tar.gz`|Archiving & scripting|
**Usage Example:**
```plain text
ollama runbash"Write a bash script to delete log files older than 7 days in /var/log"
```
___
#### **Week 2 — Bash Intermediate**

|Day|Prompt|Task|
|---|---|---|
|Mon|`Write a script to monitor CPU usage and alert if >80%`|Conditionals & monitoring|
|Tue|`Explain how 'sed' works for replacing text in a file`|Text manipulation|
|Wed|`Write a bash script to parse auth.log and list failed SSH login IPs`|Log parsing|
|Thu|`Explain the difference between $* and $@ in scripts`|Parameter handling|
|Fri|`Write a function in bash to check if a process is running`|Functions & process check|
|Sat|`Write a script to rotate logs weekly`|Automation|
|Sun|`Explain how cron jobs work and provide example to run backup daily`|Scheduling|
___
#### **Week 3 — Python Fundamentals & Scripting**

|Day|Prompt|Task|
|---|---|---|
|Mon|`Write a Python script to read cowrie.json and count failed logins`|JSON parsing|
|Tue|`Explain Python list comprehension with examples`|Python basics|
|Wed|`Write a Python function to extract IPs from log lines`|String & regex|
|Thu|`Write a Python script to summarize log counts per user`|Aggregation|
|Fri|`Explain difference between dict.get() and dict[]`|Dictionaries|
|Sat|`Write a Python script to read multiple JSON log files and merge them`|File handling|
|Sun|`Write a Python function to alert if failed logins > 10 per IP`|Conditional logic|
**Usage Example:**
```plain text
ollama run python"Write a Python script to read cowrie.json and count failed logins"
```
___
#### **Tips for Using Prompts**
6. **Start Small**: Break tasks into micro-prompts (`Explain X`, then `Write script for X`)
7. **Temperature Setting**:
	- Bash: 0.5 → flexible examples
	- Python: 0.5 → clear code generation
8. **Context / num_ctx**: 2048 is sufficient for small scripts; increase for multi-file or complex logs
9. **Model Switching**: Use aliases if you created them:
```plain text
ollama run shell "Prompt here"
ollama run py "Prompt here"
```
10. **Iterate & Refactor**: Ask model to improve or optimize scripts after generation
___
#### ✅ Pro Practice Flow
11. Run **daily prompt** in Open WebUI using `bash` or `python` model
12. Copy generated script, test on local VM or container
13. Make small edits → re-run prompt asking for **optimization / explanation**
14. Save useful snippets in a **personal snippet library**