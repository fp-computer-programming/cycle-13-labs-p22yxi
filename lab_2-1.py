# Yongdong Xi Mar 4


class car:
    def __build_car__(wheels, axels, doors, color):
        wls = wheels
        als = axels
        dos  = doors
        cor = color



        doors = int(input("How many doors does this car have? "))
        axels = int(input("How many axels does this car have? "))
        color = input("What is color of this car? ")
        wheels = int(input("How many wheels does this car have? "))
    print('This car has', wls, 'wheels,', axels, 'axels,', doors, 'doors and', color, 'color')