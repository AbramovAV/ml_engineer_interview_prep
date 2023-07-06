class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        from operator import add, mul, sub, truediv 
        stack = []
        operators = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": truediv
        }
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                stack.append(int(operators[token](left_operand, right_operand)))
        return stack.pop()