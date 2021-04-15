#include<stdio.h>
//features i think of adding
//to make todo with array of struct
//add - [1]
//Read - to see my to do list [2]
//update - mark as done todo [3]
// delete 
//edit - only edit completed ones [4]
//exit [5]
struct todo {
    int index;
    char task[100];
    const char* status;
};


void  main(){
    struct todo list[15];
    int action,i=0,editno,iexit=0;
    while(1){
        if(i>10){
            printf("Note: You can only add %d more todo now\n",15-i);
            printf("You can still replace any completed todo with a new pending one\n");
        }
        printf("Choose operation to perform from following options:\n");
        printf("To add a todo enter '1'\n");
        printf("To read todo list enter '2'\n");
        printf("To change a todo status enter '3'\n");
        printf("To edit a todo enter '4'\n");
        //printf("To delete a todo enter ''\n");
        printf("To exit the app enter '5'\n");
        scanf("%d",&action);
        switch (action)
        {
        case 1:
            if(i<15){
            printf("Type it all out in one word:\n");
            list[i].index = i+1;
            scanf("%s",&list[i].task);
            list[i].status = "pending";
            i++;
            break;
            }
            else{
                 printf("LIMIT EXCEEDED : Can't add more todo\n");
                 /*printf("You can still replace any completed todo with a new pending one\n");
                 commenting it out as not necessary line*/
                break;
            }
        case 2:
            printf("Your todo list is as follows :\n");
            for(int j=0;j<i;j++){
                printf("%d. %s - %s\n",list[j].index,list[j].task,list[j].status);
            }
            break;
        case 3:
            printf("Enter the index of todo you want to change status of:\n");
            scanf("%d",&editno);
            if(list[editno-1].status == "pending"){
                list[editno-1].status = "DONE";
            }
            else{
                list[editno-1].status = "pending";
            }
            break;
        case 4:
            printf("Enter the index of todo you want to edit:\n");
            scanf("%d",&editno);
            if(editno<16){
            printf("Type it all out in one word:\n");
            scanf("%s",&list[editno-1].task);
            list[editno-1].status = "pending";
            break;
            }
            else{
                 printf("How can you edit a todo which is not even in list?\n");   
                break;
            }
        case 5:
            printf("!! W A R N I N G\n");
            printf("This action will cause loss of all data that you have added\n");
            printf("Press '1' if you still want to proceed\n");
            printf("Press '0' to continue adding todo\n");
            scanf("%d",&iexit);
            break;

        default:
            printf("Are bhamiya jo options hain unme se choose kariye na\n");
            break;
        }
        if(iexit==1){
            printf("Sayonara senpai :sad loli noices:\n");
            break;
            }
        


    }















    
}


/*
LIST OF ALL BUGS / PROBLEMS I'M CURRENTLY FACING
1. One word todo addition is possible, if i seprate with space, it gets treated as new todo
    > i don't understand why value of i gets updated in doing so
    > one funny thing that i oberseved is that if i add more than 15 input at first then this while loop runs infinitely as if
        it is running over and over again to add those todo but ofc i coded it this way so max todo limit is 15, maybe that
        will help me understand how this works
2. Unable to add delete todo feature
*/