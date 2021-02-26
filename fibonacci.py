def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num-1)+fibonacci(num - 2)


number = input('please enter a number: ')
while True:
    if number.isdigit():
        print(fibonacci(int(number)))
        break
    else:
        number = input('please enter a VALID number:')


number = int(number)
sequence = []

if number <= 1:
    sequence.append(1)
else:
    sequence = [1]
    i = 1
    while i < number:
        if len(sequence) == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[len(sequence)-1]+sequence[len(sequence)-2])
        i += 1

print(sequence)