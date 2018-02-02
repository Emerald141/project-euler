# An unbiased single 4-sided die is thrown and its value, T, is noted.
# T unbiased 6-sided dice are thrown and their scores are added together.
#     The sum, C, is noted.
# C unbiased 8-sided dice are thrown and their scores are added together.
#     The sum, O, is noted.
# O unbiased 12-sided dice are thrown and their scores are added together.
#     The sum, D, is noted.
# D unbiased 20-sided dice are thrown and their scores are added together.
#     The sum, I, is noted.
# Find the variance of I, and give your answer rounded to 4 decimal places.

# THEORY:
#
# "_" denotes subscript.
# When following a "sum", "^" denotes superscript;
# otherwise, it denotes exponentiation.
# "d20" refers to a 20-sided die; do not confuse with the variable "d".
#
# E[I^2] = E[E[I^2 | D]]
# = sum_d P(D=d) E[I^2 | D=d]
# = sum_d P(D=d) E[(sum_{i=1}^d d20_i)^2]
# = sum_d P(D=d) E[sum_{i=1}^d (d20_i^2) + sum_{1<=i<j<=d} d20_i d20_j]
# = sum_d P(D=d) (d*E[d20^2] + d*(d-1)*E[d20]^2)
# = (sum_d P(D=d) d*(E[d20^2] + E[d20]^2)) + (sum_d P(D=d) d^2 E[d20]^2)
# = Var(d20) E[D] + E[d20]^2 E[D^2]
#
# Following the same chain of reasoning...
# E[D^2] = Var(d12) E[O] + E[d12]^2 E[O^2]
# E[O^2] = Var(d8) E[C] + E[d8]^2 E[C^2]
# E[C^2] = Var(d6) E[T] + E[d6]^2 E[T^2]
# E[T^2] = Var(d4) + E[d4]^2
#
# E[I] = E[d20] E[D]
# E[D] = E[d12] E[O]
# E[O] = E[d8] E[C]
# E[C] = E[d6] E[T]
# E[T] = E[d4]

from time import time

start = time()

letterSquare = 1    # if calculating C, then E[T^2];
                    # if calculating O, then E[C^2]; etc.
letter = 1          # if calculating C, then E[T];
                    # if calculating O, then E[C]; etc.

for die in [4, 6, 8, 12, 20]:   # Calculate T, C, O, D, and I, in order
    roll = (die + 1.) / 2   # if calculating T, then E[d4];
                            # if calculating C, then E[d6]; etc.
    rollSquare = sum([x ** 2. for x in range(1, die + 1)]) / die
                            # if calculating T, then E[d4^2];
                            # if calculating C, then E[d6^2]; etc.

    letterSquare = (rollSquare - roll ** 2) * letter + roll ** 2 * letterSquare
    letter = letter * roll

result = letterSquare - letter ** 2  # Var(I) = E[I^2] - E[I]^2
peresult(389, result, time() - start)
