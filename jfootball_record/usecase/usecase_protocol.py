from typing import Any, Protocol

from jfootball_record.adaptor.adaptor_protocol import Adaptor
class Usecase(Protocol):

    adaptor: Adaptor

    def handle(self,**kwargs) -> Any:
        ...