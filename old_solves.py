# parser
from tokenizer import Operator, Number, Paren

LEFT_PAREN = 2
RIGHT_PAREN = 3

class Object:
    def __init__(self, obj):
        self.object = obj
        self.next_object = None


class Stack:
    def __init__(self):
        self.high_object = None

    def push(self, obj):
        new_object = Object(obj)

        new_object.next_object = self.high_object
        self.high_object = new_object

    def pull(self):
        if self.high_object is  None:
            return None

        obj = self.high_object.object
        self.high_object = self.high_object.next_object
        return obj

    def check(self):
        if self.high_object is None:
            return None
        return self.high_object.object

def to_reverse_polish_notation(expression: list):
    rpn_expression = []
    operators_stack = Stack()
    for obj in expression:
        if isinstance(obj, Number):
            rpn_expression.append(obj.value)
        elif isinstance(obj, Operator):
            if operators_stack.check() is None:
                operators_stack.push(obj)
            else:
                high_object = operators_stack.check()
                if isinstance(high_object, Operator):
                    if high_object.priority >= obj.priority:
                        operators_stack.pull()
                        rpn_expression.append(high_object.operator)
                operators_stack.push(obj)
        elif isinstance(obj, Paren):
            if obj.is_open:
                operators_stack.push(obj)
            elif not obj.is_open:
                high_object = operators_stack.pull()
                while not isinstance(high_object, Paren):
                    rpn_expression.append(high_object.operator)
                    high_object = operators_stack.pull()

    while operators_stack.check() is not None:
        obj_operator = operators_stack.pull()
        rpn_expression.append(obj_operator.operator)

    return rpn_expression