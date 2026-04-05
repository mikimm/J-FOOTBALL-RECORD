from typing import Any, Protocol

class Usecase(Protocol):

    def handle(self,**kwargs) -> dict:
        ...