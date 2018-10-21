from collections import defaultdict, Counter
import scipy.special

def input(file_name):
    with open(file_name) as f:
        count = int(f.readline())
        res = []
        for _ in range(count):
            tmp = []
            tmp.append(int(f.readline().strip()))
            tmp.append([int(x) for x in f.readline().strip().split()])
            res.append(tmp)
        return res

def output(arr, file_name):
    with open(file_name, 'w') as f:
        for i,v in enumerate(arr):
            f.write("Case #{}: ".format(i + 1) + v + '\n')

def solve(val):

    _, arr = val
    hm = defaultdict(lambda :0)

    counts = Counter(arr)
    keys = counts.keys()
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            hm[i * j] += 1
    print(hm)
    res = 0
    for k in keys:
        if k in hm:
            cnt = hm[k]
            skipped = False
            for x in arr:
                if x == k and not skipped:
                    continue
                if x * k == k:
                    cnt -= 1
            res += cnt
    # res = 0
    # for i in range(len(arr) - 2, -1, -1):
    #     x = arr[i]
    #
    #     update_hm(i + 1)
    #     # print(hm)
    #     # print(x, any(not i in pair for pair in hm[x]))
    #     if x in hm:
    #         res += hm[x]
    return str(res)


test_input = input('a-test.in')
output([solve(x) for x in test_input], 'A-test-modded.out')

#
# small_input = input('A-small-attempt0.in')
# output([solve(x) for x in small_input], 'A-small-practice-modded.out')
#
# large_input = input('A-large-practice.in')
# output([solve(x) for x in large_input], 'A-large-practice.out')