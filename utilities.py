import random
import math

# Constants
rad_to_degree = 57.2957795


# This function creates random color numbers
def randomizeColor():
    return random.randrange(256), random.randrange(256), random.randrange(256)


# This function finds cosine of two coordinates
def cosineAngle(x1, y1, x2, y2):
    nominator = (x1*x2) + (y1*y2)
    denominator = math.sqrt(x1**2 + y1**2) + math.sqrt(x2**2 + y2**2)

    return nominator / denominator


# This function converts cosine to angle using arccos
def angle(x1, y1, x2, y2):
    cosine = cosineAngle(x1, y1, x2, y2)
    return round(math.acos(cosine) * rad_to_degree)


def slope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)


def slopeAngle(x1, y1, x2, y2):
    try:
        return round(math.atan(slope(x1, y1, x2, y2)) * rad_to_degree)
    except ValueError:
        pass


def speedAcc(speed, increment):
    if speed[1] < 0:
        speed[1] -= increment
    else:
        speed[1] += increment
    return speed


# Direction True side is right, False is left
def hold_key_hitpad(pad_var, direction: bool, replacement):
    if direction:
        pad_var += replacement
    elif not direction :
        pad_var -= replacement
    return pad_var


if __name__ == "__main__":
    print(randomizeColor())

    print(slopeAngle(1, 1, -1, -1))