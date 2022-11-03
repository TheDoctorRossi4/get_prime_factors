def get_prime_factors(value: int) -> list:
    items = []
    divisor = 2
    temp_fract = value

    while divisor <= value:
        fract = temp_fract / divisor
        if temp_fract % divisor == 0:
            items.append(divisor)
            temp_fract = fract
        divisor += 1
    return items
