

#Last in first out 



# class stack:
#     def __init__(self) -> None:
#         self.values =[]
#     def push(self,x):
#         self.values = [x] + self.values
#     def pop(self):
#         return self.values.pop(0)
    
# s=stack()
# s.push(10)
# s.push(20)
# s.push(30)
# s.push(40)
# print(s.values)
# s.pop()
# print(s.values)

# ______________


class queue:
    def __init__(self) -> None:
        self.values =[]
        
    def enqueue(self,x):
        self.values.append(x)
        
    def dequeue(self):
        front = self.values[0]
        self.values=self.values[1:]
        return front
    
q1=queue()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

print(q1.values)

print(q1.dequeue())
print(q1.values)