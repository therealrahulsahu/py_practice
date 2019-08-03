import re
import os


def file_py(var):
    patt = re.compile(r'^(.+)(\.py)$')
    if patt.match(var):
        return True
    else:
        return False


def file_jpg(var):
    patt = re.compile(r'^(.+)(\.jpg)$')
    if patt.match(var):
        return True
    else:
        return False


def run_python(add):
    for x in os.walk(add):
        for y in filter(file_py,x[2]):
            temp = 'python \"'+x[0]+'\\'+y+'\"'
            os.system(temp)


def run_jpg(add):
    for x in os.walk(add):
        for y in filter(file_jpg, x[2]):
            temp = '\"'+x[0]+'\\'+y+'\"'
            os.system(temp)



def trave_py(add):
    os.chdir(add)
    content = os.listdir()
    for x in filter(file_py, content):
        os.system('python \"{}\"'.format(x))
    for x in filter(os.path.isdir, content):
        trave_py(x)
        os.chdir('..')


def trave_jpg(add):
    os.chdir(add)
    content = os.listdir()
    for x in filter(file_jpg, content):
        # os.system('\"{}\"'.format(x))
        print(os.path.abspath(x))
    for x in filter(os.path.isdir, content):
        trave_jpg(x)
        os.chdir('..')


def specific_add(add, patt, out):
    os.chdir(add)
    for x in os.listdir():
        if os.path.isfile(x):
            if patt.search(x):
                out.append(os.path.abspath(x))
        elif os.path.isdir(x):
            if patt.search(x):
                out.append(os.path.abspath(x))
            specific_add(x, patt, out)
            os.chdir('..')


data = []
sea=input('Enter patt to search: ')
specific_add('d:\\media\\', re.compile(r'{}'.format(sea), re.I), data)
print(*data, sep='\n')

#trave_jpg('D:\\Media\\Pictures\\Photo')
#os.chdir('d:\\rahul code\\python\\rahul')
#print(*list(filter(os.path.isdir,os.listdir('d:\\rahul code\\python\\rahul'))))
#print(*os.listdir('d:\\rahul code\\python\\rahul'),sep='\n')
