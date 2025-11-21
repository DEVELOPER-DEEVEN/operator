# Intercept: Autonomous Windows Agent

Intercept is an enterprise-grade autonomous agent designed to control Windows environments using natural language prompts. It leverages **Google Gemini 1.5 Pro** for multimodal reasoning, **Cloud Spanner** for transactional state management, and **Firestore** for vector-based few-shot learning.

## 🚀 Tech Stack

- **Core AI**: Google Gemini 1.5 Pro (Multimodal Vision & Text)
- **Backend**: FastAPI (Python 3.10+)
- **Database (Transactional)**: Google Cloud Spanner
- **Database (Vector/NoSQL)**: Google Cloud Firestore
- **Client**: Python (PyAutoGUI, MSS, Requests)
- **Infrastructure**: Google Cloud Run (Dockerized)

## 🏗️ Architecture

The system follows a **Client-Server** architecture:

1.  **Client (`intercept/client`)**:
    *   Captures screen state using `mss`.
    *   Executes low-level OS actions (Click, Type, Scroll) via `pyautogui`.
    *   Maintains a "Switch Control" listener for accessibility inputs.
2.  **Server (`intercept/server`)**:
    *   **API Layer**: FastAPI endpoints handling multipart image uploads.
    *   **Guardrails**: `GuardrailService` sanitizes inputs (PII redaction) and blocks dangerous commands (`rm -rf`).
    *   **Reasoning Engine**: Gemini 1.5 Pro analyzes the screen + prompt to generate the next action.
    *   **Memory**:
        *   *Short-term*: Session history in Firestore.
        *   *Long-term*: Vector similarity search in Firestore for "few-shot" example retrieval.
    *   **Audit**: All actions are transactionally logged to Cloud Spanner.

## 🛠️ Configuration

### Prerequisites
- **Python 3.10+**
- **Google Cloud Project** with the following APIs enabled:
    - Gemini API (Generative Language)
    - Cloud Spanner API
    - Firestore API

### Environment Variables

| Variable | Description | Default |
| :--- | :--- | :--- |
| `GOOGLE_API_KEY` | API Key for Gemini 1.5 Pro | Required |
| `GOOGLE_CLOUD_PROJECT` | GCP Project ID for Spanner/Firestore | Required |
| `INTERCEPT_SERVER_URL` | URL of the deployed server | `https://...run.app` |

## 📦 Installation & Usage

### 1. Server (Local Dev)

```bash
# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn intercept.server.main:app --reload --host 0.0.0.0 --port 8000
```

### 2. Client (Agent)

```bash
# Run the agent
python -m intercept.client.agent "open chrome and search for shoes on amazon"
```

## 🛡️ Security & Safety

- **Context Guardrails**: Automatically detects and blocks malicious commands before execution.
- **PII Redaction**: Sensitive data patterns (SSN, CC) are redacted from logs.
- **Human-in-the-loop**: The client runs locally, allowing the user to terminate the process (Fail-safe: Move mouse to corner).

## 🧪 Testing

Run the comprehensive test suite covering guardrails, API endpoints, and mock integrations:

```bash
pytest tests/
```
