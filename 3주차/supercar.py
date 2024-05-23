from car import Car

class SuperCar(Car):
    def __init__(self,color,speed=0,bTurbo=True):
        super().__init__(color,speed)
        self.bTurbo = bTurbo
    
    def setTurbo(self,bTurbo=True):
        self.bTurbo = bTurbo
    
    def speed_up(self):
        if self.bTurbo:
            self.speed += 50
        else:
            super().speed_up()
    
    def __str__(self):
        if self.bTurbo:
            return "color: %s, speed: %s, Turbo: %s"%(self.color, self.speed, "On")
        else:
            return "color: %s, speed: %s, Turbo: %s"%(self.color, self.speed, "Off")

if __name__ == "__main__":
    s1 = SuperCar('gold')
    s2 = SuperCar("White", 50, False)

    print("s1 : ",s1)
    print("s2 : ",s2)

    s1.speed_up()
    s2.speed_up()

    print("s1 : ",s1)
    print("s2 : ",s2)