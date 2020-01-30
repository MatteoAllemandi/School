import sys

N = 9973
g = 1567

try:
    sniffed_value = int(sys.argv[1])
except TypeError:
    print('Type Error')

print(f'Sniffed value = {sniffed_value}')

result_list = []

for y in range(0,N):
    if (g**y)%N == sniffed_value:
        result_list.append(y)

print(f'Computed value: {result_list}')