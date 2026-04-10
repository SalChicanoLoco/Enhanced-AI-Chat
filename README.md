# Enhanced AI Chat (Skeleton)

Portable, multi-provider chat app scaffold for **web + mobile-first + desktop-ready** usage.

## What this skeleton gives you now

- FastAPI backend with a **provider abstraction layer** and a single chat endpoint.
- Pre-registered providers for:
  - ChatGPT (OpenAI)
  - Codex (OpenAI)
  - Claude (Anthropic)
  - Gemini (Google)
  - Grok (xAI)
- Experimental **router middleware** endpoint to map task routes (e.g. `coding`, `research`) to provider+model pairs.
- Responsive **UI shell** with a modern chat layout, provider/model switcher, and runtime theme switching.
- Theme token system (`/v1/themes`) so skins can be swapped quickly without rewrites.

> Current provider implementations are safe echo stubs. Replace each stub with official SDK calls once credentials are wired.

## API surface

- `GET /health`
- `GET /v1/providers`
- `POST /v1/chat/completions`
- `PUT /v1/router`
- `GET /v1/router/{route_name}`
- `GET /v1/themes`

## Architecture (starting point)

```text
Client Shell (web/PWA now, Capacitor/Tauri later)
   |
   v
FastAPI Gateway
   ├─ Auth Layer (OAuth + API key brokerage)
   ├─ RouterRuntime (task route -> provider/model)
   ├─ ProviderRegistry
   │   ├─ OpenAI adapter (ChatGPT/Codex)
   │   ├─ Anthropic adapter (Claude)
   │   ├─ Google adapter (Gemini)
   │   └─ xAI adapter (Grok)
   └─ Artifact/Tool execution services (next step)
```

## Stable connector strategy (what to plug in next)

Use official SDKs and OAuth libraries first:

- OpenAI: `openai` SDK
- Anthropic: `anthropic` SDK
- Google Gemini: `google-genai` or current official Gemini SDK path
- xAI: official `xai-sdk`
- OAuth broker: `Authlib` (FastAPI) or external IdP (Auth0/Clerk/WorkOS)

### Why this approach

- Avoids custom auth implementations.
- Keeps provider adapters isolated and replaceable.
- Makes it easy to add/remove platforms later without rewriting UI or orchestration.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Next implementation milestones

1. Add real OAuth callback/session endpoints (`/v1/auth/*`) with secure token storage.
2. Replace `EchoProvider` with provider-specific adapters using official SDKs.
3. Add streaming responses (SSE/WebSocket).
4. Add artifact service (file generation, previews, downloads).
5. Add plugin contract for external platform APIs and your router software.
6. Package the same UI for mobile/desktop (PWA + Capacitor/Tauri).
