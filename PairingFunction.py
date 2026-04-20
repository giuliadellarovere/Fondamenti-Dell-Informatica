import math

# Pairing Function
def pairing_function(x, y): # x, y non-negative integers
    k = x + y;
    # formula di pairing_function: (k*k + k)//2 + x, dove k = x + y
    result = math.ceil( (k*k + k)//2 + x );
    return result;

# Inverse Pairing Function 
def inverse_pairing_function(z): # z non-negative integer
    x = 0;
    y = 0;
    if(z == 0):
        return (x, y);
    # formula inversa di pairing_function
    # w = x + y
    # radice quadrata di 8z + 1, meno 1, diviso 2, arrotondato per difetto
    w = math.floor((math.sqrt(8 * z + 1) - 1) / 2);
    # calcolo della base della diagonale
    t = (w**2 + w) // 2; # w**2 è w al quadrato, // è la divisione intera
    # x è la differenza tra z e la base della diagonale
    x = z - t;
    # poiché w = x + y, allora y = w - x
    y = w - x;
    
    return (int(x), int(y));
    
# Proiezione del primo elemento della coppia
def projection_x(z):
    (x, y) = inverse_pairing_function(z);
    return x;

# Proiezione del secondo elemento della coppia
def projection_y(z):
    (x, y) = inverse_pairing_function(z);
    return y;



#-------------------------------------------------------------------------------------------
# TEST
x = int(input("Inserire il valore di x: "));
y = int(input("Inserire il valore di y: "));
z = pairing_function(x, y);
print("La coppia (", x, ",", y, ") è mappata al numero: ", z);
print();
z = int(input("Inserire il valore di z: "));
(x, y) = inverse_pairing_function(z);
print("Il numero ", z, " è mappato alla coppia: (", x, ",", y, ")");
print();
z1 = print("Proiezione del primo elemento della coppia: ", projection_x(z));
z2 = print("Proiezione del secondo elemento della coppia: ", projection_y(z));