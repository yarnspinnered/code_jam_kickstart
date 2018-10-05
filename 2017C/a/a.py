import logging

logging.basicConfig(level=logging.ERROR)

def input(file_name):
    with open(file_name) as f:
        input = f.readlines()
        return [x.strip() for x in input[1:]]

def output(arr, file_name):
    with open(file_name, 'w') as f:
        for i,v in enumerate(arr):
            f.write("Case #{}: ".format(i + 1) + v + '\n')

def solve(val):

    if len(val) % 2 == 1:
        return 'AMBIGUOUS'
    encrypted = [ord(c) - ord('A') for c in val]
    decrypted = [None for x in range(len(val))]
    logging.debug('encrypted {}'.format(encrypted))
    decrypted[1] = encrypted[0]
    decrypted[-2] = encrypted[-1]

    for i in range(3, len(val), 2):
        if not decrypted[i]:
            decrypted[i] = (encrypted[i-1] - decrypted[i - 2] ) % 26
    for i in range(len(val) - 4, -1, -2):
        if not decrypted[i]:
            decrypted[i] = (encrypted[i + 1] - decrypted[i + 2]) % 26
    logging.debug(str(decrypted))
    return ''.join([chr(x + ord('A')) for x in decrypted])

small_input = input('A-small-practice.in')
output([solve(x) for x in small_input], 'A-small-practice.out')

large_input = input('A-large-practice.in')
output([solve(x) for x in large_input], 'A-large-practice.out')