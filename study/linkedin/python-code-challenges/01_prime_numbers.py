def get_prime_factors(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        div, mod = divmod(N, divisor)
        if mod == 0:
            factors.append(divisor)
            N = div
        else:
            divisor += 1
    return factors


if __name__ == "__main__":
    print(get_prime_factors(630))
    print(get_prime_factors(13))
