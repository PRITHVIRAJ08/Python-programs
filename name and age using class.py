class details():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person(self):
        print("name is:",self.name)
        print("age is :",self.age)
p1=details("prithvi","13")
p1.person()