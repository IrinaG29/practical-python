# Exercise 1.5

height = 100
counter = 1

while counter < 11:
    bounce = (3 * height) / 5
    height = bounce
    print(counter, round(bounce, 4))
    counter = counter + 1
