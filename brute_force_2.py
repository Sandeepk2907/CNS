import itertools
import string
import time
def bruute_force(target_password,length):
    start_time=time.time()
    
    charset=string.ascii_letters + string.digits + string.punctuation
    for l in range(1,length+1):
        for attempt in itertools.product(charset,repeat=l):
            attempt_password="".join(attempt)
            print(f"Trying password :{attempt_password}")
            
            if attempt_password==target_password:
                end_time=time.time()
                print("\n Password Found")
                print(f"Password {attempt_password}")
                print(f"Time Taken :{end_time-start_time:.2f}seconds")
                return attempt_password
    print("\nPassword not found within the maximum length.") 
    return None
target_password = "sandeep"
length = 11
bruute_force(target_password,length)
                      