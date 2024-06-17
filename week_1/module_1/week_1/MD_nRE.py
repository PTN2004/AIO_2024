import math

def md_nre_single_sample(y, y_hat, n=2, p=1):
    loss = math.pow(y, 1/n) - math.pow(y_hat, 1/n)
    return math.pow(loss, p)

print(md_nre_single_sample(100, 99.5))
print(md_nre_single_sample(50, 49.5))
print(md_nre_single_sample(20, 19.5))
print(md_nre_single_sample(0.6, 0.1))

