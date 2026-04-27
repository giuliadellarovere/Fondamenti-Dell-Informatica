# FUNZIONI PRIMITIVE RICORSIVE
# Insieme delle funzioni che si possono costruire a partire dalla
# composizione o ricorsione primitiva di funzioni di base


# FUNZIONI DI BASE

# per ogni x in N --> zero(x) = 0
def zero(x):
    return 0;

# per ogni x in N --> succ(x) = x + 1
def succ(x):
    return x + 1;

# per ogni n in N (n >= 1) e per ogni i in {1, ..., n} --> proj(n, i)(x1, ..., xn) = xi
def proj(n, i, *args):
    if(i < 1 or i > n):
        raise ValueError("i deve essere compreso tra 1 e n");
    return args[i - 1]; # python è 0-indexed, quindi args[i - 1] restituisce 
                        # l'i-esimo elemento (1-indexed) della tupla args  


# REGOLE DI COMPOSIZIONE E RICORSIONE PRIMITIVA  

# composizione di funzioni
# f(x1, ...., xk) = h( g1(x1, ..., xk), g2(x1, ..., xk), ..., gk(x1, ..., xk) )
def comp(g, h):
    def composed_function(*args):
        g_results = [g_i(*args) for g_i in g];  # calcola g1(args), g2(args), ..., gk(args)
        return h(*g_results);                   # chiama h con i risultati di g come argomenti
    return composed_function;
    
# ricorsione primitiva
# f(x1, ..., xk, 0) = g(x1, ..., xk)
# f(x1, ..., xk, y + 1) = h(x1, ..., xk, y, f(x1, ..., xk, y))
def prim_rec(g, h):
    def recursive_function(*args):
        if args[-1] == 0:  # caso base: l'ultimo argomento è 0
            return g(*args[:-1])  # chiama g con tutti gli argomenti tranne l'ultimo
        else:  # caso ricorsivo: l'ultimo argomento è y + 1
            y = args[-1] - 1  # calcola y
            recursive_result = recursive_function(*args[:-1], y)  # chiama f(x1, ..., xk, y)
            return h(*args[:-1], y, recursive_result)  # chiama h(x1, ..., xk, y, f(x1, ..., xk, y))
    return recursive_function;

def ricorsione_primitiva(x, g, h): # x = (x1, ..., xk), g e h sono funzioni primitive ricorsive
    F = g(*x); # F(x) = g(x1, ..., xk)
    for i in range(y): # per i = 0, ..., n - 1
        F = h(*x, i, F); # F(x, i + 1) = h(x1, ..., xk, i, F(x, i))
    return F;


# ESTERNSIONE DELLE FUNZIONI PRIMITIVE RICORSIVE

# prodotto
def mul(x, y):
    if(y == 0):
        return 0;
    else:
        return ( x + mul(x, y - 1) );

# potenza
def pow(x, y):
    if(y == 0):
        return 1;
    else:
        return ( x * pow(x, y - 1) );

# iperpotenza
def hyperpow(x, y):
    if(y == 0):
        return 1;
    else:
        return pow(x, hyperpow(x, y - 1));

# predecessore
def pred(x):
    if(x == 0):
        return 0;
    else:
        return ( x - 1 );

# sottazione
def diff(x, y):
    if(y == 0):
        return x;
    else:
        return pred(diff(x, y - 1));

# fattoriale
def fact(y):
    if(y == 0):
        return 1;
    else:
        fattoriale = y * fact(y - 1);
        return fattoriale;

# segno
def sign(x):
    if(x == 0):
        return 0;
    else:
        return 1;

# if-then-else
def ite(x, y, z, f, g):
    if(y > z):
        return f(x,y,z);
    else:
        return g(x,y,z);

# modulo 
def mod(y, x):
    if(y == 0):
        return 0;
    elif(x == 0 or x == 1):
        return y; # se x = 0 o x = 1, allora mod(y, x) = y per ogni y in N
    else:
        mod_prec= mod(y-1, x);
        modulo = succ(mod_prec) * sign(x - succ(mod_prec));
        return modulo;

# divisione
def div(y, x):
    if(x == 0):
        raise ValueError("La divisione per zero non è definita");
    elif(y == 0):
        return 0;
    else:
        div_prec = div(y - 1, x);
        if( mod(y, x) == 0):
            divisione = succ(div_prec);
        else:
            divisione = div_prec;
        return divisione;

# minimo
def min(x, y):
    minimo = diff(x, diff(x, y));
    return minimo;

# massimo 
def max(x, y):
    massimo = sum(x, diff(y, x));
    return massimo;

# somma
def sum(x, y):
    if(y == 0):
        return x;
    else:
        return succ(sum(x, y - 1));

# produttora
# sommatoria

# mu-operatore-limitato
# sia f primitiva ricorsiva n+1 aria
# g(x1, ..., xn, y) = mu*z < y*( f(x1, ..., xn, z) = 0 )
# mu*z < y*( f(x1, ..., xn, z) = 0 ) = 0 se esiste z < y tale che f(x1, ..., xn, z) = 0
def mu_operatore_limitato(f, x, y):
    z = 0;
    found = False;
    while(not found and z < y):
        if(f(*x, z) == 0):
            found = True;
        else:
            z = z + 1;
    return z;
        

#-------------------------------------------------------------------------------------------
# TEST
print("TEST FUNZIONI PRIMITIVE RICORSIVE");
print("mul(3, 4) = ", mul(3, 4)); # 12
print("pow(2, 5) = ", pow(2, 5)); # 32
print("hyperpow(2, 3) = ", hyperpow(2, 3)); # 16
print("pred(5) = ", pred(5)); # 4   
print("diff(5, 3) = ", diff(5, 3)); # 2
print("fact(5) = ", fact(5)); # 120
print("sign(0) = ", sign(0)); # 0
print("sign(5) = ", sign(5)); # 1
print("ite(5, 3, 4, lambda x,y,z: x+y+z, lambda x,y,z: x*y*z) = ", ite(5, 3, 4, lambda x,y,z: x+y+z, lambda x,y,z: x*y*z)); # 12
print("ite(5, 4, 3, lambda x,y,z: x+y+z, lambda x,y,z: x*y*z) = ", ite(5, 4, 3, lambda x,y,z: x+y+z, lambda x,y,z: x*y*z)); # 60
print("mod(17, 3) = ", mod(17, 3)); # 2
print("div(17, 3) = ", div(17, 3)); # 5

print("min(20, 7) = ", min(20, 7)); # 7
print("max(20, 7) = ", max(20, 7)); # 20
print("sum(21, 21) = ", sum(21, 21)); # 42