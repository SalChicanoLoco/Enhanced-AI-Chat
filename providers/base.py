from abc import ABC, abstractmethod
from typing import Dict, List

from core.models import AuthMode, Capability, ChatRequest, ChatResponse, ProviderDescriptor, ProviderId


class BaseProvider(ABC):
    provider_id: ProviderId
    display_name: str
    auth_modes: List[AuthMode]
    capabilities: List[Capability]
    docs_url: str

    def descriptor(self) -> ProviderDescriptor:
        return ProviderDescriptor(
            provider_id=self.provider_id,
            display_name=self.display_name,
            auth_modes=self.auth_modes,
            capabilities=self.capabilities,
            docs_url=self.docs_url,
        )

    @abstractmethod
    async def generate(self, request: ChatRequest) -> ChatResponse:
        raise NotImplementedError


class EchoProvider(BaseProvider):
    """Safe default implementation for local skeleton builds."""

    def __init__(
        self,
        provider_id: ProviderId,
        display_name: str,
        auth_modes: List[AuthMode],
        capabilities: List[Capability],
        docs_url: str,
    ):
        self.provider_id = provider_id
        self.display_name = display_name
        self.auth_modes = auth_modes
        self.capabilities = capabilities
        self.docs_url = docs_url

    async def generate(self, request: ChatRequest) -> ChatResponse:
        last_user = next((m.content for m in reversed(request.messages) if m.role == "user"), "")
        return ChatResponse(
            provider=request.provider,
            model=request.model,
            output_text=f"[{self.provider_id}] skeleton response: {last_user[:200]}",
            raw={"implementation": "echo", "next_step": "replace with SDK call"},
        )
