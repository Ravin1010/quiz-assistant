from dataclasses import dataclass, field


@dataclass
class OCRResult:
    text: str
    confidence: float


@dataclass
class MCQ:
    question: str
    choices: list[str] = field(default_factory=list)