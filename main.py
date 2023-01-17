#arb_args - Takes in any number of arguments and prints them one at a time.
def arb_arg (* args):
  for i in (args):
    print(i)
#inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_funct(a,b):
  def nest_1():
    return a * b
  def nest_2():
    return a / b
  print(nest_1()+nest_2())
#lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(student_name, lunch_preference):
  print(student_name, lunch_preference)
#sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(x,y):
  return x+y,x*y
#alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
#arb_mean - Accepts any number of integers and prints their average.
#arb_longest_string - Accepts any number of strings and returns the longest one.