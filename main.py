def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result


def find_min_coins(amount, coins=None):
    if coins is None:
        coins = [50, 25, 10, 5, 2, 1]
    min_coins = [0] + [float('inf')] * amount

    for coin in coins:
        for x in range(coin, amount + 1):
            min_coins[x] = min(min_coins[x], min_coins[x - coin] + 1)

    if min_coins[amount] == float('inf'):
        return None

    result = {}
    while amount > 0:
        for coin in coins:
            if min_coins[amount - coin] == min_coins[amount] - 1:
                result[coin] = result.get(coin, 0) + 1
                amount -= coin
                break
    return result


# Жадібний алгоритм
print("Жадібний алгоритм:")
print(find_coins_greedy(113))

# Алгоритм динамічного програмування
print("Динамічне програмування:")
print(find_min_coins(113))

