##A particular school offers cash rewards to children with good attendance
##and punctuality. If they are absent for three consecutive days or late on
##more than one occasion then they forfeit their prize.
##
##During an n-day period a trinary string is formed for each child consisting
##of L's (late), O's (on time), and A's (absent).
##
##Although there are eighty-one trinary strings for a 4-day period that can
##be formed, exactly forty-three strings would lead to a prize:
##
##OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
##OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
##AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
##AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
##LAOO LAOA LAAO
##
##How many "prize" strings exist over a 30-day period?

from time import time
from peresult import peresult

def pe191(length):
        #Define p_0(n), p_1(n), p_2(n) as the number of L-free prize strings of
        #length n that end in an O, a first consecutive A, and a second
        #consecutive A, respectively. Then we have:
        #p_0(1) = 1, p_1(1) = p_2(1) = 0
        #For n > 1:
        #p_0(n) = p_0(n-1) + p_1(n-1) + p_2(n-1)
        #p_1(n) = p_0(n-1)
        #p_2(n) = p_1(n-1)
        #
        #Define p(n) = p_0(n) + p_1(n) + p_2(n). Then the result is
        #2p(0)p(29) + 2p(1)p(28) + ... + 2p(15)p(14) + p(30)
        #because if an L exists, it can be placed at any point to divide the
        #prize string into two L-free prize strings whose lengths sum to 29.

        start = time()
        p = [[1, 0, 0]] #p[n][i] = p_i(n)
        for x in range(length):
                new0 = p[x][0] + p[x][1] + p[x][2]
                new1 = p[x][0]
                new2 = p[x][1]
                p.append([new0, new1, new2])
        result = sum(p[length])
        for x in range((length + 1) // 2):
                result += 2 * sum(p[x]) * sum(p[length-1-x])
        peresult(191, result, time() - start)

if __name__ == "__main__":
        pe191(30)
