def sum_divisors(n):
    sum == 0
    totalSums = 0
    sum_divisors = [4]

    for i in range(2, n):

        if (n % i) == 0:
            sum_divisors.append(i)
            return sum(sum_divisors)

    if totalSums < 4:

        return sum(sum_divisors)
        totalSums == totalSums + 1


print(sum_divisors(0))
# 0
print(sum_divisors(3))
# Should sum of 1
# 1
print(sum_divisors(36))
# Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102))
# Should be sum of 2+3+6+17+34+51
# 114
