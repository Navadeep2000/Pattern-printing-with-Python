# Initialising number of rows in the triangle
N = int(input("Enter number of rows needed in the triangle: "))

# Printing the upper triangle
'''
* * * * *
* * * * 
* * *
* *
*
'''

for i in range(N):
    for j in range(N):
        if i <= j:
            print('*', end=' ')  # This print statement prints '*' if the 'if' condition is satisfied
    print()  # This print statement helps in adding a next line character as it exits the 'j' loop

# Printing the lower triangle
'''
*
* *
* * *
* * * *
* * * * *
'''

for i in range(N):
    for j in range(N):
        if i >= j:
            print('*', end=' ')  # This print statement prints '*' if the 'if' condition is satisfied
    print()  # This print statement helps in adding a next line character as it exits the 'j' loop

# Printing the upper triangle in matrix form
'''
* * * * *
  * * * *
    * * *
      * *
        *
'''
print("\n")
for i in range(N):
    for j in range(N):
        if i <= j:
            print('*', end=' ')  # This print statement prints '*' if the 'if' condition is satisfied
        else:
            print(end='  ')
    print()  # This print statement helps in adding a next line character as it exits the 'j' loop

# Printing the upper triangle in matrix form
'''
        *
      * *
    * * * 
  * * * *
* * * * *
'''
for i in range(1, N+1):
    for j in range(1, N+1):
        if abs(i + j) > N:
            print('*', end=' ')  # This print statement prints '*' if the 'if' condition is satisfied
        else:
            print(' ', end=' ')
    print()  # This print statement helps in adding a next line character as it exits the 'j' loop
