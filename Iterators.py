class iterator:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
p1=iterator()
it=iter(p1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))