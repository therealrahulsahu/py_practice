if __name__ == '__main__':

    n = int(input('Enter N : '))
    data = list(map(int, input('Enter list : ').split()))
    x = int(input('Enter x : '))

    from itertools import combinations
    comb = list(combinations(data, 3))

    i = 0
    while True:
        try:
            if sum(comb[i]) == x:
                print(*sorted(list(comb[i])))
            i += 1
        except IndexError:
            break
