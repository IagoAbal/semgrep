from typing import NamedTuple, Any
class LineCol(NamedTuple):
    line: int
    column: int

class Node(NamedTuple):
    start_mark: LineCol
    end_mark: LineCol

class RoundTripConstructor:
    def construct_object(self, node: Node, deep: bool = False) -> Any:
        ...

class YAML:
    Constructor: Any
    representer: Any
    def load(self, stream: Any) -> Any:
        ...

    def dump(self, obj: Any, stream: Any) -> None:
        ...


class YAMLError(Exception):
    ...
