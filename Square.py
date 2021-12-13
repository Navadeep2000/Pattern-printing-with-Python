def fill(value):  # This function returns a true value, saying the square is filled or a hollow one
    if value:
        return True  # This returns False value, denoting the square is a HOLLOW
    else:
        return False  # This returns a True value, denoting the square is FILLED


def square(size, character, Truth):  # Defining a common function for printing a square of size 'size'
    if Truth:
        for i in range(size):
            for j in range(size):
                print(character, end=' ')
            print()
    else:
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(character, end=' ')
                else:
                    print(end='  ')
            print()


# Main function
length = int(input(" Enter length of the square :       "))  # Example : A 4x4 matrix is a square of length 4
print("Select 0 for HOLLOW and 1 for FILLED")
select = int(input(" Enter fill status '0' or '1'  :    "))
CharFill = input(" Enter a common character to fill : ")
square(length, CharFill, fill(select))
