from hashing import *

h = customhash

int_val = 4
str_val = 'PythonIsBest'
flt_val = 24.56


print('The integer hash value is when using custom hash func:' + str(h(int_val)))
print('The integer hash value is when using custom hash func:' + str(h(str_val)))
print('The integer hash value is when using custom hash func:' + str(h(flt_val)))
print ("The integer hash value is : " + str(hash(int_val))) 
print ("The string hash value is : " + str(hash(str_val))) 
print ("The float hash value is : " + str(hash(flt_val)))
