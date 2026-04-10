from typing import Dict, Optional

from core.models import ProviderId, RouterBinding, RouterConfig


class RouterRuntime:
    """Simple in-memory model router for experimental workflows."""

    def __init__(self):
        self._bindings: Dict[str, RouterBinding] = {}

    def configure(self, config: RouterConfig) -> RouterConfig:
        self._bindings = {b.route_name: b for b in config.bindings}
        return RouterConfig(bindings=list(self._bindings.values()))

    def resolve(self, route_name: str) -> Optional[RouterBinding]:
        return self._bindings.get(route_name)

    def default(self) -> RouterBinding:
        return self._bindings.get(
            "default",
            RouterBinding(route_name="default", provider=ProviderId.CHATGPT, model="gpt-4.1"),
        )
