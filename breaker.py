import sys
files=sys.argv[1]
address=sys.argv[2]
from bitcoin import *
p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
def load(files):
    signatures=[]
    import csv
    with open(files,'r') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=",")
        line = 0
        for row in csv_reader:
            r=(row[0])
            s1=(row[1])
            z1=(row[2])
            t=tuple([r,s1,z1])
            signatures.append(t)
            line+=1
     
    return signatures

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def inv_mod(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m

def recover():
    db = load(files)
    signatures = db
    nn = len(signatures)
    privkeys = []
    for ii in range(1, nn-1):
        z1 = int(signatures[ii][2])
        r = int(signatures[ii][0])
        s1 = int(signatures[ii][1])
        z2 = int(signatures[ii+1][2])
        r1 = int(signatures[ii+1][0])
        s2 = int(signatures[ii+1][1])
        if r == r1:
            pr = (((z1*s2) - (z2*s1)) * inv_mod(r*(s1-s2),p) % int(p))
            myhex = "%064x" % pr
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            pri = (((z1*s2) - (z2*s1)) * inv_mod(r*(s1+s2),p) % int(p))
            myhex = "%064x" % pri
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            priv = (((z1*s2) - (z2*s1)) * inv_mod(r*(-s1-s2),p) % int(p))
            myhex = "%064x" % priv
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            privk = (((z1*s2) - (z2*s1)) * inv_mod(r*(-s1+s2),p) % int(p))
            myhex = "%064x" % privk
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            privke = (((z1*s2) + (z2*s1)) * inv_mod(r*(s1-s2),p) % int(p))
            myhex = "%064x" % privke
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            privkey = (((z1*s2) + (z2*s1)) * inv_mod(r*(s1+s2),p) % int(p))
            myhex = "%064x" % privkey
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
            privkeys = (((z1*s2) + (z2*s1)) * inv_mod(r*(-s1-s2),p) % int(p))
            myhex = "%064x" % privkeys
            myhex = myhex[:64]
            priv = myhex
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break 
            privkeys1 = (((z1*s2) + (z2*s1)) * inv_mod(r*(-s1+s2),p) % int(p))
            myhex = "%064x" % privkeys1
            myhex = myhex[:64]
            priv = myhex
            print(priv)
            pub = privtopub(priv)
            pubkey1 = encode_pubkey(privtopub(priv), "bin_compressed")
            addr = pubtoaddr(pubkey1)
            n = addr
            if n.strip() == address:
                print("HAckedaddress",addr, myhex)
                break
recover()
