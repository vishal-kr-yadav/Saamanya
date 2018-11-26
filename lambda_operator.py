# The lambda operator or lambda function is a way to create small anonymous functions,
# i.e. functions without a name.

# Lambda functions are mainly used in combination with
# the functions filter(), map() and reduce().

# The general syntax of a lambda function is quite simple:
# lambda argument_list: expression

f = lambda x, y : x + y
# print(f(1,1))

# map function

def fahrenheit(T):
    return ((float(9)/5)*T + 32)
temp = (36.5, 37, 37.5,39)

F = map(fahrenheit, temp)
print(F)