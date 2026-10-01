import turtle as trtl

import turtle as trtl
wn = trtl.Screen()
custom_polygon = ((0, 0), (1, 2), (3, 5), (4, 5), 
                  (4, 6), (4, 7), (7, 4), (6, 4), (5, 4), (5, 3), (2,1), (0,0))
wn.register_shape("pipingbag", custom_polygon)

my_turtle = trtl.Turtle()
my_turtle.shape("pipingbag")
my_turtle.color("black")
my_turtle.fillcolor("white")


import random
random_color = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "coral", "cornflowerblue", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue", "purple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
plate_color = random.choice(random_color)

number_list = [1,2,3,4,5,6,7,8,9,10]

flavor_list = ["chocolate", "vanilla", "strawberry"]
flavor_color = ["chocolate","cornsilk","pink"]

my_turtle.penup()
my_turtle.left(180)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.pendown()
my_turtle.fillcolor(plate_color)

def draw_oval(radius):
    for _ in range(2):
        my_turtle.circle(radius, 90)     
        my_turtle.circle(radius / 8, 90) 


my_turtle.left(45) 
my_turtle.begin_fill()
draw_oval(250)
my_turtle.end_fill()

cake_color = trtl.textinput("cake flavor","what type of cake do you want? (chocolate, vanilla, or strawberry)")
cake_color = cake_color.lower()
while cake_color not in flavor_list:
    cake_color = trtl.textinput("cake flavor","what type of cake do you want? (chocolate, vanilla, or strawberry)")
    cake_color = cake_color.lower()

cakecolor_index = flavor_list.index(cake_color)
my_turtle.fillcolor(flavor_color[cakecolor_index])

number_of_layers = trtl.textinput("Number of ckae layers","how many layers do you want for your cake? (1-6)")

while int(number_of_layers) > 6:
    number_of_layers = trtl.textinput("Number of ckae layers","how many layers do you want for your cake? (1-6)")
#print(number_of_layers)

my_turtle.penup()
my_turtle.left(45)
my_turtle.forward(285)
my_turtle.left(90)
my_turtle.forward(35)
my_turtle.pendown()
my_turtle.forward(25)
my_turtle.left(90)

for layers in range(int(number_of_layers)):
    my_turtle.begin_fill()
    for _ in range(2):
        my_turtle.forward(200)
        my_turtle.left(90)
        my_turtle.forward(50)
        my_turtle.left(90)
    my_turtle.right(90)
    if int(number_of_layers) -1 > layers:
        my_turtle.forward(50)
    my_turtle.left(90)

    my_turtle.end_fill()

candle_fire = trtl.textinput("candles","Do you want your candles lit?")

my_turtle.right(90)
for candle in range(random.choice(number_list)):
    for _ in range(2):
        my_turtle.forward(30)
        my_turtle.left(90)
        my_turtle.forward(10)
        my_turtle.left(90)
    my_turtle.forward(30)
    if candle_fire == "yes":
        my_turtle.fillcolor("orange")
        my_turtle.begin_fill()
        my_turtle.circle(5)
        my_turtle.end_fill()
    my_turtle.right(180)
    my_turtle.forward(30)
    my_turtle.setheading(0)
    my_turtle.left(180)
    my_turtle.forward(20)
    my_turtle.setheading(90)


    
#Making sprinkles

#print(my_turtle.xcor(),my_turtle.ycor())
sprinkles = trtl.textinput("Sprinkes","do you want sprinkles")
#print(sprinkles)
if sprinkles != None and sprinkles.lower() == "yes":
    my_turtle.pensize(5)
    my_turtle.speed(90)
    for sprinkle in range(100):
        x_position = random.randint(-55,125)
        y_position = random.randint(-25, 150)
        my_turtle.penup()
        my_turtle.goto(int(x_position), int(y_position))
        my_turtle.setheading(random.randint(0, 360))
        my_turtle.pencolor(random.choice(random_color))
        my_turtle.pensize(3)
        my_turtle.pendown()
        my_turtle.forward(10)
    my_turtle.pensize(1)
my_turtle.speed(5)


    


wn = trtl.Screen()
wn.mainloop()