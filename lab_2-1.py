# Yongdong Xi Mar 4


class car:
    def __build_car__(wheels, axels, doors, color):
        wls = wheels
        wheels = int(input("How many wheels does this car have? "))
        als = axels
        axels = int(input("How many axels does this car have? "))
        dos  = doors
        doors = int(input("How many doors does this car have? "))
        cor = color
        color = input("What is color of this car? ")
    print('This car has', wls, 'wheels,', axels, 'axels,', doors, 'doors and', color, 'color')