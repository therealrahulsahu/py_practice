import re
import time
with open('EnglishDictionary.csv', 'r') as file:
    data_txt = file.read()
data = [[x.split(',')[0], int(x.split(',')[1])] for x in data_txt.split('\n')]


def filter_data(values, tm):
    reg = re.compile(r'(?i)^'+tm)
    output = []
    first = False
    for x in values:
        if reg.match(x[0]):
            output.append(x)
            first = True
        else:
            if first:
                break
    return output


user = ''
while True:
    inp = input()
    if inp == '#':
        break
    user += inp
    st = time.time()
    data = filter_data(data, user)
    result = sorted(data, key=lambda x: x[1], reverse=True)[:5]
    en = time.time()
    total = int((en-st)*(10**6))
    if len(result) > 0:
        print(*[x[0] for x in result], sep=', ', end='\t\t{}\n'.format(total))
    else:
        print('No match Found !! \t\t{}'.format(total))
        break
print('Exiting')

exit_now = input('Press Enter to exit')
