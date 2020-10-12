def fibo(count):
    sequence = [0, 1]

    any(map(lambda _: sequence.append(sum(sequence[-2:])), range(2, count)))

    return sequence[:count]

print(fibo(10))