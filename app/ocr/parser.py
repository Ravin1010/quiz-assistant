from .models import MCQ


class QuestionParser:
    def parse(self, text: str) -> MCQ:
        raise NotImplementedError