# 4-9-2023 at 21:55
#
# real	0m0.078s
# user	0m0.012s
# sys	0m0.007s

# 3: arithmetic progression where a=3 and l=999.
# 5: arithmetic progression where a=5 and l=995.
#
# Sum of arithmetic progressions to l,
#        S = (l//a)/2 × (a + l)
#
# Only problem here is that the multiple of these numbers (3 and 5)
# will be repeated in both sums.
#
# Subtracting the sum of the multiple (namely 15) ONCE should work.

arith = lambda a, l: (l//a)/2 * (a + l)
print(arith(3, 999) + arith(5, 995) - arith(15, 990))
