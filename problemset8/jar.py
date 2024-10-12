class Jar:
    def __init__(self, capacity=12):
        self.capacity=capacity
        self.sizej=0
        

    def __str__(self):
         print(self._sizej*"\U0001F36A")
        

    def deposit(self, n):
        if n+self._sizej>= self._capacity:
            raise ValueError("Capacity exceeded")
        else:
            self._sizej+=n
        

    def withdraw(self, n):
        if self._sizej-n< 0:
            raise ValueError("Not many cookies left")
        else:
            self._sizej-=n

    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        if not(capacity >= 0):
            raise ValueError("Wrong Capacity")
        else:
            self._capacity=capacity

    @property
    def sizej(self):
        return self._sizej
    @sizej.setter
    def sizej(self,initial=0):
        self._sizej=0
def main():
    jar1=Jar(capacity=5)
    jar1.deposit(4)
    print(jar1.sizej)
    jar1.withdraw(3)
    print(jar1.sizej)
    print(jar1)
        

    
   
if __name__ == "__main__":
    main()