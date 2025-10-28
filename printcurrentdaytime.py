from datetime import datetime
#function that return current day time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

#print timesstamp to see how how long sections of codetakje to run

first_name = "Sergio"
print_time("printed first name")
print(first_name)

for x in range (0,10):
    print(x)
print_time("completed for loop")