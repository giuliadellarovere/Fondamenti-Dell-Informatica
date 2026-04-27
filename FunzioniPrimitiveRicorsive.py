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
    return args[i - 1];