import string
import sys
attributes=[]
dataTypes=[]
validDataTypes=["CHARACTER","NUMERIC","DECIMAL","DATE","TIME","TIMESTAMP","DATETIME","YEAR","CHAR","INTEGER","SMALLINT","FLOAT","REAL"]
tableConstraints=["UNIQUE","PRIMARY","FOREIGN","CHECK"]

f=open("input.txt",'r')
temp=f.read()
temp=temp.splitlines()
s=""
for i in range(len(temp)):
    temp[i]=temp[i].strip()
    temp[i]=temp[i].strip(',')
    temp[i]=temp[i].upper()
    s=s+temp[i]+" "
#s=s.upper()
s=s.strip()
index=s.find("CREATE TABLE")
if((index!=-1) and s[-1]==';' and s[-2]==')'):
    endIndex=s.rfind(')')#finds last occurence of ")"
    index=index+12;
    begindex=index
    s1=s[begindex:endIndex]
    temp.pop(-1)
    temp.pop(0)
    while(s[index]!='('):
        index=index+1
    #isolate the table name
    tableName=s[begindex:index]
    if(tableName==" " or tableName==""):
        print "Table name not specified."
        sys.exit(1)
    else:
        s2=s1[s1.find('(')+1:]
    j=0
    split=s.find("(")+1
    eleList=temp
    print "the element list is",eleList
    for i in range(len(eleList)):
        #separate the attribute name and datatype and store it into dType list deleting the trailing and leading blank spaces
        eleList[i]=eleList[i].strip();
        dType=eleList[i].split(" ",2)
        #check if the attribute's datatype is in the mentioned set of datatypes
        if(dType[0] in set(tableConstraints)):
            k=1
            if((dType[0]=="PRIMARY" or dType[0]=="FOREIGN") and (dType[1]=="KEY")):
                k=2
            dType[k]=dType[k].strip("(")
	    dType[k]=dType[k].strip(")")
            columnNames=dType[k].split(",")
	    for i in range(len(columnNames)):
	        if(columnNames[i] in set(attributes)):
		     print columnNames[i]
        	     j=1
           	else:
		     print columnNames[i]
            	     print "The attribute for table constraint is incorrect."
             	     sys.exit(1)
        else:    
                if(dType[1] in set(validDataTypes)):
                    if(len(dType)>2):
			temp=dType[2].split(" ")
                        if(temp[0] in set(tableConstraints)):
                            if(temp[0]=="PRIMARY" or temp[0]=="FOREIGN"):
                               # temp=dType[2].split(" ")
                                if(temp[1]=="KEY" and len(temp)==2):
                                    attributes.append(dType[0])
                                    dataTypes.append(dType[1])
                                else:
                                    print "invalid table constraints"
                                    sys.exit(1)
                            else:
                                attributes.append(dType[0])
                                dataTypes.append(dType[1])
                        else:
                           print "invalid table constraints"
			   sys.exit(1)
                    else:
                        attributes.append(dType[0])
                        dataTypes.append(dType[1])
                else:
                    print "Invalid datatype",dType[1]
                    sys.exit(1)

else:
    print index,s[-1],s[-2]
    print "Create table syntax incorrect"
    sys.exit(1)
print "The parsed tree is "
print "       DDL"
print "\t|\n\t|\n\t|"
print "CREATE TABLE"
print"\t|\n\t|\n\t|\n\t"
print "\t",tableName.strip()
print"\t\t|\n\t\t|\n\t\t|\n\t\t"
print "\t\t--------'('"
for i in range(len(attributes)):
    print"\t\t|\n\t\t|\n\t\t|\n\t\t|"
    print "\t\t--------",attributes[i],"---",dataTypes[i]
    print"\t\t|\n\t\t|\n\t\t|\n\t\t"
    if(i!=(len(attributes)-1)):
        print "\t\t--------','"
print"\t\t|\n\t\t|\n\t\t|\n\t\t|"
print "\t\t--------')'"
print"\t\t|\n\t\t|\n\t\t|\n\t\t|"
print "\t\t--------';'"
#if anywhere the syntax is invalid it just gives the reason as to why it is invalid and just exits from the code
#the tableName,the names of the attributes(attributes[]),the datatypes of the attributes(dataTypes[]) have all been isolated

