from typing import Dict, Any


class BaseProvider:
    def generate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
