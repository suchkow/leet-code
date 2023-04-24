from collections import deque


def is_valid(s: str) -> bool:
    pairs_ls = [('(', ')'), ('[', ']'), ('{', '}')]
    deq = deque([ ])

    if len(s) % 2 != 0:
        return False

    for i, j in s:
        deq.append(i)
        deq.append(j)
        s = s[2:]


    return 


case_1 = '()' # true
case_2 = '()[]{}' # true
case_3 = '[({})]' # true
case_4 = '[(}){]' # false
case_5 = '(]' # false

is_valid(case_1)
is_valid(case_2)
is_valid(case_3)
is_valid(case_4)
is_valid(case_5)

