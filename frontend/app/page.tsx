"use client";

import { useCallback, useEffect, useState } from "react";

const apiBase = (process.env.NEXT_PUBLIC_API_BASE_URL || "http://127.0.0.1:8000").replace(/\/$/, "");

export default function Home() {
  const [status, setStatus] = useState<"loading" | "ready" | "error">("loading");
  const checkHealth = useCallback(async (signal?: AbortSignal) => {
    setStatus("loading");
    try {
      const response = await fetch(apiBase + "/health", {
        signal: signal ? AbortSignal.any([signal, AbortSignal.timeout(5000)]) : AbortSignal.timeout(5000),
        cache: "no-store",
      });
      if (!response.ok) throw new Error("Health request failed");
      const data = await response.json();
      if (data.status !== "ok") throw new Error("Unexpected health response");
      if (!signal?.aborted) setStatus("ready");
    } catch {
      if (!signal?.aborted) setStatus("error");
    }
  }, []);

  useEffect(() => {
    const controller = new AbortController();
    void checkHealth(controller.signal);
    return () => controller.abort();
  }, [checkHealth]);

  return (
    <main>
      <header><a href="/" className="brand">PathWise<span> / Career assistant</span></a><span className="badge">Development preview</span></header>
      <section className="hero">
        <p className="eyebrow">Evidence for every step</p>
        <h1>Discover opportunities.<br />Find your next step.</h1>
        <p className="intro">Explore jobs, review resume evidence, and track applications to make clearer career decisions.</p>
      </section>
      <section className="connection" aria-labelledby="connection-title">
        <div><h2 id="connection-title">Service connection</h2>
          <p role="status" aria-live="polite">{status === "loading" ? "Connecting to the backend…" : status === "ready" ? "Backend connected · FastAPI is healthy" : "Cannot connect to the backend. Start the API server and try again."}</p>
          <code>{apiBase}/health</code>
        </div>
        <button disabled={status === "loading"} onClick={() => void checkHealth()}>Check again</button>
      </section>
      <section className="features" aria-label="Planned features">
        {[["01", "Discover jobs", "Browse jobs from selected sources with provenance and discovery timestamps."], ["02", "Review evidence", "Compare job requirements with evidence from your resume."], ["03", "Track applications", "Keep track of saved jobs, applications, and interviews."]].map(([number, title, description]) => (
          <article key={number}><span className="number">{number}</span><h2>{title}</h2><p>{description}</p><small>Planned</small></article>
        ))}
      </section>
      <footer>Engineering skeleton: frontend and backend connectivity only.</footer>
    </main>
  );
}
