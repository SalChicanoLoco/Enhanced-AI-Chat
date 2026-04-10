from enum import Enum
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class ProviderId(str, Enum):
    CHATGPT = "chatgpt"
    CODEX = "codex"
    CLAUDE = "claude"
    GEMINI = "gemini"
    GROK = "grok"


class AuthMode(str, Enum):
    API_KEY = "api_key"
    OAUTH = "oauth"


class Capability(str, Enum):
    CHAT = "chat"
    ARTIFACTS = "artifacts"
    TOOL_USE = "tool_use"
    CODE = "code"


class ProviderDescriptor(BaseModel):
    provider_id: ProviderId
    display_name: str
    auth_modes: List[AuthMode]
    capabilities: List[Capability]
    docs_url: Optional[str] = None


class ChatMessage(BaseModel):
    role: str = Field(pattern="^(system|user|assistant|tool)$")
    content: str = Field(min_length=1)


class ChatRequest(BaseModel):
    session_id: str = Field(min_length=1, max_length=128)
    provider: ProviderId
    model: str = Field(min_length=1, max_length=128)
    messages: List[ChatMessage] = Field(min_length=1)
    metadata: Dict[str, Any] = Field(default_factory=dict)


class ChatResponse(BaseModel):
    provider: ProviderId
    model: str
    output_text: str
    raw: Dict[str, Any] = Field(default_factory=dict)


class RouterBinding(BaseModel):
    route_name: str = Field(min_length=1, max_length=64)
    provider: ProviderId
    model: str = Field(min_length=1, max_length=128)


class RouterConfig(BaseModel):
    bindings: List[RouterBinding] = Field(default_factory=list)


class ThemeTokenSet(BaseModel):
    name: str = Field(min_length=1, max_length=64)
    tokens: Dict[str, str] = Field(default_factory=dict)
