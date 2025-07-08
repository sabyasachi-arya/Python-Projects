def fibonacci():  # A function where Fibonacci sequence formula will be executed
    n = int(input(f"Enter a number upto which Fibonacci sequence will be shown : "))
    # "n" is a variable in which the user will be asked to enter a number
    # upto which Fibonacci seq will be printed out
    if n >= 2:  # if n is greater than 2 then execute the Fibonacci Sequence
        (a, b) = (0, 1)  # Assigning the starting numbers into two variables taking in as a tuple
        print(a)    # Printing the first number
        while b <= n:  # While b is less than or equal to user input the Fibonacci sequence will be executed
            # If the b becomes greater than n in the process then the function will stop executing sequence upto n
            # (beginning of the loop)
            print(b)  # Printing the second number in sequence, and only printing the 'b' is in the loop
            (a, b) = (b, a + b)  # after printing b the new value of 'a' is now 'b' and the new value of 'b'
            # is a + b, and the value replacement is getting done in the same line for both variable
            # because if we assign the value one after another like: a = b and b = a + b
            # the 'a' will equal to 'b' and when we will try to assign
            # 'b's value to 'a + b' then it will be 'b + b' because 'a' is already 'b'
            # so here we are using a and b as a tuple to replace their values,
            # because it is a loop everytime 'b' gets a new value from the line:12: (a, b) = (b, a + b)
            # it gets printed out as an extension of the sequence but 'a' does not get printed everytime when
            # loop runs because 'print(a)' is outside of the loop. So, it gets printed out once.

    else:
        print("User input has to be greater than 2 to execute the Fibonacci Sequence.")
        # If user puts value less than 2 then this string gets printed out


fibonacci()  # Calling the function
