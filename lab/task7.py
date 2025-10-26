lines = ['one', 'two', 'three']

with open('input.txt', 'w') as f:
    for line in lines:
        f.write(f'Cycle run {line}\n')

print('Done!')