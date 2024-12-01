list1 = [1,2,1]
list2 = [1,2,3]

copy_list2 = list1.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrow")
else:
    print("not palindrow")
