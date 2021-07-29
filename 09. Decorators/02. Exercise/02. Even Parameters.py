def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            error_message = "Please use only even numbers!"
            try:
                if arg % 2 != 0:
                    return error_message
            except:
                return error_message
        return func(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
