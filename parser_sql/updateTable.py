import sys
import string
print "Enter the sql query:-"
#s=raw_input()
f=open("input.txt",'r')
temp=f.read()
temp=temp.splitlines()
s=""
for i in range(len(temp)):
	temp[i]=temp[i].strip()
	s=s+temp[i]+" "
s=s.strip()
relop=["=","<",">","<=",">=","<>","between","like","in"]
if (s.find("update")==0 and s[-1]==";"):
	z=1
else:
	print "wrong syntax"
	sys.exit(0)
begindex=s.find("update")+7
endindex=s.find("set")-1
str1 = s[begindex:endindex]
x=s.find("set",(endindex+1),(endindex+4))
set1=[]
if (x!=-1):
	begindex=x+4;
	y=(s.find("where"))
	if(y!=-1):
		endindex=y-1
	else:
		print "no where clause"
		sys.exit(1)
	index=begindex
	while(index<=endindex):
		index=index+1
		if ((s[index]==" ")|(s[index]==",")):
			s1=s[begindex:index]
			set1.append(s1)
			begindex=index+1
index=s.find("where")+5
temp=s[index:-1]
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
			if(beg>end):
				flag=0
				print"invalid where."
				sys.exit(1)
			else:
				flag=1	
				arg.append(temp2[i])
			break
		else:
			flag=0
			continue
if flag!=1:
	print "invalid where clause."
	sys.exit(1)
print "DML"
print "|\n|\n|\n|"
print "UPDATE"
print "\t|\n\t|\n\t|\n\t"
print "\t",str1.strip()
print "\t|\n\t|\n\t|\n\t"
print "\tSET-------------"
for i in range(len(set1)):
	print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
	print "\t|\t\t--------",set1[i]
	if(i!=(len(set1)-1)):
		print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
		print "\t|\t\t--------','"
print "\tWHERE-----------"
for i in range(len(arg)):
	print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
        print "\t|\t\t--------",arg[i]
	if(i!=(len(set1)-1)):
		print"\t|\t\t|\n\t|\t\t|\n\t|\t\t|\n\t|\t\t|"
		print "\t|\t\t--------','"
print "\t--------';'"

