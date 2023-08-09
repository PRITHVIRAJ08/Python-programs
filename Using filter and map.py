def prime(n):
    for i in range(2,n):
        if n%i ==0:
            return False
        else:
            return True
filtered=filter(prime,range(7))
print(list(filtered))
def pow(x):
    return x*x
mapped=map(pow,range(5))
print(list(mapped))