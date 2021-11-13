
##################### 1)program #######################
print("Calculator")
print("1.Addition(+)")
print("2.Substraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Percentage(%)")
a=input("What You want To Perform:")
if(a=='1')or(a=='add'):
    print("Addition")
    c=float(input("Enter First No.:"))
    d=float(input("Enter Second No."))
    print("Resul:t" ,c+d)
elif(a=='2')or(a=='sub'):
    print("Substraction")
    c=float(input("Enter First No.:"))
    d=float(input("Enter Second No.:"))
    print("Result:" ,c-d)
elif(a=='3')or(a=='mul'):
    print("Multiplication")
    c=float(input("Enter First no.:"))
    d=float(input("enter Second No.:"))
    print("Result:" ,c*d)
elif(a=='4')or(a=='div'):
    print("Division")
    c=float(input("Enter First No.:"))
    d=float(input("Enter Second No.:"))
    print("Result:" ,c/d)
elif(a=='5')or(a=='per'):
    print("Percentage")
    total=float(input("Enter First No.:"))
    obt=float(input("Enter Second No.:"))
    if(total>=obt):
        per=(obt/total)*100
        print(per)
    else:
        print("Check Your Value")
    
else:
    print("Invalid!!!!!!")



'''
################ 2) Program ###########################
print("Calculator")
print("1.Addition(+)")
print("2.Substraction(-)")
print("3.Multiplication(*)")
print("4.Division(/)")
print("5.Percentage(%)")
a1=('1','add','Add','ADD','addition','Addition','ADDITION','+')
a2=('2','sub','Sub','SUB','substraction','Substraction','SUBSTRACTION','-')
a3=('3','mul','Mul','MUL','multiplication','Multiplication','MULTIPLICATION','*')
a4=('4','div','Div','DIV','division','Division','DIVISION','/')
a5=('5','per','Per','PER','percentage','Percentage','PERCENTAGE','%')
b=input("What You want To Perform:")
if(b in a1):
    print("Addition")
    n1=float(input("Enter First No.:"))
    n2=float(input("Enter Second No.:"))
    print("Result:" ,n1+n2)
elif(b in a2):
    print("Substraction")
    n1=float(input("Enter First No.:"))
    n2=float(input("Enter Second No.:"))
    print("Result:" ,n1-n2)
elif(b in a3):
    print("Multiplication")
    n1=float(input("Enter First No."))
    n2=float(input("Enter Second No."))
    print("Result:" ,n1*n2)
elif(b in a4):
    print("Division")
    n1=float(input("Enter First No.:"))
    n2=float(input("Enter second No.:"))
    print("Result:" ,n1/n2)
elif(b in a5):
    print("Percentage")
    n1=float(input("Enter First No.:"))
    n2=float(input("Enter second No.:"))
    print("Result:" ,(n1/n2)*100)
else:
    print("Invalid!!!!!!!!")
'''    







































