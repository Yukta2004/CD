# Shift Reduce Parser in Python

# Grammar rules
productions = {
    "E+E": "E",
    "E*E": "E",
    "(E)": "E",
    "id": "E"
}

def shift_reduce_parser(input_string):
    stack = []
    input_tokens = input_string.split()
    actions = []

    print(f"{'Stack':<30} {'Input':<30} Action")
    print("="*70)

    while True:
        # Shift
        if input_tokens:
            token = input_tokens.pop(0)
            stack.append(token)
            actions.append("Shift")
        else:
            actions.append("No more input")

        print(f"{' '.join(stack):<30} {' '.join(input_tokens):<30} {actions[-1]}")

        # Try Reduce
        reduced = True
        while reduced:
            reduced = False
            for i in range(len(stack)):
                substr = ' '.join(stack[i:])
                if substr in productions:
                    rule = productions[substr]
                    stack = stack[:i] + [rule]
                    actions.append(f"Reduce by {rule} → {substr}")
                    print(f"{' '.join(stack):<30} {' '.join(input_tokens):<30} {actions[-1]}")
                    reduced = True
                    break

        if not input_tokens and stack == ["E"]:
            print(f"\nFinal Result: ACCEPTED")
            return

        if not input_tokens and stack != ["E"]:
            print(f"\nFinal Result: REJECTED")
            return

# Example usage
input_expr = "id + id * id"
shift_reduce_parser(input_expr)
