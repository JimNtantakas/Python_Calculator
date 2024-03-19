#import re

def calculations(mylist):  # function that makes simple computations with +,-,* (without parentheses)
    i=0    
    while i<len(mylist):
        if mylist[i]=='*':
            mylist[i-1]=str(float(mylist[i-1])*float(mylist[i+1]))
            mylist.pop(i)
            mylist.pop(i)
        elif mylist[i]=='/':
            mylist[i-1]=str(float(mylist[i-1])/float(mylist[i+1]))
            mylist.pop(i)
            mylist.pop(i)
        else:
            i+=1          
    i=0
    while i<len(mylist):
        if mylist[i]=='+':
            if i==0 or mylist[i-1]=='(' :
                mylist.pop(i)
            else:
                mylist[i-1]=str(float(mylist[i-1])+float(mylist[i+1]))
                mylist.pop(i)
                mylist.pop(i)
        elif mylist[i]=='-':
            if i==0 or mylist[i-1]=='(' :
                mylist[i+1]=str(float(mylist[i+1])*(-1))
                mylist.pop(i)
            else:
                mylist[i-1]=str(float(mylist[i-1])-float(mylist[i+1]))
                mylist.pop(i)
                mylist.pop(i)     
        else:
            i+=1
    return mylist[0]


def calculate(s):
    start=[]
    s=s.replace(" ","")
    if ('+' not in s) and ('-' not in s) and ('*' not in s) and ('(' not in s) and ('/' not in s):
        return s
    
    #s = re.findall(r'\d+|\D', s)   
    #Convert the string into a list ,for example "4123+8*9  --> ["4123","+","8","*","9"] ,and this is the format we need to calculate the result
    i=0
    string=""
    s2=[]
    mylist=[]
    while i<len(s)-1:
        if (s[i].isdigit() and (s[i+1].isdigit() or s[i+1]=='.')) or s[i]=='.':
            mylist.append(s[i])
        else:
            for z in range(len(mylist)):
                string+=mylist[z]
            string+=s[i]
            #print(string)
            s2.append(string)
            string=""
            mylist=[]
        i+=1
    s=s2[:]
    
    start=[]
    j=0
    while j<len(s):
        if s[j]=='(':
            start.append(j)
            j+=1
        elif s[j]==')':
            end=j
            distance=end-start[-1]
            s[start[-1]]=calculations(s[start[-1]+1:end])
            for i in range(distance):
                s.pop(start[-1]+1)
                j-=1        
            start.pop(len(start)-1)
        else:
            j+=1
    return calculations(s)
