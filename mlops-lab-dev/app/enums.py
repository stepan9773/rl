from enum import auto, Enum


class StrEnum(str, Enum):
    pass


class AutoName(StrEnum):
    def _generate_next_value_(name, start, count, last_values):
        return name


class RLModels(AutoName):
    PPO = auto()
