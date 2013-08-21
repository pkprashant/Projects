from sys import *
#s=raw_input("Enter sql statement\n")
f=open("input.txt",'r')
s=f.read()
s=s.upper()
s=s.strip()
#check for ';'
if(s[-1]==';'):
    temp=s[:-1].strip().split(" ")
else:
    print "Invalid commit syntax"
    sys.exit(1)
if(temp[0]=="COMMIT"):
    if(len(temp)==2):
        if(temp[1]=="WORK"):
            print "TCL\n|\n|\n|\n|\nCOMMIT\n|\n|\n|\n----WORK"
	    print "|\n|\n|\n----;"
        else:
            print "Invalid syntax\n"
    elif(len(temp)==1):
        print "TCL\n|\n|\n|\n|\nCOMMIT"
	print "|\n|\n|----;"
    else:
        print "Invalid syntax\n"
else:
    print "Invalid syntax\n"
