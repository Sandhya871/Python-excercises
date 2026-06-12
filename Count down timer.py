# Example 1
import time 
time.sleep(3)
print("TIME's UP!")

# OUTPUT
pause for 3 sec
TIME's UP!


# Example 2
import time
my_time = int(input("Enter your time in sec: "))
for x in range(0,my_time):
    print(x)
    time.sleep(3)
print("TIME's UP!")

# OUTPUT
pause for 5 sec
Enter your time in sec: 5
0
1
2
3
4
TIME's UP!


# Example 3
import time
my_time = int(input("Enter your time in sec: "))
for x in reversed (range(0,my_time)):
    print(x)
    time.sleep(3)
print("TIME's UP!")

# OUTPUT
pause for 3 sec
Enter your time in sec: 3
2
1
0
TIME's UP!


# Example 4
import time
my_time = int(input("Enter your time in sec: "))
for x in range(my_time,0,-1):
    print(x)
    time.sleep(3)
print("TIME's UP!")

# OUTPUT
pause for 4 seconds
Enter your time in sec: 4
4
3
2
1
TIME's UP!
