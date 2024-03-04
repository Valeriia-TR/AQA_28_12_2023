#import lesson9.arithmetic as module
#from lesson9.arithmetic import *
#from lesson9.folder_1.folder_2.folder_3 import arithmetic1
#from lesson9.arithmetic1 import my_sum, my_difference
#from lesson9.folder_1.folder_2.folder_3.arithmetic1 import my_sum as sum1
#from lesson9.folder_1.folder_2.folder_3.arithmetic2 import my_sum as sum2

bubba_salary = 200
uga_buga = 100

#print(module.my_sum(bubba_salary,uga_buga))
#print(my_sum(bubba_salary,uga_buga))
#print(arithmetic1.my_sum(bubba_salary, uga_buga))
#print(sum1(bubba_salary, uga_buga))
#print(sum2(bubba_salary,uga_buga, 300))

from lesson9 import my_sum, very_important_func
print(my_sum(bubba_salary,uga_buga))
very_important_func()

from lesson9.another_dir.another_one_directory.application import my_sum as another_sum
print(another_sum(bubba_salary,uga_buga))
