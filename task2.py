def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinations(n, k):
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))


def lottery_probability(N, K, M):
    total_ways = combinations(N, K)
    winning_ways = 0

    for m in range(M, K + 1):
        ways_to_choose_m = combinations(K, m)
        ways_to_choose_remaining = combinations(N - K, K - m)
        winning_ways += ways_to_choose_m * ways_to_choose_remaining

    probability = (winning_ways / total_ways) * 100
    return round(probability, 4)


N = 20
K = 11
M = 8

result = lottery_probability(N, K, M)
print(f"Вероятность выигрыша: {result}%")