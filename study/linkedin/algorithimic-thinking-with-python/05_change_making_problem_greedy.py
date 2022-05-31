coin_set = [1, 2, 5, 10, 20, 25, 50, 100, 200]
coin_set.reverse()


def make_change(target_amount):
    coin_set_idx = 0
    coins = []
    while target_amount > 0:
        while coin_set[coin_set_idx] > target_amount:
            coin_set_idx += 1

        coin = coin_set[coin_set_idx]
        coins.append(coin)
        target_amount -= coin

    return coins


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p
