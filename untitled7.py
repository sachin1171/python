list1=[0,1,2,3,4,5,6,7,8,9]
list2 = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
print ("Original key list is : " + str(list2))
print ("Original value list is : " + str(list1))
res = {}
for key in list2:
    for value in list1:
        res[key] = value
        list1.remove(value)
        break 
print ("Resultant dictionary is : " +  str(res))




list(range(1,10,2))
