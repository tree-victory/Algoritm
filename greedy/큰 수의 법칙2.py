n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

result = 0

# 가장 큰 수가 더해지는 횟수
count = int(m/(k+1)) * k + m % (k+1)

result += first * count
result += (m - count) * second

print(result)
