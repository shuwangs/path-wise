"""Local configuration shared by the API and migrations."""
import os
from pathlib import Path

from dotenv import load_dotenv

# Shell variables take precedence over the local, untracked configuration.
load_dotenv(Path(__file__).resolve().parents[1] / ".env", override=False)

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://pathwise:pathwise_local@127.0.0.1:5433/pathwise",
)
