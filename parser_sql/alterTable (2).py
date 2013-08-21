import string
import sys
attributes=[]
dataTypes=[]
validDataTypes=["CHARACTER","NUMERIC","DECIMAL","DATE","TIME","TIMESTAMP","DATETIME","YEAR","CHAR","INTEGER","SMALLINT","FLOAT","REAL"]
modifiers=["ADD","MODIFY","DROP","RENAME"]
tableConstraints=["UNIQUE","PRIMARY KEY","FOREIGN KEY","CHECK","NOT NULL"]


#input from file
f=open("input.txt",'r')
temporary=f.read()

#to convert multi-line inputs to a single line.
temporary=temporary.splitlines()
s=""
for i in range(len(temporary)):
    temporary[i]=temporary[i].strip()
    temporary[i]=temporary[i].lstrip(',')
    temporary[i]=temporary[i].upper()
    s=s+temporary[i]+" "
#s=s.upper()
s=s.strip()

if(s[-1]==";"):
	s=s[:-1].strip()
	s=s[:-1].strip('(')
	print s
else:
	print "Semicolon missing at the end."
	sys.exit(0)
temp=s.split(' ',4) 
'''4 parts atleast must be there in any alter table construct'''
for i in range(len(temp)):
	temp[i]=temp[i].strip()
	temp[i]=temp[i].strip('(')
print temp

if(temp[0]=="ALTER" and temp[1]=="TABLE"):
    tableName=temp[2]
    if(temp[3]=="RENAME"):  
        construct=s.split(" ")
        print construct
        if(construct[4]=="TO" and len(construct)==6):
            print "ALTER TABLE\n\t|\n\t|\n\tRENAME\n\t|\n\t|"
	    print "\t",tableName,"----TO----",construct[5]
	    print "\t|\n\t|\n\t|\n\t----';'"
	else:
	    print "invalid rename clause."
            sys.exit(1)


    elif(temp[3]=="DROP"):
        construct=s.split(" ")
        if(construct[4]=="COLUMN" and len(construct)==6):
           print "ALTER TABLE\n\t|\n\t|\n\tDROP\n\t|\n\t|\n\t",tableName,"---------",construct[5]
	   print "\t|\n\t|\n\t|\n\t----';'"
	else:
           print "invalid drop clause."
	   sys.exit(1)


    elif(temp[3]=="ADD"):
        if(s.find("(")==-1):
           construct=s.split(" ")
           if((construct[5] in set(validDataTypes)) and len(construct)==6):
               print "ALTER TABLE\n\t|\n\t|\n\tADD\n\t|\n\t|\n\t",tableName,"---------",construct[5]
	       print "\t|\n\t|\n\t|\n\t----';'"
	   else:
		print "The datatype may not be valid or the table name may not be mentioned"
		sys.exit(0)
        else:
            s1=s[s.find('(')+1:s.rfind(")")]
	    print s1
            eleList=s1.split(',')
            print "the element list is",eleList
            for i in range(len(eleList)):
            #separate the attribute name and datatype and store it into dType list deleting the trailing and leading blank spaces
                eleList[i]=eleList[i].strip();
                dType=eleList[i].split(" ")
            #check if the attribute's datatype is in the mentioned set of datatypes
                if(dType[1] in set(validDataTypes)):
                    attributes.append(dType[0])
                    dataTypes.append(dType[1])
                else:
                    print "Invalid datatype"
                    sys.exit(1)
	    print "ALTER TABLE\n\t|\n\t|\n\t",tableName,"\n\t|\n\t|\n\tADD--------"
	    for i in range(len(attributes)):
		print "\t\t|\n\t\t|\n\t\t|"
		print "\t\t----",attributes[i],"----",dataTypes[i]
		if(i!=(len(attributes)-1)):
			print "\t\t|\n\t\t|\n\t\t|"
			print "\t\t----','"
	    print "\t\t|\n\t\t|\n\t\t|"
	    print "\t\t----';'"
	    #print "\t|\n\tTO----------",s[s.rfind(")")+5:-2]


    elif(temp[3]=="MODIFY"):
        if(s.find("(")==-1):
           construct=s.split(" ",6)
           if(construct[5] in set(validDataTypes)):
                if(len(construct)>6):
                   if(construct[6] in tableConstraints):
                       print "ALTER TABLE\n\t|\n\t|\n\tMODIFY\n\t|\n\t|\n\t",tableName,"---------",construct[5],"-----';'"
                else:
                   print "ALTER TABLE\n\t|\n\t|\n\tMODIFY"
        else:
            s1=s[s.find('(')+1:s.rfind(")")]
            eleList=s1.split(',')
            print "the element list is",eleList
            for i in range(len(eleList)):
            #separate the attribute name and datatype and store it into dType list deleting the trailing and leading blank spaces
                eleList[i]=eleList[i].strip();
                dType=eleList[i].split(" ",2)
            #check if the attribute's datatype is in the mentioned set of datatypes
                if(dType[1] in set(validDataTypes)):
                    attributes.append(dType[0])
                    dataTypes.append(dType[1])
                    if(len(dType)>2):
                        if(dType[2] in tableConstraints):
#                            print "ALTER TABLE\n\t|\n\t|\n\tMODIFY"
			     z=1
                    else:
                        #print "ALTER TABLE\n\t|\n\t|\n\tMODIFY"
			     z=1

		
                else:
                    print "Invalid datatype"
                    sys.exit(1)
	    print "ALTER TABLE\n\t|\n\t|\n\t",tableName
	    print "\t|\n\t|\n\t|\n\tMODIFY"
	    for i in range(len(attributes)):
		print "\t\t|\n\t\t|\n\t\t|"
		print "\t\t----",attributes[i],"----",dataTypes[i]
		if(i!=(len(attributes)-1)):
			print "\t\t|\n\t\t|\n\t\t|"
			print "\t\t----','"
	    print "\t\t|\n\t\t|\n\t\t|"
	    print "\t\t----';'"
        
else:
    print "invalid alter table syntax."


#if anywhere the syntax is invalid it just gives the reason as to why it is invalid and just exits from the code
#the tableName,the names of the attributes(attributes[]),the datatypes of the attributes(dataTypes[]) have all been isolated

