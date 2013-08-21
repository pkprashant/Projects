import sys
import string
def display():
	print "DML"
	print "|\n|\n|\n|"
	if (len(attr)==1):
		print "SELECT--------",attr[0]
		print "|\n|\n|\n|"
	else:
		print "SELECT-------------------"
		for i in range(len(attr)):
			print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
		        print "\t|\t\t|--------",attr[i]
			if(i!=(len(attr)-1)):
				print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
				print "\t|\t\t|--------','"
	if(len(fromattr1)==1):
                print "------FROM-------------",fromattr1[0]
        else:
                print "------FROM-------------"
                for i in range(len(fromattr1)):

                        print "\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
                        print "\t|\t\t--------",fromattr1[i]
			if(i!=(len(fromattr1)-1)):
				print "\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t"
				print "\t|\t\t|--------','"
	print "\t|\n\t|\n\t|\n\t|"

	if(len(arg)==1):# and s.find("where",begindex)==-1):
		print "\tWHERE-----------",arg[0]
	else:
		print "\tWHERE-----------"
		for i in range(len(arg)):

			print "\t\t\t|\n\t\t\t|\n\t\t\t|\n\t\t\t|"
		        print "\t\t\t--------",arg[i]
			if(i!=(len(arg)-1)):
				print "\t\t\t|\n\t\t\t|\n\t\t\t|\n\t\t\t|"	
			        print "\t\t\t--------','"
	print "\t\t\t|\n\t\t\t|\n\t\t\t|\n\t\t\t|"
	print "\t\t\t--------';'"




f=open("input.txt",'r')
temporary=f.read()
temporary=temporary.splitlines()
s=""
for i in range(len(temporary)):
    temporary[i]=temporary[i].strip()
    s=s+temporary[i]+" "
s=s.strip()
s=s.lower()
if(s.find("select")==-1 and s[-1]!=";"):
	print "Invalid syntax."
	sys.exit(1)
attr=[]
fromattr=""
fromattr1=[]
relop=["=","<",">",">=","<=","<>","between","like","in"]


begindex=s.find("select")+7
endindex=s.find("from")-1
if(endindex==-2):
	print "no from clause."
	sys.exit(1)
index=begindex
if(s[begindex:endindex]=="*"):
	print "all the entries from the table"
	attr.append("*")
else:
	attr=s[begindex:endindex]
	attr=attr.split(",")


if(s.find("where")==-1):#no where clause,just select * from abc;
	begindex=s.find("from")+5
	fromattr=s[begindex:-2]
	fromattr1=fromattr.split(",")
	print "fromattr1=",fromattr1
	display()
else:
	begindex=s.find("from")+5
	endindex=s.find("where")-1
	fromattr=s[begindex:endindex]
	fromattr1=fromattr.split(",")
	begindex=s.find("where")+6
	endindex=s.find(";")
	temp=s[begindex:endindex]
	temp=temp.split("and",index);
	arg=[]
	temp1=[]
	temp2=[]

	for i in range(len(temp)):
	        temp1=temp[i].split("or")
        	for j in range(len(temp1)):
                	temp1[j]=temp1[j].strip()
			temp2.append(temp1[j])

	for i in range(len(temp2)):
	        for j in range(len(relop)):
        	        if(temp2[i].find(relop[j])!=-1):
                	        beg=temp2[i].find(relop[j])+len(relop[j])+1
				end=len(temp2[i])
				if(beg>end):#to check for cases such as a<
					flag=0
					print "invalid where clause"
					sys.exit(1)
				else:
					flag=1
	                        	arg.append(temp2[i])#if everything is valid in the where clause
	                        break
        	        else:
                	        flag=0
                        	continue
	if flag!=1:
        	print "invalid where clause."
	        sys.exit(1)
	else:
		display()
