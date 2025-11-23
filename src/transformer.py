from lark import Transformer

class ConfigTransformer(Transformer):
    def start(self, items):
        return ("start", items)

    def item(self, items):
        return items[0]

    def const_def(self, items):
        name = items[0]
        value = items[1]
        return ("const_def", name, value)

    def value(self, items):
        return items[0]

    def NUMBER(self, token):
        return ("number", int(token))

    def string(self, items):
        raw = items[0]
        return ("string", raw[1:-1])

    def array(self, items):
        return ("array", items)

    def const_use(self, items):
        name = items[0]
        return ("const_use", name)

    def NAME(self, token):
        return str(token)
