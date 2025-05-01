// 1 lexical error
// #include <stdio.h>

// int main()
// {
//     printf("Compiler Design
//     return 0;
// }


//2 lexical error

// #include <stdio.h>

// int main(){
// int 1age = 40;

//     printf("Age:",&age);
//     return 0;
// }




// 1 semantic error
// #include <stdio.h>
// int main()
// {
// if (a == 10)
// {
//     printf("a :%d\n",a);
// }

//     return 0;
// }


// 2 semantic error

// #include <stdio.h>

//int myFunc(){
// int num1,num2;
// printf("Enter num1 : ");
// scanf("%d",&num1);
// printf("Enter num2 : ");
// scanf("%d",&num2);
// int result = num1 + num2
// return result;
}
// int main()
// {
//  my Func(18,12);
//  printf("The result is:%d\n",result);    
//     return 0;
// }



// 1 syntax error
// #include <stdio.h>

// int main() {
//     for (int i = 1; i <= 10; i++) {
//         printf("%d\n" i)
//     return 0;
// }


//2  syntax error
#include <stdio.h>

int printNumbers(int n)
for(int i = 0;i <n; i++){
printf("Number : %d\n",i)
}

int main(){
   printNumbers(10);
    return 0;

