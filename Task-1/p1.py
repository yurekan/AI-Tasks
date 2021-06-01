import os

txtfile = input("Enter the name of textfile : ")
if os.path.isfile(txtfile):
    with open(txtfile,'r') as fobj:
        for num in fobj:
            numlist = num.split()
            for i in range(len(numlist)):
                numlist[i]=int(numlist[i])
            num_min = numlist[0]
            num_max = numlist[0]
            avg = total = 0
            for i in range(len(numlist)):
                if num_min > numlist[i]:
                    num_min = numlist[i]
            for j in range(len(numlist)):
                if num_max < numlist[j]:
                    num_max = numlist[j]
            for k in range(len(numlist)):
                total += numlist[k]
            avg = total/len(numlist)
            print("The minimum element is given by : ",num_min)
            print("The maximum element is given by : ",num_max)
            print("The average of all the elements is given by : ",avg)
else:
    print("File not found")