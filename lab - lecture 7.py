# 1. Will the code run, & if so, what will be the data types & values of a & b?
a, b = [10, 11]
print("a & b's types are:", type(a), "&", type(b))
print("a & b's values are:", a, "&", b) 
# Yes, a & b are both integers.  a = 10, b = 11.  

a, b = [10]
# No, the # of variables on the L of the "=" are not balanced w/ the # of values on the R.  

a, b = [10, 11, 12]
# No, the # of variables on the L of the "=" are not balanced w/ the # of values on the R.  

a, *b = [10, 11]
# Yes, a is an integer & b is a list.  a = 10, b = [11]. 

a, *b = [10]
# Yes, a is an integer & b is a list.  a = 10, b = [].  

a, *b = [10, 11, 12]
# Yes, a is an integer & b is a list.  a = 10, b = [11, 12].   

# 2. What data type is args & kwargs inside the function, what are the values,
# and how would you use them?
def base_function(*args, **kwargs):
    print("args & kwarg's types are:", type(args), "&", type(kwargs))
    print("args & kwarg's values are:", args, "&", kwargs) 
    pass

base_function()
base_function(['A', 'B'])
base_function('Hello', 'World', '!')
base_function(answer=True, question='No')
base_function('a', 'b', c='value', d=10)
# The args are always put into a tuple, and the kwargs are always put into a dictionary.
# The values are as listed by the print statements.  The first three function calls
# result in empty kwarg dictionaries.  The fourth results in an empty arg tuple.
# The last populates both the arg tuple & the kwarg dictionary.

# 3. Write a lambda function that is passed into my_func, & performs a valid
# operation on a & b, without editing the contents of my_func at all.

def my_func(a, b, func=lambda a, b: (a+b) / (a-b)):
    value = func(a, b)
    return value

x = my_func(5,7)
print(x)
