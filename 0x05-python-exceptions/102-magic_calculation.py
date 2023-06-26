#!/usr/bin/python3
#!/usr/bin/python3

def magic_calculation(a, b):
    result = 0  # Initialize the result variable
    for i in range(1, 3):  # Iterate over the range from 1 to 2 (exclusive)
        try:
            if i > a:
                raise Exception("Too far")  # Raise an exception if i is greater than a
            else:
                result += (a ** b) / i  # Perform a mathematical calculation and add the result to 'result'
        except:
            result = b + a  # If an exception is caught, set 'result' to the sum of b and a
            break  # Exit the loop
    return result  # Return the final result
