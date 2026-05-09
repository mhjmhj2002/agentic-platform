# 🚀 Agentic Platform Roadmap

## 📌 Vision

Agentic Platform is an experimental AI Software Engineering Platform focused on automating the software development lifecycle using AI agents.

The platform aims to orchestrate:

- GitHub issue ingestion
- Project context understanding
- AI-based technical planning
- Human approval workflows
- Autonomous code generation
- Pull Request automation
- Multi-repository engineering orchestration

The long-term goal is to create an internal AI Engineering Assistant capable of supporting real enterprise software development workflows.

---

# 🧠 Core Concept

The platform follows an Agentic SDLC approach:

```text
GitHub Issue
    ↓
Webhook Event
    ↓
Event Normalization
    ↓
Project Context Analysis
    ↓
AI Technical Planning
    ↓
Human Approval
    ↓
Code Generation
    ↓
Pull Request Creation
```

---

# ✅ Completed Steps

## 1. Project Foundation

- FastAPI application created
- Modular architecture defined
- Virtual environment configured
- Logging system implemented
- OpenAPI/Swagger enabled

---

## 2. GitHub Webhook Integration

Implemented:

- GitHub webhook endpoint
- Event normalization layer
- Issue opened event handling
- Event routing workflow

Current supported events:

- issues.opened

---

## 3. Workflow Engine

Implemented:

- Workflow router
- Issue workflow
- Event dispatcher
- Async orchestration

Current workflows:

| Workflow | Status |
|---|---|
| Issue Opened | ✅ |
| Comment Approval | ⏳ |
| PR Workflow | ⏳ |

---

## 4. Project Context Engine

Implemented:

- Repository scanner
- Stack detector
- Multi-project architecture support
- Spring Boot detection
- Maven detection
- Java version detection
- Dependency extraction

Current detected context:

- Language
- Framework
- Build tool
- Java version
- Dependencies
- Source directories

---

## 5. AI Planning Agent

Implemented:

- OpenAI integration
- Context-aware planning
- Technical implementation planning
- Structured JSON plan generation

Current capabilities:

- Generate technical development plans
- Understand Spring Boot projects
- Generate layered architecture plans
- Suggest validation/testing/documentation steps

---

## 6. Multi-Repository Awareness

Implemented:

- Dynamic repository mapping
- Independent microservice analysis
- Repository-specific context generation

Current repositories:

- agentic-platform
- agentic-ms-user
- future microservices

---

## 7. Technical Documentation

Implemented:

- Complete README
- Setup documentation
- Architecture documentation
- Development roadmap

---

# 🚧 Current Sprint

## Goal

Generate professional technical development plans automatically from GitHub issues.

Expected output:

```text
docs/plans/issue-<id>-development-plan.md
```

This is the first major milestone intended for internal demonstration.

---

# 🔥 Next Steps

## 1. Markdown Development Plan Generator

Priority: HIGH

Create:

```text
app/skills/plan_markdown_generator.py
```

Responsibilities:

- Convert AI JSON plans into professional Markdown
- Generate developer-readable plans
- Include project context
- Include approval section

Expected output example:

```text
docs/plans/issue-1-development-plan.md
```

---

## 2. GitHub Comment Integration

Priority: HIGH

Features:

- Automatically comment generated plan on GitHub issue
- Add execution logs
- Add approval instructions

Example:

```text
Reply with:
- approve plan
- reject plan
```

---

## 3. Human Approval Workflow (HITL)

Priority: HIGH

States:

| State | Description |
|---|---|
| NEW | Issue received |
| PLANNING | AI generating plan |
| WAITING_APPROVAL | Waiting developer approval |
| APPROVED | Approved by developer |
| CODING | Generating code |
| OPENING_PR | Creating PR |
| DONE | Finished |
| FAILED | Error |

---

## 4. State Persistence

Priority: HIGH

Implement:

- State files
- Execution persistence
- Idempotent workflow protection
- Retry-safe execution

Suggested location:

```text
app/state/
```

---

## 5. Code Generation Agent

Priority: VERY HIGH

Initial low-risk tasks:

- Update pom.xml version
- Create README sections
- Create DTOs
- Create entities
- Create controllers

Future goals:

- Full CRUD generation
- Service generation
- Repository generation
- Validation generation
- Test generation

---

## 6. Git Automation

Priority: HIGH

Features:

- Branch creation
- Commit generation
- Push automation
- Pull Request creation

---

## 7. Retrieval-Augmented Context (RAG)

Priority: MEDIUM

Future goals:

- Architecture memory
- Historical implementation memory
- Repository knowledge indexing
- Similar issue retrieval

Potential technologies:

- pgvector
- ChromaDB
- Qdrant

---

## 8. Multi-Agent Architecture

Priority: MEDIUM

Future agents:

| Agent | Responsibility |
|---|---|
| Planning Agent | Generate technical plans |
| Coding Agent | Generate code |
| Review Agent | Validate code |
| Test Agent | Generate tests |
| Documentation Agent | Generate docs |
| PR Agent | Create PRs |

---

## 9. MCP Integration

Priority: MEDIUM

Future goals:

- MCP-compatible tools
- IDE integration
- External tool orchestration
- AI tool interoperability

---

## 10. Observability & Governance

Priority: MEDIUM

Future goals:

- Workflow tracing
- Execution metrics
- Token tracking
- Cost analysis
- Audit logs
- Prompt observability

---

# 🏗️ Current Architecture

```text
agentic-platform/
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── github/
│   ├── llm/
│   ├── memory/
│   ├── project_context/
│   ├── prompts/
│   ├── skills/
│   ├── state/
│   └── workflows/
│
├── docs/
├── docker/
├── tests/
└── docker-compose.yml
```

---

# 🎯 Short-Term Goal

Deliver a fully working demo with:

- GitHub Issue
- Automatic AI planning
- Technical Markdown generation
- Human approval flow

This milestone already represents a production-relevant AI engineering workflow.

---

# 🎯 Mid-Term Goal

Achieve autonomous PR generation for simple CRUD-based tasks.

---

# 🎯 Long-Term Goal

Build a complete AI Software Engineering Platform capable of orchestrating enterprise-grade software development workflows.

---

# ⚠️ Disclaimer

This project is experimental and focused on:

- AI Engineering
- Agentic SDLC
- Software automation
- Multi-agent orchestration
- Developer productivity
- Human-in-the-loop AI systems
