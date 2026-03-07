from typing import Any, Protocol
class Adaptor(Protocol):
    def call(self,**kwargs) -> Any:
        ...
