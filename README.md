# Remote MCP Server (FastMCP) — Build, Test, Deploy & Connect

This project demonstrates how to build a **Remote MCP (Model Context Protocol) Server** using **FastMCP**, test it locally using the **MCP Inspector**, deploy it to the cloud, and optionally connect it to an AI host (like Claude Desktop) so the AI can call your tools remotely.

The goal of this repo is to showcase an **end-to-end MCP server workflow** that is production-friendly enough to demonstrate to recruiters: **tool design, HTTP transport, debugging, deployment, and integration**.

---

## Expense Tracker MCP Server (Remote + Local)

An **Expense Tracker MCP Server** that lets an AI host (like **Claude Desktop**) manage your expenses using **natural language**.  
You can add expenses, list them by date/month, and generate summaries—all by calling MCP **tools** over **Streamable HTTP** (remote) or **STDIO** (local).

---

$## ✨ What This Project Does

This project builds an **Expense Tracker MCP Server** that exposes structured capabilities to AI clients.

### ✅ MCP Server Capabilities

#### 1) Tools (Callable Actions)
Your AI host can call server functions like:
- `add_expense` → Add a new expense (amount, category, date, note)
- `list_expenses` → Fetch expenses for a date range / month
- `summarize_expenses` → Totals + breakdowns (month-wise / category-wise)

#### 2) Resources (Read-only Data)
The server also provides read-only endpoints like:
- `server_info` (metadata / server details)
- `categories` JSON resource for consistent **category + subcategory** selection

> Using a categories JSON resource ensures clean, consistent categorization across entries (no duplicate categories like “Transport” vs “Transportation”).

#### 3) Remote Hosting Support
- Uses **Streamable HTTP transport**, so you can deploy the server remotely and access it via a **Remote MCP URL**.

---

## 🧪 Local Development & Testing

You can validate your MCP server locally using:

✅ **FastMCP Dev / MCP Inspector**
- Confirms **capability discovery** (tools/resources show up correctly)
- Lets you run **tool calls** and verify outputs

Typical flow:
1. Start server in dev mode
2. Open MCP Inspector
3. Verify tools/resources
4. Run tool calls (add/list/summarize)

---

## 🌍 Deploy as a Remote MCP Server (Cloud)

### 1) Push Code to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main


---

## 🧱 Tech Stack

- **Python**
- **FastMCP**
- **uv** (project/dependency manager)
- **Git + GitHub**
- **FastMCP Cloud** (deployment)
- (Optional) **SQLite** for stateful apps like Expense Tracker

---

## 📌 Key Concepts / Topics Covered (Recruiter-Friendly)

### 1) MCP Lifecycle Understanding
- Initialization phase (protocol negotiation + capability setup)
- Operation phase (capability discovery + tool calls)
- Shutdown phase (transport-managed closure)

### 2) Capability Discovery
- How a client discovers available server capabilities:
  - `tools/list`
  - `resources/list`
  - `prompts/list` (if supported)
- How this enables dynamic tool selection by the host AI

### 3) Tool Calling (Core MCP Value)
- Defining server-side tools
- Passing structured arguments
- Returning structured results usable by AI agents

### 4) Resource Exposure
- Exposing static or dynamic data via `@mcp.resource`
- Example use-case: category mapping from a JSON file for consistent classification

### 5) Transport Layer (Local vs Remote)
- `stdio` transport for **local servers**
- `http` / **streamable HTTP** transport for **remote servers**
- Hosting server to make tools accessible across devices/users

### 6) Observability & Reliability (Special Cases)
- Ping requests (keep connection alive, detect dead peers)
- Error handling (JSON-RPC style error objects)
- Timeouts & cancellations
- Progress notifications for long-running operations

### 7) Deployment Workflow
- Source control with GitHub
- Deploy from repo using FastMCP Cloud
- Auto build & redeploy on new commits

---

## 🌍 Deploy as a Remote MCP Server (FastMCP Cloud)

### 1) Push code to GitHub
bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
---
### 2) Deploy on FastMCP Cloud
1) Log in to FastMCP Cloud
2) Select Deploy from your own code
3) Choose your GitHub repo + branch
4) Set the entry file to: main.py
5) Click Deploy

✅ After deployment, you’ll get a Remote MCP URL that can be used by clients/AI hosts.


### 3) Connect to Claude Desktop (Optional)
If your AI host supports custom remote connectors:
Open Claude Desktop -> Go to Settings → Connectors -> Click Add custom connector -> Paste your Remote MCP URL -> Restart Claude Desktop

Now Claude can directly call your server tools.
