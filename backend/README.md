# Backend

FastAPI application with a process health endpoint. Requires Python 3.10+.

From the repository root (macOS / Linux):

```sh
cd backend
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

For subsequent starts, activate the existing virtual environment and run Uvicorn. Press Ctrl+C to stop; run `deactivate` to leave the environment.

API documentation: http://127.0.0.1:8000/docs.

```sh
curl http://127.0.0.1:8000/health
```

Expected response: `{"status":"ok","service":"pathwise-api"}`. This checks process health only, without checking a database or external sources.

Run tests from the backend directory with the virtual environment activated:

```sh
python -m pip install -r requirements-dev.txt
python -m pytest
```

Default CORS configuration permits localhost and 127.0.0.1 on ports 3000 and 3001. No override is needed for normal development. Optional `CORS_ORIGINS` replaces the default list and must match the frontend's scheme, hostname, and port exactly. `.env.example` is a reference; the application does not load it automatically.

The verified dependency snapshot in `requirements.lock.txt` includes development dependencies for Python 3.13 / macOS.
