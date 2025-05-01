MAX = 100

# LR(0) Parsing Table for the grammar S->AA, A->aA | b
action = [
    ["S1", "S2", ""],  # State 0
    ["S3", "S4", "R2"], # State 1
    ["R3", "R3", "R3"], # State 2
    ["S1", "S2", ""],  # State 3
    ["R3", "R3", "R3"], # State 4
    ["R1", "R1", "R1"], # State 5
    ["", "", "Accept"]   # State 6
]

# Goto Table for the given grammar
gotoTable = [
    [3],
    [5],
    [0],
    [6],
    [5],
    [0],
    [0]
]

# Stack for parsing
stack = []
top = -1

# Push function
def push(state):
    global top
    if top < MAX - 1:
        top += 1
        stack.append(state)

# Pop function
def pop(count):
    global top
    if top >= count - 1:
        for _ in range(count):
            if stack:
                stack.pop()
                top -= 1

# Function to check valid input characters
def isValidInput(input_str):
    for char in input_str:
        if char not in ['a', 'b', '$']:
            return False
    return True

# Function to perform parsing
def parse(input_str):
    global top
    if not isValidInput(input_str):
        print("Error: Invalid characters in input!")
        return False

    i = 0
    push(0)  # Start state

    print("\nParsing Steps:")
    print(f"{'Stack':<10} {'Input':<15} {'Action'}")
    print("-" * 35)

    while True:
        state = stack[top]
        symbol = input_str[i]

        actionIndex = -1
        if symbol == 'a':
            actionIndex = 0
        elif symbol == 'b':
            actionIndex = 1
        elif symbol == '$':
            actionIndex = 2

        if actionIndex == -1:
            print("Parsing Failed: Invalid Input Symbol")
            return False

        act = action[state][actionIndex]

        stack_str = "".join(map(str, stack))
        print(f"{stack_str:<10} {input_str[i:]:<15} {act}")

        if act.startswith('S'):  # Shift
            push(int(act[1:]))
            i += 1
        elif act.startswith('R'):  # Reduce
            rule = int(act[1:])
            if rule == 1:  # A -> aA
                pop(2)
                if stack:
                    push(gotoTable[stack[-1]][0])
            elif rule == 2:  # A -> b
                pop(1)
                if stack:
                    push(gotoTable[stack[-1]][0])
            elif rule == 3:  # S -> AA
                pop(2)
                if stack:
                    push(gotoTable[stack[-1]][0])
        elif act == "Accept":
            print("Parsing Successful!")
            return True
        else:
            print("Parsing Failed.")
            return False

# Function to print the Parsing Table
def printParsingTable():
    print("\nLR(0) Parsing Table:")
    print(f"{'State':<7} | {'a':<5} | {'b':<5} | {'$':<5} |")
    print("-" * 27)
    for i in range(7):
        print(f"{i:<7} | {action[i][0]:<5} | {action[i][1]:<5} | {action[i][2]:<5} |")
    print("-" * 27)

# Driver
if _name_ == "_main_":
    input_str = input("Enter input string ending with '$': ")
    printParsingTable()
    parse(input_str)
