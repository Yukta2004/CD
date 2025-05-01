class SymbolTableEntry:
    def __init__(self, symbol, symbol_type, scope="global", address=None):
        self.symbol = symbol
        self.type = symbol_type
        self.scope = scope
        self.address = address if address is not None else hex(id(self)) #unique address


class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, symbol, symbol_type, scope="global"):
        entry = SymbolTableEntry(symbol, symbol_type, scope)
        self.table[symbol] = entry
        return entry  # Return entry for potential address assignment

    def lookup(self, symbol):
        return self.table.get(symbol)  # None if not found

    def display(self):
        print("\n-------------------------------------------------------")
        print("| {:<10} | {:<15} | {:<12} | {:<8} |".format("Symbol", "Address", "Type", "Scope"))
        print("-------------------------------------------------------")

        for entry in self.table.values():
            print("| {:<10} | {:<15} | {:<12} | {:<8} |".format(
                entry.symbol, entry.address, entry.type, entry.scope
            ))

        print("-------------------------------------------------------")


def main():
    expr = input("Enter expression terminated by $: ")
    expr = expr.split('$')[0]  # Remove everything after (and including) '$'

    symbol_table = SymbolTable()

    print("\nGiven Expression:", expr)

    for c in expr:
        if not c.isalnum() and c not in "+-*/= ":
            continue  # Skip invalid characters

        if not symbol_table.lookup(c):  # If not already in the table
            if c.isalnum():
                symbol_table.insert(c, "Identifier")
            elif c in "+-*/=":
                symbol_table.insert(c, "Operator")

    symbol_table.display()

if __name__ == "__main__":
    main()
