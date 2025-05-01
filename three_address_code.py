# 3 address code
import string

temp_count = 0

def new_temp():
    global temp_count
    temp = f"t{temp_count}"
    temp_count += 1
    return temp

def generate_three_address_code(op, arg1, arg2, result):
    print(f"{result} = {arg1} {op} {arg2}")

# Operator stack and value stack
op_stack = []
val_stack = []

def precedence(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

def apply_operator():
    op = op_stack.pop()
    b = val_stack.pop()
    a = val_stack.pop()
    result = new_temp()
    generate_three_address_code(op, a, b, result)
    val_stack.append(result)

def main():
    expr = input("Enter an arithmetic expression (e.g., a+b*c-d): ").strip()

    for token in expr:
        if token.isspace():
            continue
        if token.isalnum():  # operand
            val_stack.append(token)
        elif token in '+-*/':
            while op_stack and precedence(op_stack[-1]) >= precedence(token):
                apply_operator()
            op_stack.append(token)

    while op_stack:
        apply_operator()

    # Cleanup final result (no need to free memory in Python)
    val_stack.pop()

if __name__ == "__main__":
    main()
