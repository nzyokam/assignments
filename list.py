my_list = []

my_list.append(40)
my_list.append(20)
my_list.append(10)
my_list.append(30)

print(my_list)  
my_list.insert(1, 15)
print(my_list)  

my_list.extend([70, 60, 50])
print(my_list)  
my_list = sorted(my_list, key=int)

print(my_list)  

index_of_30 = my_list.index(30) 
print(index_of_30)