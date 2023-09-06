class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2
    
    def breathe(self):
        print("Inhale, Exhale")

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()

    def breathe(self):
        #Do everything in the Animal class breathe method, but add an extra string
        super().breathe()
        print("Doing this underwater.")

    def swim(self):
        print("moving in water.")

nemo = Fish()
nemo.swim()
nemo.breathe()
print (nemo.num_eyes)