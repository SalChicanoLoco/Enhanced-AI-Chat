from typing import Dict, List

from core.models import AuthMode, Capability, ProviderId
from providers.base import BaseProvider, EchoProvider


class ProviderRegistry:
    def __init__(self):
        self._providers: Dict[ProviderId, BaseProvider] = {
            ProviderId.CHATGPT: EchoProvider(
                provider_id=ProviderId.CHATGPT,
                display_name="ChatGPT (OpenAI)",
                auth_modes=[AuthMode.API_KEY, AuthMode.OAUTH],
                capabilities=[Capability.CHAT, Capability.ARTIFACTS, Capability.TOOL_USE, Capability.CODE],
                docs_url="https://platform.openai.com/docs/overview",
            ),
            ProviderId.CODEX: EchoProvider(
                provider_id=ProviderId.CODEX,
                display_name="Codex (OpenAI)",
                auth_modes=[AuthMode.API_KEY, AuthMode.OAUTH],
                capabilities=[Capability.CHAT, Capability.CODE, Capability.TOOL_USE],
                docs_url="https://platform.openai.com/docs",
            ),
            ProviderId.CLAUDE: EchoProvider(
                provider_id=ProviderId.CLAUDE,
                display_name="Claude (Anthropic)",
                auth_modes=[AuthMode.API_KEY, AuthMode.OAUTH],
                capabilities=[Capability.CHAT, Capability.ARTIFACTS, Capability.TOOL_USE, Capability.CODE],
                docs_url="https://docs.anthropic.com/",
            ),
            ProviderId.GEMINI: EchoProvider(
                provider_id=ProviderId.GEMINI,
                display_name="Gemini (Google)",
                auth_modes=[AuthMode.API_KEY, AuthMode.OAUTH],
                capabilities=[Capability.CHAT, Capability.ARTIFACTS, Capability.TOOL_USE, Capability.CODE],
                docs_url="https://ai.google.dev/gemini-api/docs",
            ),
            ProviderId.GROK: EchoProvider(
                provider_id=ProviderId.GROK,
                display_name="Grok (xAI)",
                auth_modes=[AuthMode.API_KEY],
                capabilities=[Capability.CHAT, Capability.CODE, Capability.TOOL_USE],
                docs_url="https://docs.x.ai/docs/overview",
            ),
        }

    def list(self) -> List[BaseProvider]:
        return list(self._providers.values())

    def get(self, provider_id: ProviderId) -> BaseProvider:
        return self._providers[provider_id]
