import re
with open('EnglishDictionary.csv', 'r') as file:
    data_txt = file.read()
data = [[x.split(',')[0], int(x.split(',')[1])] for x in data_txt.split('\n')]


def sub(values):
    n = len(values)
    output = []
    for Len in range(1, n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            st = ''
            for k in range(i, j + 1):
                st += values[k]
            output.append(st)
    return list(reversed(output))


def contain(cnt, entry):
    name = entry[0]
    i = 0
    for x in cnt:
        if x[0] == name:
            x[1] = max(entry[1], x[1])
            cnt.sort(key=lambda x: x[1], reverse=True)
            break
        i += 1
    if i == len(cnt):
        cnt.append(entry)
        cnt.sort(key=lambda x: x[1], reverse=True)
        if len(cnt) > 5:
            cnt.pop()


def filter_data(values, sch):
    output = []
    for x in values:
        for tm in sch:
            ln = len(tm)
            reg = re.compile(r'(?i)'+'.*'.join(list(tm)))
            reg_seq = re.compile(r'(?i)'+tm)
            reg_st = re.compile(r'(?i)^'+tm)
            if reg.search(x[0]):
                contain(output, [x[0], ln*x[1]])
            if len(tm) > 1 and reg_seq.search(x[0]):
                contain(output, [x[0], 1.5 * ln * x[1]])
            if reg_st.search(x[0]):
                contain(output, [x[0], 2 * ln * x[1]])
    return [x[0] for x in output]


user = input()
print(*filter_data(data, sub(user)), sep=', ')

exit_now = input('Press Enter to exit')
