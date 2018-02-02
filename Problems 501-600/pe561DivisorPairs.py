##Let S(n) be the number of pairs (a,b) of distinct divisors of
##n such that a divides b.
##For n=6 we get the following pairs: (1,2),(1,3),(1,6),(2,6),(3,6).
##So S(6)=5.
##Let p_m# be the product of the first mm prime numbers, so p2#=2∗3=6.
##Let E(m,n) be the highest integer k such that 2^k divides S((p_m#)^n).
##E(2,1)=0 since 2^0 is the highest power of 2 that divides S(6)=5.
##Let Q(n) be the sum of E(904961,i) from i=1 to n.
##Q(8)=2714886.
##
##Evaluate Q(10^12).

from time import time
import sys
sys.path.append("../Library")
from peresult import peresult

# THEORY:
# For the number p^n, where p is prime, there are (n+1)(n+2)/2 pairs of
# divisors (including the n+1 pairs where both entries are equal).
# For p_1^n * p_2^n * ... * p_m^n, there are therefore
# ((n+1)(n+2)/2)^m pairs of divisors.
# There are (n+1)^m pairs where the divisors are not distinct; these must be
# removed from consideration, so S((p_m#)^n) = ((n+1)(n+2)/2)^m - (n+1)^m.
# This formula can be factored alternately as
#     (n+1)^m * (((n+2)/2)^m - 1)
# or as
#     ((n+1)/2) ^ m * ((n+2)^m - 2^m).
# Define T(x) as the highest power of two that divides x.
# There are four cases.
#     If n mod 4 == 0:
#         Use the first factorization.
#         n+1 is odd.
#         (n+2)/2 is odd.
#         (((n+2)/2)^m - 1) is even.
#         The problem then becomes to count the factors of two
#         in (((n+2)/2)^m - 1).
#         Define n as 4*k, where 1 <= k <= cap//4.
#         Then T(n) = T((2k + 1)^m - 1)
#                   = T( (m choose 0)(2k^m) + (m choose 1)(2k^(m-1))
#                        + ... + (m choose m-1)(2k).
#         Trivial to show that the T of each other term is strictly greater
#         than the T of the last term.
#         Therefore E(m,n) = T(m*2k) = T(2k) = T(k) + 1.
#         The sum of all such E(m,n) for n mod 4 == 0
#         is therefore cap//4 + cap//8 + cap//16 + cap//32 + ...
#     If n mod 4 == 1:
#         Use the second factorization.
#         (n+1)/2 is odd.
#         (n+2)^m is odd.
#         (n+2)^m - 2^m is odd.
#         Both halves of the equation are odd, so E(m,n) == 0.
#     If n mod 4 == 2:
#         Use the first factorization.
#         (n+1)^m is odd.
#         (n+2)/2 is even.
#         ((n+2)/2)^m - 1 is odd.
#         Both halves of the equation are odd, so E(m,n) == 0.
#     If n mod 4 == 3:
#         Use the second factorization.
#         ((n+2)^m - 2^m) is odd.
#         (n+1)/2 is even.
#         ((n+1)/2)^m is even.
#         Thus E(m,n) = m * T((n+1)/2).
#         Summing E(m,n) over all such n is equivalent to summing
#         m * T(2k) for 1 <= k <= (cap+1)//4, as k = (n+1) / 4.
#         The sum of all E(m,n) for n mod 4 == 3
#         is therefore m*( (cap+1)//4 + (cap+1)//8 + (cap+1)//16 + ... )
#     Since 10^12 mod 4 == 0, cap+1//2^n == cap//2^n.
#     This means Q(cap) = (m+1) * (cap//4 + cap//8 + cap//16 + cap//32 + ...)

def solve(cap):
    start = time()
    result = cap // 4
    term = cap // 4
    while term > 0:
        term //= 2
        result += term
    result *= 904961 + 1
    peresult(561, result, time() - start)

if __name__ == "__main__":
    solve(10 ** 12)
