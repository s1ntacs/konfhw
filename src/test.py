from parser import ConfigParser
from transformer import ConfigTransformer
from evaluator import ConstantEvaluator
import os

def run_file(file_path):
    parser = ConfigParser("grammar.lark")
    transformer = ConfigTransformer()
    evaluator = ConstantEvaluator()

    print(f"\n=== Файл: {file_path} ===")

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    try:
        tree = parser.parse_text(text)
        ast = transformer.transform(tree)
        result = evaluator.evaluate(ast)
        print("Результат:")
        print(result)
    except Exception as e:
        print("Ошибка:")
        print(e)

def main():
    files = ["text1.txt", "text2.txt", "text3.txt"]

    for f in files:
        if os.path.exists(f):
            run_file(f)
        else:
            print(f"Файл {f} не найден")

if __name__ == "__main__":
    main()
