#include <stdio.h>
#include <string.h>
int main(int argc,char* argv[])
{	
			char word[]="Public speaking is very easy.",buffer[100];
			FILE *f;
			int i,count1=0,count2=0,flag=0;
			if(argc>2)
			{
				printf("Usage: %s [<input_file>]\n",argv[0]);
				return 0;

			}
			else if(argc==2)
			{	 
				f=fopen(argv[1],"r");
				if(f==NULL)
				{
					printf("%s: Error : Couldn't open %s\n",argv[0],argv[1]);
					return 0;
				}
				else
				{
					fread(&buffer,1,29,f);
					fclose(f);
				}
			}		

	
			printf("Welcome to my fiendish little bomb. You have 6 phases with\nwhich to blow yourself up. Have a nice day!\n");
			
			if(argc==1)
			scanf("%s",buffer);
			
			for(i=0;buffer[i]!='\0';i++)
			{
				count1++;
			}
			for(i=0;buffer[i]!='\0';i++)
			{
				count2++;
			}
			if(count1!=count2)
			{
				flag=1;
			}
			else
			{
				for(i=0;buffer[i]!='\0'&&word[i]!='\0';i++)
				{
					if(buffer[i]!=word[i])
					{
						flag=1;
					}
				}
			}
			if(flag==0)
			{
				printf("Phase 1 defused. How about the next one?\n");
			}	
			else
			{
				printf("BOOM!!!\n");
				printf("The bomb has blown up.\n");
			}
	


			return 0;

}