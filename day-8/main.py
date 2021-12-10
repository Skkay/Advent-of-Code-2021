# 0 : 6
# 1 : 2 *
# 2 : 5
# 3 : 5
# 4 : 4 *
# 5 : 5
# 6 : 6
# 7 : 3 *
# 8 : 7 *
# 9 : 6
with open('day-8/inputs.txt', 'r') as f:
    inputs = f.readlines()

signals = []
values = []
for input in inputs:
    signals.append(input.split(' | ')[0].strip().split(' '))
    values.append(input.split(' | ')[1].strip().split(' '))

count = 0
for value in values:
    for v in value:
        count += 1 if len(v) in [2, 4, 3, 7] else 0

print(count)
