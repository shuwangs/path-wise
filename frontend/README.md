# Frontend

Next.js + TypeScript frontend. The homepage checks backend health and supports retry on failure. Product workflows are planned.

Requires Node.js 20.9+; use a supported LTS release.

From the repository root:

```sh
cd frontend
npm ci
npm run dev
```

Open http://127.0.0.1:3000. Press Ctrl+C to stop.

Production build and startup:

```sh
npm run build
npm run start
```

Type checking: `npm run typecheck`.

Optional configuration: copy `.env.example` to `.env.local`, set `NEXT_PUBLIC_API_BASE_URL`, then restart the frontend. The default is http://127.0.0.1:8000. Health requests time out after five seconds.
