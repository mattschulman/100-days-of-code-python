import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Create your own decorator function to measure the amount of seconds that a function takes to execute
# complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function(). 
# You will need to complete the speed_calc_decorator() function.
# Write your code below 👇

def fast_function():
  for i in range(1000000):
    i * i

def slow_function():
  for i in range(10000000):
    i * i
