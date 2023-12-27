import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Create your own decorator function to measure the amount of seconds that a function takes to execute
# complete the code exercise by printing out the time it takes to run the fast_function() vs the slow_function(). 
# You will need to complete the speed_calc_decorator() function.
# Write your code below 👇

def speed_calc_decorator(function):
  def wrapper():
    start_time = time.time()
    function()
    end_time = time.time()
    print(f"{function.__name__} run speed: {end_time - start_time}s")
  return wrapper

@speed_calc_decorator
def fast_function():
  for i in range(1000000):
    i * i

@speed_calc_decorator
def slow_function():
  for i in range(10000000):
    i * i

fast_function()
slow_function()