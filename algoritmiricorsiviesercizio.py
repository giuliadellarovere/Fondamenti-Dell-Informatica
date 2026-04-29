# Generare i codici dei seguenti Insiemi Ricorsivi
# 1) {x : x è un numero pari}
# 2) {x : x è un numero dispari}
# 3) {x : x è un numero primo}
# 4) {x : x è una potenza di 2}
# 5) {x : Mx ha meno di 5 stati} con Mx che è una macchina di Turing che accetta x


# 1) funzione che restituisce True se x è un numero pari, False altrimenti
def is_even(x):
    n = 1 - mod(x, 2);
    if(n == 1):
        return True;
    else:
        return False;
#--------------------------------------------------------------------------------------
# modulo 
def mod(y, x):
    if(y == 0):
        return 0;
    elif(x == 0 or x == 1):
        return y; # se x = 0 o x = 1, allora mod(y, x) = y per ogni y in N
    else:
        mod_prec= mod(y-1, x);
        modulo = (mod_prec + 1) * sign(x - (mod_prec + 1));
        return modulo;

# segno
def sign(x):
    if(x == 0):
        return 0;
    else:
        return 1;
#---------------------------------------------------------------------------------------

# 2) funzione che restituisce True se x è un numero dispari, False altrimenti
def is_odd(x):
    n = 1 - mod(x, 2);
    if(n == 0):
        return True;
    else:
        return False;

# 3) funzione che restituisce True se x è un numero primo, False altrimenti
def is_prime(x):
    if(x < 2):
        return False;
    else:
        for i in range(2, x):
            if(mod(x, i) == 0):
                return False;
        return True;

# 4) funzione che restituisce True se x è una potenza di 2, False altrimenti
def is_power_of_2(x):
    if(x < 1):
        return False;
    else:
        while(mod(x, 2) == 0):
            x = x // 2;
        if(x == 1):
            return True;
        else:
            return False;

# 5) funzione che restituisce True se Mx ha meno di 5 stati, False altrimenti
# E' una funzione ricorsiva perchè limito superiormente il numero delle iterazioni dell'if.
# Quindi l'algoritmo termina sempre dopo un numero finito di iterazioni.
def has_few_states(Mx):
    if(num_states(Mx) < 5):
        return True;
    else:
        return False;

def num_states(Mx):
    # questa funzione dovrebbe restituire il numero di stati della macchina di Turing Mx
    # ma non è possibile implementarla in modo ricorsivo, quindi la lasciamo come una funzione primitiva
    pass;


# *******************************************************************************************
# TEST
print("TEST INSIEMI RICORSIVI");
print("is_even(4) = ", is_even(4)); # True
print("is_even(5) = ", is_even(5)); # False
print("is_odd(4) = ", is_odd(4)); # False
print("is_odd(5) = ", is_odd(5)); # True
print("is_prime(1) = ", is_prime(1)); # False
print("is_prime(2) = ", is_prime(2)); # True
print("is_prime(3) = ", is_prime(3)); # True
print("is_prime(4) = ", is_prime(4)); # False
print("is_power_of_2(1) = ", is_power_of_2(1)); # True
print("is_power_of_2(2) = ", is_power_of_2(2)); # True
print("is_power_of_2(3) = ", is_power_of_2(3)); # False
print("is_power_of_2(4) = ", is_power_of_2(4)); # True
print("is_power_of_2(5) = ", is_power_of_2(5)); # False