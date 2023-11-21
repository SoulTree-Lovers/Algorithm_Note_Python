n, m, k = map(int, input().split())

num_list = list(map(int, input().split()))

num_list.sort()

first_max = num_list[-1]
second_max = num_list[-2]

count = m // (k + 1) * k + m % (k + 1)

result = 0
result += count * first_max
result += (m - count) * second_max

print(result)