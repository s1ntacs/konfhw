from lark import Lark
import re
import os

class ConfigParser:
    def __init__(self, grammar_path: str):
        if not os.path.exists(grammar_path):
            raise FileNotFoundError(f"Grammar file not found: {grammar_path}")

        with open(grammar_path, "r", encoding="utf-8") as f:
            self.grammar = f.read()

        self.parser = Lark(
            self.grammar,
            start="start",
            parser="lalr",
            propagate_positions=True
        )

    @staticmethod
    def remove_comments(text: str) -> str:
        text = re.sub(r"^REM.*$", "", text, flags=re.MULTILINE)
        text = re.sub(r"\{\{!--.*?--\}\}", "", text, flags=re.DOTALL)
        return text

    def parse_text(self, text: str):
        clean = self.remove_comments(text)
        return self.parser.parse(clean)

    def parse_file(self, file_path: str):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Input file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        return self.parse_text(text)
