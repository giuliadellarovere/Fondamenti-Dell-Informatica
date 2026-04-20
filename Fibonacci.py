import math
from PairingFunction import pairing_function as pair
from PairingFunction import projection_x as proj_1
from PairingFunction import projection_y as proj_2

# FIBONACCI FUNCTION

# Recursive version
def fibonacci_recursive(n):
    if(n == 0 or n == 1):
        return 1;
    else:
        fibo_rec = fibonacci_recursive(n-1) + fibonacci_recursive(n-2);
        return fibo_rec;

# Iterative version
def fibonacci_iterative(n):
    if(n == 0 or n == 1):
        return 1;
    else:
        a = 1;
        b = 1;
        for _ in range(2, n + 1):
            c = a + b;
            a = b;
            b = c;
        return b;

# Using the pair method
def fibonacci_pairing(n):
    # base case
    if(n == 0):
        fibo_1 = 1;
        fibo_2 = 1;
        fibo = pair(fibo_1, fibo_2);
        return fibo;
    # recursive case
    else:
        # fibo(n) = h( fibo(n-1) )
        return h(fibonacci_pairing(n - 1));


# Function h(x) = pair( proj_2, proj_1 + proj_2 )       
def h(x):
    fibo_1 = proj_2(x);
    fibo_2 = proj_1(x) + proj_2(x);
    return pair(fibo_1, fibo_2);  



#----------------------------------------------------------------------------------------------
# TEST
n = int(input("Inserire il valore di n: "));
print("Fibonacci(", n, ") = ", fibonacci_recursive(n));
print();
print("Fibonacci(", n, ") = ", fibonacci_pairing(n));