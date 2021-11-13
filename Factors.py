
dict={}
b=[]

for i in range(1,100):
    for j in range(1,i+1):

        if i%j==0:
            b.append(j)
            dict[i]=b
    b = []
print(dict)


