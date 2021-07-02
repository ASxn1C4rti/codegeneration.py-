# Import
import time
import random
from time import sleep as time_per_word
import sys

# Username input and availability
username=input("[System] username:")
time.sleep(1)
print ("[System] username:available")
time.sleep(0.6)
print ("[System] username:saved as",username)
time.sleep(0.6)

# Usercode generation
user_random = random.randint(1,1000)
user_code = sys.getsizeof(username) * user_random
print ("[System] usercode:hasfcd"+str(user_code))
time.sleep(0.6)
