def type_check(types):
    def check_accepts(func):
        def wrapper(num):
            if type(num) == types:
                return func(num)
            else:
                return "Bad Type"
        return wrapper
    return check_accepts


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
