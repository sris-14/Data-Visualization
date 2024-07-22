# program to handle ZeroDivisionError exception when dividing by zero
print("Line 1")
print("Line 2")

try:
    print(100/0)

except ZeroDivisionError as e:
    print(e)  
     
print("Line 3")
print("Line 4")