#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#define maxqueue 6

struct queue
{
    int front;
    int rear;
    int a[maxqueue];
};

typedef struct queue Queue;

typedef enum action{arrive,depart}Action;

void getdetails(int *,int *,int *);
void display1();
void display2(int,int,int,int);
void createqueue(Queue *,int,int *,int *,int *,Action kind);
int empty(struct queue *);
void refuse_plane(int,Action);

int main()
{
    Queue landing,takeoff;
    Queue *pl=&landing;
    Queue *pt=&takeoff;
    int current_time=1;//current time, one unit for taking off and landing.
    int end_time;//total units of time for simulation.
    int expect_arrive;//time used by 1 plane to arrive.
    int expect_depart;//time used by 1 plane to depart.
    int i,ch,id,j,k;
   
//initializing the front and rear pointers of the landing queue as well as the takeoff queue.
    pl->front=pl->rear=maxqueue-1;
    pt->front=pt->rear=maxqueue-1;

    int n_land=0;//number of planes landed.
    int n_takeoff=0;//number of planes taking off.
    int n_planes=0;//number of planes processed so far.
    int n_refuse=0;//number of planes being refused.

    display1();
    int choice=1;
    getdetails(&end_time,&expect_arrive,&expect_depart);

    while(current_time<=end_time)
    {
        printf("1.Landing 2.Take off 3.Service");
        printf("\nEnter choice:-");
        scanf("%d",&ch);
        switch(ch)
        {
            case 1:
            {
                do
                {
 	              printf("Enter the id of plane to be landing:-");
        	        scanf("%d",&id);
                	  createqueue(pl,id,&n_land,&n_refuse,&n_planes,arrive);
	              current_time++;
        	        if(current_time>end_time)
                	        break;
			  printf("Do you wish to continue:-1.yes 2.no:-");
        	        scanf("%d",&choice);
                }while(choice<2);
    		    printf("\n");
                break;
            }
	    case 2:
	    {
                do
                {
	              printf("\nEnter the id of the plane to take off:-");
        	        scanf("%d",&id);
                	               
              createqueue(pt,id,&n_takeoff,&n_refuse,&n_planes,depart);
        	        current_time++;
	             if(current_time>end_time)
                	        break;
		   	printf("Do you wish to continue:-1.yes 2.no:-");
        	        scanf("%d",&choice);
                }while(choice<2);
		    printf("\n");
                break;
	    }
	    case 3:
	    {
		//check whether the landing queue is empty or not. If not empty then service the planes.
		if((empty(pl)))
        	printf("Landing queue empty\n");
		else
		{
                	j=((pl->front)+1)%maxqueue;
	                while(j!=(pl->rear+1)%maxqueue)
        	        {
			
                	        printf("The plane with id %3d has been landed.\n",pl->a[j]);
				pl->front=(pl->front+1)%maxqueue;
                               j=(j+1)%maxqueue;
	                }
	        }
    	
	      k=((pt->front+1)%maxqueue);
		if(empty(pt))
		printf("Takeoff queue empty\n");
		else
		{
                	printf("The plane %3d took off.\n",pt->a[k]);
	                pt->front=(pt->front+1)%maxqueue;
		}
        	break;
            }
	}//end of switch case
    }//end of while
    
/*After the total simulation time is over, all the planes must be serviced..
So first the landing queue will be serviced then the takeoff queue will be serviced..
*/
    if((empty(pl)))
         printf("Landing queue empty\n");
    else
    {
         j=((pl->front)+1)%maxqueue;
         while(j!=(pl->rear+1)%maxqueue)
         {
             printf("The plane with id %3d has been landed.\n",pl->a[j]);
                 j=(j+1)%maxqueue;
         }
         pl->front=(pl->front+1)%maxqueue;
     }
     
     k=((pt->front+1)%maxqueue);
     if(empty(pt))
           printf("Takeoff queue empty\n");
     else
     {
	  while(k!=(pt->rear+1)%maxqueue)
	  {
              printf("The plane %3d took off.\n",pt->a[k]);
	        pt->front=(pt->front+1)%maxqueue;
		  k=(k+1)%maxqueue;
          }
     }  
     display2(n_land,n_takeoff,n_refuse,n_planes);
}

void display2(int n1,int n2,int n3,int n4)
{
        printf("\nTotal planes processed so far:-%d",n4);
        printf("\nTotal planes landed are:-%d",n1);
        printf("\nTotal planes took off are:-%d",n2);
        printf("\nTotal planes refused are:-%d\n",n3);
}

void getdetails(int *end_time,int *expect_arrive,int *expect_depart)
{ 
    printf("Enter the units of time the simulation will take:-");
    scanf("%d",end_time);
    printf("\nEnter the units of time for flight to arrive:-");
    scanf("%d",expect_arrive);
    printf("\nEnter the units of time for flight to depart:-");
    scanf("%d",expect_depart);
}

void display1()
{
    printf("\n");
    printf("-----------------------------------------------------\n");
    printf("\t\t\tWelcome..\n");
    printf("-----------------------------------------------------\n\n");
    printf("The program simulates an airport with only one runway.\n");
    printf("One plane can land or depart in specified time.\n");
    printf("Upto  %d planes can be waiting to land or take off.\n",(maxqueue-1));
}

void createqueue(Queue *q,int id,int *n,int *refuse,int *n2,Action kind)
{
      
        if((q->rear+1)%maxqueue==q->front)
        {
                (*refuse)++;
                refuse_plane(id,kind);
        }
        else
        {
                q->rear=(q->rear+1)%maxqueue;
                q->a[q->rear]=id;
                (*n)++;
                (*n2)++;
        }
}

void refuse_plane(int id,Action kind)
{
     switch(kind)
     {
        case arrive:
             printf("Plane %3d directed to a different airport.\n",id);
		  break;
        case depart:
             printf("Plane %3d requested to try later.\n",id);
		  break;
     }
}

int empty(struct queue *q)
{
        if(q->front==q->rear)
                return 1;
        else
                return 0;
}


