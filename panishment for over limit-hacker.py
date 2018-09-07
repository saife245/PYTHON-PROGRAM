speed = int(input('ENTER THE SPEED: '))

if speed <= 90:
    print("0 No punishment")

elif speed >= 91 and speed <= 110:

    FINE = (speed - 90)*300
    print("{} WARNING".format(FINE))

else:
    FINE = (speed - 90)*500
    print("{} LICENSE REMOVED".format(FINE))
