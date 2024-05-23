pi = 3.141592
perimeter = 0

def calc_perimeter(radius):
    global perimeter
    print('pi:',pi)
    perimeter =2*pi*radius

calc_perimeter(10)

print('원둘레(r=10):',perimeter)