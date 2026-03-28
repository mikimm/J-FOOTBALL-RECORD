from typing import Dict, TypeVar
from dacite import from_dict

T = TypeVar("T")
def convert_to_dataclass(origin_dataclass:T,origin_dict:Dict):
    return from_dict(data_class=origin_dataclass,data=origin_dict)