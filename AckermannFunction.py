import random

# FUNZIONE DI ACKERMANN
def A(x, y):  # x, y non-negative integers
    if(x == 0):
        return (y + 1);
    elif(x > 0 and y == 0):
        return A(x-1, 1);
    else:
        ackermann = A(x-1, A(x, y-1));
        return ackermann;       


# TEST
x = int(input("Inserire il valore di x: "));
y = int(input("Inserire il valore di y: "));
print("A(", x, ",", y, ") = ", A(x, y));

# --------------------------------------------------------------------------------------------
# COMMENTI

# Provare a far computare A(5,5) ha fatto "esplodere" Python, che ha restituito l'errore: 
# ! RecursionError: maximum recursion depth exceeded !
# Questo perchè la funzione di Ackermann è una delle funzioni più esplosive 
# che esistano in matematica

# CRESCITA ESPLOSIVA
# x = 0 and y = n  -->  A(0, n) = n + 1 crescita lineare
# x = 1 and y = n  -->  A(1, n) = n + 2 crescita lineare
# x = 2 and y = n  -->  A(2, n) = 2n + 3 crescita lineare
# x = 3 and y = n  -->  A(3, n) = 2^(n + 3) - 3 crescita esponenziale

# Python va in CRASH da A(3,7) in poi, 
#   perchè A(3,7) = 2^(7 + 3) - 3 = 2^10 - 3 = 1021, 
#   che è un numero troppo grande

# x = 4 and y = n  -->  A(4, n) = 2^(2^(n + 3) - 3) - 3 crescita doppia esponenziale
# x = 5 and y = n  -->  A(5, n) = 2^(2^(2^(n + 3) - 3) - 3) - 3 crescita tripla esponenziale