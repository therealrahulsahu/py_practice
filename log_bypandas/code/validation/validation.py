def validPatt(reg, string):
    from re import compile
    reg = compile(reg)
    return bool(reg.match(string))


def validEmail(string):
    reg = r'^((?<!\.)([\w]+)(?!\.))@(\w+)(\.\w+(\.\w+)?(?!\.))$'
    return validPatt(reg, string)


def validPhone(string):
    reg = r'^[6-9][0-9]{9}$'
    return validPatt(reg, string)


def validName(string):
    reg = r'^[a-zA-Z\s]+$'
    return validPatt(reg, string)

