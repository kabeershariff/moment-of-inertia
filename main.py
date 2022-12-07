class Formula(object):

    def ring_hollow(mass, radius):
        return mass*radius**2


    def disc_solid(mass, radius):
        return (mass*radius**2)/2

    def hollow(mass, radius):
        return (mass*radius**2)*(2/3)

    def sphere(mass, radius):
        return (mass*radius**2)*(2/5)

    def rod(mass, radius):
        return (mass*radius**2)/12



class Main(object):
    
    def __init__(self):
        Main.start()


    def start():
        
        print("FIND THE MOMENT OF INERTIA, enter your option")
        print("1. Ring and Hollow Cylinder")
        print("2. Disc and Solid Cylinder")
        print("3. Hollow Sphere")
        print("4. Solid Sphere")
        print("5. Rod")
        print("6. QUIT ")
        
        try:
            option = int(input())
        except:
            print("\n===>invalid input")
            Main()

        if option==6:
            exit()
        try:
            print("Enter mass")
            mass = float(input())

            print("radius")
            radius = float(input())

        except:
            print("\n===> An Error occured , Try a valid input\n")
            Main()

        
        if option == 1:
            answer = Formula.ring_hollow(mass, radius)
        elif option == 2:
            answer = Formula.disc_solid(mass, radius)
        elif option == 3:
            answer = Formula.hollow(mass, radius)
        elif option == 4:
            answer = Formula.sphere(mass, radius)
        elif option == 5:
            answer = Formula.rod(mass, radius)
        else:
            print("\nEnter valid option")
            Main()

        print(f"\n===> The answer is {answer} \n\n")
        Main()

Main()
