def number_increment(numbers):
    def increase():
        numbs = [num + 1 for num in numbers]
        return numbs
    return increase()


print(number_increment([1, 2, 3]))