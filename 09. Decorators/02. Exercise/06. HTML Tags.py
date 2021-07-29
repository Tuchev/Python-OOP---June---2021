def tags(tag):
    def add_tag(func):
        def wrapper(*args):
            return f"<{tag}>{func(*args)}</{tag}>"

        return wrapper

    return add_tag


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
