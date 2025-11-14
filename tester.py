import geo.utils as utils

# calculate the length of hypotenuse
a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

# calculate the area of circle
r = 10
area = utils.circle(r)
print('area =', area)
