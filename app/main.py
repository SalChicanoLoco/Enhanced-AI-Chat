from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from core.models import ChatRequest, ChatResponse, ProviderDescriptor, RouterConfig, ThemeTokenSet
from core.provider_registry import ProviderRegistry
from core.router_runtime import RouterRuntime

app = FastAPI(title="Enhanced AI Chat", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

registry = ProviderRegistry()
router_runtime = RouterRuntime()
themes = [
    ThemeTokenSet(name="midnight", tokens={"bg": "#0b1020", "surface": "#121a2b", "accent": "#6ee7ff"}),
    ThemeTokenSet(name="sunset", tokens={"bg": "#130d1f", "surface": "#22152f", "accent": "#ff8fb1"}),
]


@app.get("/health")
def health():
    return {"status": "ok", "service": "enhanced-ai-chat"}


@app.get("/v1/providers", response_model=list[ProviderDescriptor])
def list_providers():
    return [p.descriptor() for p in registry.list()]


@app.post("/v1/chat/completions", response_model=ChatResponse)
async def chat(req: ChatRequest):
    provider = registry.get(req.provider)
    return await provider.generate(req)


@app.put("/v1/router", response_model=RouterConfig)
def configure_router(config: RouterConfig):
    return router_runtime.configure(config)


@app.get("/v1/router/{route_name}")
def resolve_router_route(route_name: str):
    binding = router_runtime.resolve(route_name)
    if not binding:
        raise HTTPException(status_code=404, detail="route not configured")
    return binding


@app.get("/v1/themes", response_model=list[ThemeTokenSet])
def list_themes():
    return themes


app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
