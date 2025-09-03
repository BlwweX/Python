from datetime import datetime
from dataclasses import dataclass
from typing import Literal
from typing import Optional

@dataclass(frozen=True)
class ColorConfig:
    DebugColor: tuple[int, int, int] = (255, 255, 255)
    InfoColor: tuple[int, int, int] = (162, 255, 213)
    WarningColor: tuple[int, int, int] = (255, 208, 20)
    ErrorColor: tuple[int, int, int] = (255, 68, 0)
    CriticalColor: tuple[int, int, int] = (190, 0, 0)

loggingLevels: dict[str, int] = {
    "Debug": 1,
    "Info": 2,
    "Warning": 3,
    "Error": 4,
    "Critical": 5,
}

def RgbToTerminal(rgbTuple: tuple[int, int, int]) -> str:
    r, g, b = rgbTuple
    return f"\033[38;2;{r};{g};{b}m"


class Logger:
    def __init__(self, prefix: Optional[str]) -> None:
        self.ColorConfig = ColorConfig()
        self.Prefix = prefix.upper() if prefix else None
        self.MinimumLevel = "Debug"
        
    def __call__(self, logType: Literal["Debug", "Info", "Warning", "Error", "Critical"], message: str) -> None:
        if loggingLevels[logType] < loggingLevels[self.MinimumLevel]:
            return
        
        colorPrefix = RgbToTerminal(getattr(self.ColorConfig, f"{logType}Color"))
        ourPrefix = self.Prefix or logType

        print(f"{colorPrefix}{datetime.now()} [{ourPrefix.upper()}]: {message}\033[0m")
        
    def set_minimum_level(self, logType: Literal["Debug", "Info", "Warning", "Error", "Critical"]) -> None:
        self.MinimumLevel = logType