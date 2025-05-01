%{
# include <stdio.h>
# include <string.h>
%}

%option noyywrap

%%

"int"|"float"|"char"|"if"|"else"|"while"|"return" { printf("Keyword: %s\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]* { printf("Identifier: %s\n", yytext); }
[0-9]+                { printf("Constant: %s\n", yytext); }
[+\-*/=]              { printf("Operator: %s\n", yytext); }
[}{][)(,:';"]          { printf("Seperator: %s\n", yytext); }
[$@#&^!?]         { printf("Special Charactor: %s\n", yytext); }
[ \t\n]               { /* Ignore whitespace */ }
.                     { printf("Unknown Symbol: %s\n", yytext); }

%%

int main() {
    printf("Enter a program snippet: \n");
    yylex(); // Start lexical analysis
    return 0;
}


#flex file_name.l
#gcc lex.yy.c
#.\a.exe
