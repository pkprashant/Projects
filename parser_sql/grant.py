import sys
privileges=["ALL","SELECT","INSERT","UPDATE","DELETE","REFERENCES","USAGE"]
#temporary=raw_input("please enter the sql statement:\n")
#temporary=temporary.splitlines()
f=open("input.txt",'r')
temporary=f.read()
#to handle multiline inputs
temporary=temporary.splitlines()
s=""
for i in range(len(temporary)):
    temporary[i]=temporary[i].strip()
    s=s+temporary[i]+" "
s=s.upper()
s=s.strip()

if(s.find("GRANT")!=-1 and s[-1]==";"):
    s1=s.split(" ")
    if(s1[1] in set(privileges) and s1[2]=="ON" and s1[4]=="TO"):
        databaseName=s1[3]
        index=s.find("TO")+3
        temp=s[index:-1].split(" ")
        userList=temp[0].split(",")
        print databaseName
        print userList
	print "TCL"
	print "|\n|\n|\n|\nGRANT"
	print "|\n|\n|\n|\n--------",s1[1],"\n|\t|\n|\t|\n|\t|\n|\t--------",databaseName
	for i in range(len(userList)):#to handle multi user input
		print "|\n|\n|\n|\n--------",userList[i]
		if(i!=(len(userList)-1)):
			print "|\n|\n|\n|\n--------','"
	print "|\n|\n|\n|\n--------';'"
    else:
	print "invalid syntax"
	sys.exit(1)
else:
    print "invalid syntax"
    sys.exit(1)
