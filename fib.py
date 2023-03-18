# Fibonacci Sequencer

# Input Function
def input_func():
    user_input = int
    correct = False
    while not correct:
        try:
            user_input = int(input("""Fibonacci Sequence Calculator 
            Please enter number of iterations: """))
            correct = True
        # Error on wrong input
        except Exception as error:
            print(f"Error Code : {error}")
            print("Please enter a Whole Number Integer for iterations: """)
    return user_input


# Main Function
def main():
    # Check for correct input
    iterations = input_func()

    # Begin Sequencing Fibonacci
    fib = []
    # Begin Iteration through range
    for i in range(iterations):
        if i == 0:
            fib.append(0)
        elif i == 1:
            fib.append(1)
        else:
            fib.append(fib[i-1] + fib[i-2])
    print(f"{fib}")


# Check Script for Main
if __name__ == "__main__":
    main()
