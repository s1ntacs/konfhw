class ConstantEvaluator:
    def __init__(self):
        self.constants = {}

    def evaluate(self, ast):
        tag, items = ast
        if tag != "start":
            raise ValueError("Корневой узел должен быть start")

        for node in items:
            if node[0] == "const_def":
                self._add_constant(node)

        evaluated_items = [self._eval_node(node) for node in items]


        return evaluated_items

    def _add_constant(self, node):
        _, name, value = node
        if name in self.constants:
            raise ValueError(f"Константа {name} определена дважды")
        evaluated_value = self._eval_node(value)
        self.constants[name] = evaluated_value


    def _eval_node(self, node):
        tag = node[0]

        if tag == "const_def":
            return None

        if tag == "const_use":
            name = node[1]
            if name not in self.constants:
                raise ValueError(f"Неизвестная константа: {name}")
            return self._deep_copy(self.constants[name])

        if tag == "array":
            values = node[1]
            return ("array", [self._eval_node(v) for v in values])

        return node

    def _deep_copy(self, value):
        tag = value[0]

        if tag in ("number", "string"):
            return (tag, value[1])

        if tag == "array":
            return ("array", [self._deep_copy(x) for x in value[1]])

        raise ValueError(f"Нельзя скопировать значение типа {tag}")
