def createTextFile(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def stats_decorator(func):
    def wrapper(*args, **kwargs):
        numbers = [num for sublist in func(*args, **kwargs) for num in sublist]
        print(f'a) Numbers read: {numbers}')
        print(f'b) Count of numbers read: {len(numbers)}')
        print(f'c) Average of numbers: {sum(numbers)/len(numbers)}')
        print(f'd) Maximum of numbers: {max(numbers)}')
        return numbers
    return wrapper

@stats_decorator #stats_decorator is used to add functionality to the printStats function. Specifically, it adds the ability to print statistics about the numbers read from a file: the numbers themselves, their count, their average, and the maximum number.
def printStats(t):
    numbers_list = []
    with open(t, 'r') as file:
        for line in file:
            numbers = list(map(int, line.split()))  # map function is used to convert the string to an iterable integers
            numbers_list.append(numbers)
    return numbers_list

sample_content = """14 6
6
14"""
sample_filename = 'sample_text.txt'
createTextFile(sample_filename, sample_content)

printStats('sample_text.txt')