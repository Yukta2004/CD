%{
#include <stdio.h>
#include <stdlib.h>

int result = 0, num = 0;
char last_op = 0; // Store the last operator, initialize as 0 (no operator yet)
int firstNumber = 1; // Flag to track the first number
%}

%%

[0-9]+  { 
    num = atoi(yytext); 
    printf("Number: %d\n", num);

    if (firstNumber) {  
        result = num; // Initialize result with the first number
        firstNumber = 0;
    } else { 
        // Perform the operation using the last stored operator
        switch(last_op) {
            case '+': result += num; break;
            case '-': result -= num; break;
            case '*': result *= num; break;
            case '/': 
                if (num == 0) {
                    printf("Error: Division by zero\n");
                    exit(1);
                }
                result /= num; 
                break;
        }
    }
}

"*"     { printf("Operator: *\n"); last_op = '*'; }
"+"     { printf("Operator: +\n"); last_op = '+'; }
"-"     { printf("Operator: -\n"); last_op = '-'; }
"/"     { printf("Operator: /\n"); last_op = '/'; }
"="     { printf("Final Result: %d\n", result); exit(0); }
[ \t\n] { /* Ignore whitespace */ }
.       { printf("Unknown Symbol: %s\n", yytext); }

%%

int main() {
    printf("Enter an arithmetic expression (end with =):\n");
    yylex(); // Start lexical analysis
    return 0;
}

int yywrap() {
    return 1; // Return 1 to indicate EOF
}


#flex file_name.l
#gcc lex.yy.c
#.\a.exe
