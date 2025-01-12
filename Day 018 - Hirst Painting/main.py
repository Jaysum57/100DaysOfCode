# import colorgram
# # Extract 6 colors from an image.
# colors = colorgram.extract('Day 018 - Hirst Painting\hirst_painting.jpg', 25)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))
# print(rgb_colors)

import random
from turtle import Turtle, Screen, colormode

rgb_colors = [
    (199, 175, 117),(124, 36, 24),(210, 221, 213),
    (168, 106, 57),(222, 224, 227),(186, 158, 53),(6, 57, 83),
    (109, 67, 85),(113, 161, 175),(22, 122, 174),(64, 153, 138),
    (39, 36, 36),(76, 40, 48),(9, 67, 47),(90, 141, 53),
    (181, 96, 79),(132, 40, 42),(210, 200, 151),(141, 171, 155),
    (179, 201, 186),(172, 153, 159),(212, 183, 177),(176, 198, 203),
]

colormode(255)

tim = Turtle()
tim.teleport(-400,-300)
tim.hideturtle()

def draw_painting(num_dots):
    for _ in range(num_dots+1):
        tim.teleport(-400, y = tim.ycor() + 50)
        for _ in range(num_dots+1):
            tim.dot(20, random.choice(rgb_colors))
            tim.teleport(x= tim.xcor() + 50)

draw_painting(10)

Screen().exitonclick()