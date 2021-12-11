def get_number(final_segments, digit):
    eq = {'012345': 0, '12': 1, '01346': 2, '01236': 3, '1256': 4, '02356': 5, '023456': 6, '012': 7, '0123456': 8, '012356': 9}

    d_number = ''
    for d in digit:
        d_number += str(list(final_segments.keys())[list(final_segments.values()).index(d)])
    d_number = ''.join(sorted(d_number))

    return eq[d_number]


with open('day-8/inputs.txt', 'r') as f:
    inputs = f.readlines()

final_segments = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: ''}
signals = []
values = []
output = 0
for input in inputs:
    signals.append(input.split(' | ')[0].strip().split(' '))
    values.append(input.split(' | ')[1].strip().split(' '))

for index, signal in enumerate(signals):
    seg_count_1 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    seg_count_2 = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
    for digit in signal:
        for segment in digit:
            seg_count_1[segment] += 1
        
        if len(digit) in [2, 4, 3, 7]:
            for segment in digit:
                seg_count_2[segment] += 1

    final_segments[2] = list(seg_count_1.keys())[list(seg_count_1.values()).index(9)]
    final_segments[4] = list(seg_count_1.keys())[list(seg_count_1.values()).index(4)]
    final_segments[5] = list(seg_count_1.keys())[list(seg_count_1.values()).index(6)]

    seg_count_2[final_segments[2]] = -1
    seg_count_2[final_segments[4]] = -1
    final_segments[1] = list(seg_count_2.keys())[list(seg_count_2.values()).index(4)]
    final_segments[3] = list(seg_count_2.keys())[list(seg_count_2.values()).index(1)]

    seg_count_1[final_segments[1]] = -1
    seg_count_1[final_segments[3]] = -1
    final_segments[0] = list(seg_count_1.keys())[list(seg_count_1.values()).index(8)]
    final_segments[6] = list(seg_count_1.keys())[list(seg_count_1.values()).index(7)]


    final_value = ''
    for digit in values[index]:
        final_value += str(get_number(final_segments, digit))
    
    output += int(final_value)

print(output)
