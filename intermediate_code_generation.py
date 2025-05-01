def generate_intermediate_code():
    n = int(input("Enter the number of expressions: "))
    expressions = []

    print("Enter expressions in format: [operator] [arg1] [arg2] [result]")
    print("Example: + a b t1")
    print("For assignments, use '=' as the operator and leave [arg2] blank.")
    print("Example: = a  t1")

    # Read input expressions
    for i in range(n):
        expr = input(f"Expression {i + 1}: ")
        expressions.append(expr.strip())

    print("\nGenerated Intermediate Code:")

    # Process each expression
    for expr in expressions:
        parts = expr.split()
        op = parts[0]

        if op == "=":  # Assignment
            # Handle assignment separately, as it has only 3 parts
            if len(parts) == 3:
                arg1 = parts[1]
                result = parts[2]
                print(f"MOV R0, {arg1}")
                print(f"MOV {result}, R0")
            else:
                print(f"Invalid assignment expression: {expr}")
        elif len(parts) == 4:
            # Handle other operations with 4 parts
            _, arg1, arg2, result = parts 

            if op == "+":
                print(f"MOV R0, {arg1}")
                print(f"ADD R0, {arg2}")
                print(f"MOV {result}, R0")
            elif op == "-":
                print(f"MOV R0, {arg1}")
                print(f"SUB R0, {arg2}")
                print(f"MOV {result}, R0")
            elif op == "*":
                print(f"MOV R0, {arg1}")
                print(f"MUL R0, {arg2}")
                print(f"MOV {result}, R0")
            elif op == "/":
                print(f"MOV R0, {arg1}")
                print(f"DIV R0, {arg2}")
                print(f"MOV {result}, R0")
        else:
            print(f"Invalid expression: {expr}")

if __name__ == "__main__":
    generate_intermediate_code()

# Enter the number of expressions: 2
#Enter expressions in format: [operator] [arg1] [arg2] [result]
#Example: + a b t1
#For assignments, use '=' as the operator and leave [arg2] blank.
#Example: = a  t1
#Expression 1: + a b t1
#Expression 2: = a t2

#Generated Intermediate Code:
#MOV R0, a
#ADD R0, b
#MOV t1, R0
#MOV R0, a
#MOV t2, R0
