%{
#include <stdio.h>
#include <stdlib.h>

int op = 0, i;
float a, b;
void digi();
%}

%%

[0-9]+(\.[0-9]+)?     { digi(); }
"+"                   { op = 1; }
"-"                   { op = 2; }
"*"                   { op = 3; }
"/"                   { op = 4; }
"^"                   { op = 5; }
\n                    { printf("\nThe Answer: %f\n\n", a); }

%%

void digi() {
    if (op == 0) {
        a = atof(yytext);
    } else {
        b = atof(yytext);
        switch(op) {
            case 1: a = a + b; break;
            case 2: a = a - b; break;
            case 3: a = a * b; break;
            case 4: a = a / b; break;
            case 5: for(i = a; b > 1; b--) a = a * i; break;
        }
        op = 0;
    }
}

int main(int argc, char *argv[]) {
    yylex();
    return 0;
}

int yywrap() {
    return 1;
}


flex hello.l
gcc lex.yy.c
.\a.exe
