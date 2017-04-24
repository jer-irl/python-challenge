def exponent(base, raised):
    if raised == 0:
        return 1
    else:
        return base * exponent(base, raised - 1)

print exponent(2, 38)
