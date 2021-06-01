import os

txtfile1 = "Merge1.txt"
txtfile2 = "Merge2.txt"
txtfile3 = "Merge3.txt"
if os.path.isfile(txtfile1) and os.path.isfile(txtfile2):
    with open(txtfile1,'r') as fobj1:
        with open(txtfile2,'r') as fobj2:
            with open(txtfile3,'w') as fobj3:
                for i in fobj1:
                    list1=i.split()
                for j in fobj2:
                    list2=j.split()
                final_list=list1+list2
                for i in range(len(final_list)):
                    final_list[i]=int(final_list[i])
                final_list.sort()
                print("The sorted list is given by : ",final_list)
                for k in range(len(final_list)):
                    fobj3.write(str(final_list[k]) + ' ')
else:
    print("The files does not exist")