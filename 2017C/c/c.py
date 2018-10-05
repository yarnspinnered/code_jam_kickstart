from pprint import pprint

def input(file_name):
    res = []
    with open(file_name) as file:
        n = int(file.readline().strip())  # Number of cases
        for i in range(n):
            m = int(file.readline().strip().split()[0])  # Number of lines for this case
            curr = []

            for j in range(m + 1):
                curr.append(file.readline().strip())
            scores = [int(x) for x in file.readline().split()]
            res.append((curr,scores))
    pprint(res)
    return res


def output(arr, file_name):
    with open(file_name, 'w') as f:
        for i,v in enumerate(arr):
            f.write("Case #{}: ".format(i + 1) + (str(v)) + '\n')

def solve(input):
    print('solving')
    n = len(input[0]) - 1
    others_tests = input[0][:n]
    others_scores = input[1][:n]
    self_tests = input[0][-1]
    q_cnt = len(self_tests)
    best = 0

    if n == 1:
        different = 0
        for j in range(q_cnt):
            if others_tests[0][j] != self_tests[j]:
                different += 1
        same = q_cnt - different
        if others_scores[0] <= same:
            return others_scores[0] + different
        else:
            return q_cnt - (others_scores[0] - same)

    both = only1 = only2 = neither= 0
    for j in range(q_cnt):
        f = [False, False]

        for i in range(n):
            if others_tests[i][j] == self_tests[j]:
                f[i] = True
        if f[0] and f[1]:
            both += 1
        elif f[0]:
            only1 += 1
        elif f[1]:
            only2 += 1
        else:
            neither += 1

    for a in range(0, q_cnt + 1):
        for b in range(0, q_cnt + 1):
            for c in range(0, q_cnt + 1):
                for d in range(0, q_cnt + 1):
                    if a + b + c + d > q_cnt or a > both or b > only1 or c > only2 or d > neither:
                        continue
                    if a + b + (only2 - c) + (neither - d) == others_scores[0] \
                        and a + (only1 - b) + c + (neither- d) == others_scores[1]:
                        best = max(best, a + b + c+ d)
    return best


res = [solve(x) for x in input('C-large-practice.in')]
output(res, 'C-large-practice.out')
# Input
#
# Output
#
#
# 3
# 1 2
# TF
# FF
# 1
# 1 3
# TTT
# TTF
# 0
# 2 3
# TTF
# FTF
# TTT
# 1 2
#
#
#
# Case  # 1: 2
# Case  # 2: 1
# Case  # 3: 2
#
