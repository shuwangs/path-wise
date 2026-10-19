# Local database

PathWise uses PostgreSQL 17, SQLAlchemy 2, psycopg 3, and Alembic.
Start Docker Desktop before running Compose.

## Start PostgreSQL

From the repository root:

```sh
docker compose up -d --wait db
docker compose ps
```

Compose binds PostgreSQL to `127.0.0.1:5433` and stores data in the named `postgres_data` volume. The development database and user are both `pathwise`; the password is `pathwise_local`. These are local development defaults.

## Configure and migrate

From the repository root:

```sh
cd backend
source .venv/bin/activate
python -m pip install -r requirements.txt
cp -n .env.example .env
python -m alembic upgrade head
python -m alembic current
```

If this is a fresh checkout, create the virtual environment first with `python3 -m venv .venv`.

The API and Alembic automatically load `backend/.env`; existing shell variables take precedence. The default `DATABASE_URL` matches Compose. Revision `0001` establishes the migration baseline and `alembic_version` tracking table; domain tables are not created yet. Future models should inherit from `app.database.Base` and be imported into the migration environment before autogeneration.

Start the backend normally:

```sh
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

From another terminal:

```sh
curl -i http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000/ready
```

`/health` reports process health without accessing PostgreSQL. `/ready` executes `SELECT 1`: it returns 200 when connected, or 503 with a generic error when the database is unavailable. It does not check migration status. The frontend currently displays process health only.

## Inspect and stop

From the repository root, open a database shell:

```sh
docker compose exec db psql -U pathwise -d pathwise
```

Inside psql, use `\dt` to list tables and `\q` to exit.

Stop the database while keeping data:

```sh
docker compose down
```

Run the startup command again to reuse the existing volume. Changing initialization credentials in Compose does not change credentials inside an existing database.

If port 5433 is occupied, change the host port in Compose (for example, `127.0.0.1:5434:5432`) and update `DATABASE_URL` in `backend/.env` to the same host port.

## Future schema changes

From the backend directory, after importing new model metadata into `migrations/env.py`:

```sh
python -m alembic revision --autogenerate -m "Describe the schema change"
python -m alembic upgrade head
```

Review every generated migration before applying it. The API does not create or migrate tables automatically.
