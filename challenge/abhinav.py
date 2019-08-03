def check(test):
    from re import compile
    p1 = compile(r'(a)(?!(a|bb|$))')
    p2 = compile(r'(bb)(?!(a|$))')
    return not (bool(p2.search(test)) or bool(p1.search(test)))


print(input('Enter String : '))


