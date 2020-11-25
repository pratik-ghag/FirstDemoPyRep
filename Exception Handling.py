a = 5
b = 2
try:
    print("Resource Open")
    print(a/b)
    k = int(input("Enter a Number : "))
    print(k)
except ZeroDivisionError as e:
    print("Can't divide by Zero : ", e)

except ValueError as e:
    print("Invalid Input : ", e)

except Exception as e:
    print("Something went Wrong")

finally:
    print("Resource Close")