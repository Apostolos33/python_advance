def sum_numbers(*args):
    sum_neg = 0
    sum_positives = 0
    for n in args:
        if n < 0:
            sum_neg += n
        else:
            sum_positives += n
    return sum_neg, sum_positives

negatives, positives = sum_numbers(*map(int, input().split()))
print(negatives)
print(positives)

if abs(negatives) > positives:
    print("The negatives are stronger than the positives")
elif abs(negatives) < positives:
    print("The positives are stronger than the negatives")