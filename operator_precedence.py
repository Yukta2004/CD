# Operator precedence parsing table
precedence = {
    '+': {'+': '>', '*': '<', '(': '<', ')': '>', 'id': '<', '$': '>'},
    '*': {'+': '>', '*': '>', '(': '<', ')': '>', 'id': '<', '$': '>'},
    '(': {'+': '<', '*': '<', '(': '<', ')': '=', 'id': '<', '$': 'E'},
    ')': {'+': '>', '*': '>', '(': 'E', ')': '>', 'id': 'E', '$': '>'},
    'id': {'+': '>', '*': '>', '(': 'E', ')': '>', 'id': 'E', '$': '>'},
    '$': {'+': '<', '*': '<', '(': '<', ')': 'E', 'id': '<', '$': 'A'},
}

def get_top_terminal(stack):
    # Return the topmost terminal symbol in stack
    for sym in reversed(stack):
        if sym in precedence:
            return sym
    return None

def operator_precedence_parser(expression):
    stack = ['$']
    tokens = expression.split() + ['$']

    print(f"{'Stack':<30} {'Input':<30} Action")
    print("="*70)

    while True:
        top = get_top_terminal(stack)
        curr = tokens[0]

        action = precedence[top][curr]

        if action == '<' or action == '=':
            # Shift
            stack.append(tokens.pop(0))
            print(f"{' '.join(stack):<30} {' '.join(tokens):<30} Shift")
        elif action == '>':
            # Reduce
            reduced = False
            if stack[-1] == 'id':
                stack[-1] = 'E'
                reduced = True
            elif len(stack) >= 3 and stack[-1] == 'E' and stack[-2] in ['+', '*'] and stack[-3] == 'E':
                stack[-3:] = ['E']
                reduced = True
            elif len(stack) >= 3 and stack[-1] == ')' and stack[-2] == 'E' and stack[-3] == '(':
                stack[-3:] = ['E']
                reduced = True
            if reduced:
                print(f"{' '.join(stack):<30} {' '.join(tokens):<30} Reduce")
            else:
                print(f"{' '.join(stack):<30} {' '.join(tokens):<30} ERROR: Cannot reduce")
                break
        elif action == 'A':
            print(f"{' '.join(stack):<30} {' '.join(tokens):<30} ACCEPTED")
            break
        else:
            print(f"{' '.join(stack):<30} {' '.join(tokens):<30} ERROR")
            break

# Example usage
input_expr = "id + id * id"
operator_precedence_parser(input_expr)

