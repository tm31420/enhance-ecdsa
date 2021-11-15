import random
def modInv(n, p):
    return pow(n, p - 2, p)


def jordan_isinf(p):
    return p[0][0] == 0 and p[1][0] == 0


def mulcoords(c1, c2):
    return (c1[0] * c2[0] % P, c1[1] * c2[1] % P)


def mul_by_const(c, v):
    return (c[0] * v % P, c[1])


def addcoords(c1, c2):
    return ((c1[0] * c2[1] + c2[0] * c1[1]) % P, c1[1] * c2[1] % P)


def subcoords(c1, c2):
    return ((c1[0] * c2[1] - c2[0] * c1[1]) % P, c1[1] * c2[1] % P)


def invcoords(c):
    return (c[1], c[0])


def jordan_add(a, b):
    if jordan_isinf(a):
        return b
    if jordan_isinf(b):
        return a
    if (a[0][0] * b[0][1] - b[0][0] * a[0][1]) % P == 0:
        if (a[1][0] * b[1][1] - b[1][0] * a[1][1]) % P == 0:
            return jordan_double(a)
        else:
            return ((0, 1), (0, 1))

    xdiff = subcoords(b[0], a[0])
    ydiff = subcoords(b[1], a[1])
    m = mulcoords(ydiff, invcoords(xdiff))
    x = subcoords(subcoords(mulcoords(m, m), a[0]), b[0])
    y = subcoords(mulcoords(m, subcoords(a[0], x)), a[1])
    return (x, y)


def jordan_double(a):
    if jordan_isinf(a):
        return ((0, 1), (0, 1))
    num = addcoords(mul_by_const(mulcoords(a[0], a[0]), 3), [0, 1])
    den = mul_by_const(a[1], 2)
    m = mulcoords(num, invcoords(den))
    x = subcoords(mulcoords(m, m), mul_by_const(a[0], 2))
    y = subcoords(mulcoords(m, subcoords(a[0], x)), a[1])
    return (x, y)


def jordan_multiply(a, n):
    if jordan_isinf(a) or n == 0:
        return ((0, 0), (0, 0))
    if n == 1:
        return a
    if n < 0 or n >= N:
        return jordan_multiply(a, n % N)
    if n % 2 == 0:
        return jordan_double(jordan_multiply(a, n // 2))
    else:  # n % 2 == 1:
        return jordan_add(jordan_double(jordan_multiply(a, n // 2)), a)


def to_jordan(p):
    return ((p[0], 1), (p[1], 1))


def from_jordan(p):
    return (p[0][0] * modInv(p[0][1], P) % P, p[1][0] * modInv(p[1][1], P) % P)


def mul(a, n):
    """
    Multiply an ECPoint.
    @param {number} a - An ECPoint
    @param {number} n - A Big Number
    """
    return from_jordan(jordan_multiply(to_jordan(a), n))


def div(a, n):
    """
    Divide an ECPoint.
    @param {number} a - An ECPoint
    @param {number} n - A Big Number
    """
    return from_jordan(jordan_multiply(to_jordan(a), modInv(n, N) % N))


def add(a, b):
    """
    Add two ECPoints.
    @param {number} a - An ECPoint
    @param {number} b - An ECPoint
    """
    return from_jordan(jordan_add(to_jordan(a), to_jordan(b)))


def sub(a, b):
    """
    Subtract two ECPoints.
    @param {number} a - An ECPoint
    @param {number} b - An ECPoint
    """
    return from_jordan(jordan_add(to_jordan(a), to_jordan((b[0], P - (b[1] % P)))))


def negate(a):
    return (a[0], P - (a[1] % P))
#
def compress(a):
    return (a[1])

def ecPoint(a):
    return mul((X, Y), a)

P = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
N = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
G = (0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798, 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8)
p = (0x7ebc1070fc6d694ad9128ce3dfb800e10035463d60016b5f9641b9e133f02222, 0x1a8fd1ee1e1a89cef69a6411b48a03f1b8dc30d2de0c53611dc4238754868cae) # evil key.

def rrr(i):
	tmpstr = hex(i)
	hexstr = tmpstr.replace('0x','').replace('L','').replace(' ','').zfill(64)
	return hexstr

def verify(public_key, message, signature):
    z=message 
    r, s = signature
    w = modInv(s, N)
    u1 = (z * w) % N
    u2 = (r * w) % N
    x, y = add(mul(G, u1),mul(public_key,u2))
    if (r % N) == (x % N):
        return True
    else:
        return False

def forge(c, a): # Create a forged'ECDSA' (hashless) signature, thanks to ???
  # set a to something other than -1 to be less obvious
    a = a % N
    g = mul(G,c)
    r = mul(p,a)
    R = add(g, r)
    s = ((R[0] * modInv(a,N)) % N)
    m = ((c * R[0] * modInv(a,N)) % N)
    r = (R[0])
    signature = r,s
    if verify(p,m,signature) == True:
        print("1111",",",(rrr(m)),",",(rrr(r)),",",(rrr(s)),",","0000") # 4 breakingecdsawithlll by daedalus m is message, r,s is signature
count = 0
while count < 1000:
    a = random.randint(1,2**256)
    c = random.randint(1,2**256)
    forge(c,a)
#this is a work in progress
