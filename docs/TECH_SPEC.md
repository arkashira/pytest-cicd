# TECH_SPEC.md – pytest‑cicd  

**Project:** `pytest-cicd`  
**Owner:** Axentx – Automated testing solution for Python applications with integrated CI/CD and test‑automation capabilities  
**Status:** Ready for implementation (v0.1.0)  

---  

## 1. Overview  

`pytest‑cicd` is a **plug‑and‑play testing platform** that extends the popular `pytest` framework with first‑class CI/CD integration, rich reporting, and an optional web dashboard. It enables Python teams to:

* Run tests locally or in any CI environment with a single command.  
* Publish test results to a central result store (PostgreSQL) for historical analysis.  
* Generate CI‑native artifacts (JUnit XML, HTML, JSON) automatically.  
* Trigger downstream pipelines (e.g., deployment, performance testing) based on test outcomes via a lightweight REST API.  

The product is delivered as:

| Artifact | Description |
|----------|-------------|
| **pytest‑cicd core** | Python package (`pytest_cicd`) that provides a pytest plugin, CLI wrapper, and result‑export utilities. |
| **CI adapters** | Pre‑built configuration snippets for GitHub Actions, GitLab CI, Azure Pipelines, and Jenkins. |
| **Dashboard service** | Optional FastAPI‑based web UI + API for browsing test runs, trends, and flaky‑test detection. |
| **Docker images** | `axentx/pytest-cicd-runner` (runtime) and `axentx/pytest-cicd-dashboard` (service). |

---  

## 2. Architecture  

```
+-------------------+          +-------------------+          +-------------------+
|   Developer PC    |  pytest  |   pytest‑cicd    |  HTTP/   |   Dashboard      |
| (or CI runner)   |--------->|   Plugin + CLI   |--------->|   (FastAPI)      |
+-------------------+          +-------------------+          +-------------------+
          |                               |                         |
          |                               |                         |
          v                               v                         v
   +----------------+            +----------------+        +-------------------+
   |   Test Suite   |            |   Result Store |<-------|   PostgreSQL DB   |
   +----------------+            +----------------+        +-------------------+
          |                               |
          |                               |
          v                               v
   +----------------+            +----------------+
   |   Artifacts    |<-----------|   Exporter     |
   | (XML/HTML/JSON)|            +----------------+
   +----------------+
```

* **pytest‑cicd Plugin** – registers hooks (`pytest_configure`, `pytest_unconfigure`, `pytest_runtest_logreport`) to capture test metadata and push results to the result store.  
* **CLI Wrapper (`pytest-cicd run`)** – convenience entry point that sets up environment variables, selects the appropriate CI adapter, and invokes `pytest`.  
* **Result Store** – PostgreSQL schema (`runs`, `tests`, `artifacts`, `metadata`). Writes are performed via SQLAlchemy ORM.  
* **Exporter** – background worker (Celery) that converts raw DB rows into JUnit XML, HTML, and JSON files for CI artifact publishing.  
* **Dashboard** – FastAPI service exposing REST endpoints (`/runs`, `/tests`, `/trends`) and a React front‑end (served via `static/`).  
* **CI Adapters** – YAML snippets that install the package, configure DB credentials, and invoke the CLI.  

---  

## 3. Components  

| Component | Language / Runtime | Primary Responsibility | Public Interface |
|-----------|-------------------|------------------------|------------------|
| **pytest‑cicd core** | Python 3.10+ | pytest plugin, result collector, CLI | `pytest_cicd` package, `pytest-cicd run` CLI |
| **Result Store** | PostgreSQL 15 | Persistent storage of test runs & metadata | SQLAlchemy ORM models (`Run`, `TestCase`, `Artifact`) |
| **Exporter** | Python (Celery) | Asynchronously generate CI artifacts | Celery tasks (`export_junit`, `export_html`, `export_json`) |
| **Dashboard API** | FastAPI (Python) | Query & aggregate test data, auth, webhook triggers | REST (`/api/v1/...`) |
| **Dashboard UI** | React (TS) + Vite | Interactive web UI for test history & flaky detection | Browser (served at `/`) |
| **CI Adapters** | YAML (GitHub Actions, GitLab CI, etc.) | Boilerplate to install & run the tool in CI pipelines | CI‑specific configuration files |
| **Docker Images** | Docker (Alpine + Python) | Portable runtime for both runner & dashboard | `docker run axentx/pytest-cicd-runner …` |

---  

## 4. Data Model  

### 4.1 ER Diagram (simplified)

```
Run
 ├─ id (PK)
 ├─ commit_sha
 ├─ branch
 ├─ triggered_by (enum: push, pr, schedule, manual)
 ├─ start_ts
 ├─ end_ts
 ├─ status (enum: passed, failed, error
