import os

txtfile1 = 'F1.txt'
txtfile2 = 'F2.txt'
txtfile3 = 'F3.txt'

with open(txtfile1,'r') as fobj1:
    with open(txtfile2,'r') as fobj2:
        with open(txtfile3,'r+') as fobj3:
            i=0
            j=0
            x=fobj1.read()
            y=fobj2.read()
            while i<len(x) or j<len(y):
                if i<len(x):
                    while x[i]!=' ':
                        word1=''
                        word1 += x[i]
                        fobj3.write(x[i])
                        i+=1
                        if i>=len(x):
                            break
                    fobj3.write(' ')
                    i+=1
                if j<len(y):
                    while y[j]!=' ' and y[j]!='':
                        word2=''
                        word2 += y[j]
                        fobj3.write(y[j])
                        print(y[j])
                        j+=1
                        if j>=len(y):
                            break
                    fobj3.write(' ')
                    j+=1
                
                

