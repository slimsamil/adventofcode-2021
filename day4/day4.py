boards_raw = open('day4/boards.txt', 'r')
numbers_raw = open('day4/numbers.txt', 'r')

boards = boards_raw.read().split('\n\n')
numbers = numbers_raw.read().split(',')

print(boards)
print(numbers)