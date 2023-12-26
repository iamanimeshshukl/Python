#Exception Handling in Python


try:
    x = int(input("Enter your age-"))
    print("Your Age is-",x)
except Exception as e:
    print("Something is wrong",e)


