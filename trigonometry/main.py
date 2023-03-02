import math

def calculate(anglerad, opposite):
    # angle and opposite
    print(f"angle = {math.degrees(anglerad)}°")
    print(f"opposite = {opposite}")
    hypotenuse = opposite / math.sin(anglerad)
    adjacent = opposite / math.tan(anglerad)
    print(f"hypotenuse = {opposite} / sin({math.degrees(anglerad)}) = {hypotenuse}")
    print(f"adjacent = {opposite} / tan({math.degrees(anglerad)}) = {adjacent}")


def calculate(opposite, adjacent):
    # opposite and adjacent
    print(f"opposite = {opposite}")
    print(f"adjacent = {adjacent}")
    anglerad = math.atan(opposite/adjacent)
    print(f"angle = atan({opposite} / {adjacent}) = {math.degrees(anglerad)}undefined")


def calculate(adjacent, hypotenuse):
    # adjacent and hypotenuse
    print(f"adjacent = {adjacent}")
    print(f"hypotenuse = {hypotenuse}")
    anglerad = math.acos(adjacent/hypotenuse)
    print(f"angle = acos({adjacent}/{hypotenuse}) = {math.degrees(anglerad)}undefined")


def calculate(opposite, hypotenuse):
    # opposite and hypotenuse
    print(f"opposite = {opposite}")
    print(f"hypotenuse = {hypotenuse}")
    anglerad = math.asin(opposite/hypotenuse)
    print(f"angle = asin({opposite} / {hypotenuse}) = {math.degrees(anglerad)}undefined")


def calculate(anglerad, hypotenuse):
    # angle and hypotenuse
    print(f"angle = {math.degrees(anglerad)}undefined")
    print(f"hypotenuse = {hypotenuse}")
    opposite = hypotenuse * math.sin(anglerad)
    adjacent = hypotenuse * math.cos(anglerad)
    print(f"opposite = {hypotenuse} x sin({math.degrees(anglerad)}) = {opposite}")
    print(f"adjacent = {hypotenuse} x cos({math.degrees(anglerad)}) = {adjacent}")


def calculate(anglerad, adjacent):
    # angle and adjacent
    print(f"angle = {math.degrees(anglerad)} undefined")
    print(f"adjacent = {adjacent}")
    hypotenuse = adjacent / math.cos(anglerad)
    opposite = adjacent * math.tan(anglerad)
    print(f"hypotenuse = {adjacent} / cos({math.degrees(anglerad)}) = {hypotenuse}")
    print(f"opposite = {adjacent} x tan({math.degrees(anglerad)}) = {opposite}")

