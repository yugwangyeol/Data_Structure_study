class Car:
    def __init__(self,color,speed=0):
        self.color = color
        self.speed = speed
    
    def speed_up(self):
        self.speed += 10
    
    def speed_down(self):
        self.speed -= 10

    def isEqual(self,carB):
        if self.color == carB.color:
            return True
        else:    
            return False
    
    def __eq__(self,other):
        return "YES" if self.color == other.color else "NO"
    
    def __str__(self):
        return "color: %s, speed: %s"%(self.color, self.speed)
    
    def __ge__(self,other):
        return "Faster" if self.speed >= other.speed else "Slower"

if __name__ == "__main__":
    car1 = Car('black')
    car2 = Car('red', 120)
    car3 = Car('yellow')

    car1.speed_up()
    car2.speed_down()

    print('car1 clor: %s, car1 speed : %s'%(car1.color, car1.speed))
    print('car2 clor: %s, car2 speed : %s'%(car2.color, car2.speed))
    print('car3 clor: %s, car3 speed : %s'%(car3.color, car3.speed))

    print(car1.isEqual(car2))
    print(car1 == car2)
    print("[car1] %s"%(car1))
    print(car1 >= car2)

    #print(car1)