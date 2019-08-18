def cal_max_cons(data):
    sub = []
    i = 0
    try:
        while True:
            sub.append(data[i+1]-data[i])
            i += 1
    except IndexError:
        pass
    max_gap = 1
    count = 1
    for x in sub:
        if x == 1:
            count += 1
            if count > max_gap:
                max_gap = count
        else:
            count = 1

    return max_gap


def main():
    n, m = list(map(int, input("Enter n and m : ").split()))
    data = list(map(int, input("Enter Arr : ").split()))
    result = 0
    result_arr = []
    for x in data:
        temp = data.copy()
        i = 1
        ele = m
        while True:
            if x+i not in temp:
                if ele == 0:
                    break
                temp.append(x+i)
                ele -= 1
            if x-i not in temp and x-i > 0:
                if ele == 0:
                    break
                temp.append(x-i)
                ele -= 1
            i += 1
        temp.sort()
        value = cal_max_cons(temp)
        if result < value:
            result = value
            result_arr = temp
    print(result_arr)
    print(result)


if __name__ == '__main__':
    main()


