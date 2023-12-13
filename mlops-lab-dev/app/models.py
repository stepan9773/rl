from pydantic import BaseModel


class RLInput(BaseModel):
    horizontalPadCoordinate: float = 0
    verticalPadCoordinate: float = 0
    horizontalSpeed: float = 0
    verticalSpeed: float = 0
    angle: float = 0
    angularSpeed: float = 0
    rightLegContact: bool = False
    leftLegContact: bool = False


class RLOutput(BaseModel):
    action: int = 0
