# perbandingan
# lebih besar >
# lebih keccil <
# lebih besar sama dengan >=
# lebih kecil sama dengan <=
# sama dengan ==
# tidak sama dengan !=
# sama "is"
# sama tidak "is not"

x = 4
y = 5

hasil = x > y
print(x, '>', y, 'adalah', hasil)

# lebih besar 
hasil = x < y 
print(x,'<','adalah', hasil)

hasil = x >= y
print(x, '>=', y, 'adalah', hasil)

hasil = x <= y
print(x, '<=', y, 'adalah', hasil)


hasil = x == y
print(x, '==', y, 'adalah', hasil)

hasil = x != y
print(x, '!=', y, 'adalah', hasil)

hasil = x is y
print(x, 'is', y, 'adalah', hasil)

hasil = x is not y
print(x, 'is not', y, 'adalah', hasil)





# > < >= <= == != ini adalah perbandingan literal
# x = 4,4 = literal (tidak memakan memory)
# x = object (memeory)
#
# x = 4 (bisa)
# x is 4 (tidak bisa, yang di bandingkan adl literal)
# x is y (bisa,karena yd di bandibngkan adalah object)

# is dan is not
hasil = x is y
print(x, 'is',y, 'adalah', hasil)

hasil = x is not y
print(x, 'is not',y, 'adalah', hasil)