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
random_color = ["aliceblue", "antiquewhite", "aqua", "aquamarine", "azure", "beige", "bisque", "black", "blanchedalmond", "blue", "blueviolet", "brown", "burlywood", "cadetblue", "chartreuse", "coral", "cornflowerblue", "crimson", "cyan", "darkblue", "darkcyan", "darkgoldenrod", "darkgray", "darkgreen", "darkgrey", "darkkhaki", "darkmagenta", "darkolivegreen", "darkorange", "darkorchid", "darkred", "darksalmon", "darkseagreen", "darkslateblue", "darkslategray", "darkslategrey", "darkturquoise", "darkviolet", "deeppink", "deepskyblue", "dimgray", "dimgrey", "dodgerblue", "firebrick", "floralwhite", "forestgreen", "fuchsia", "gainsboro", "ghostwhite", "gold", "goldenrod", "gray", "green", "greenyellow", "grey", "honeydew", "indianred", "indigo", "ivory", "khaki", "lavender", "lavenderblush", "lawngreen", "lemonchiffon", "lightblue", "lightcoral", "lightcyan", "lightgoldenrodyellow", "lightgray", "lightgreen", "lightgrey", "lightpink", "lightsalmon", "lightseagreen", "lightskyblue", "lightslategray", "lightslategrey", "lightsteelblue", "lightyellow", "lime", "limegreen", "linen", "magenta", "maroon", "mediumaquamarine", "mediumblue", "mediumorchid", "mediumpurple", "mediumseagreen", "mediumslateblue", "mediumspringgreen", "mediumturquoise", "mediumvioletred", "midnightblue", "mintcream", "mistyrose", "moccasin", "navajowhite", "navy", "oldlace", "olive", "olivedrab", "orange", "orangered", "orchid", "palegoldenrod", "palegreen", "paleturquoise", "palevioletred", "papayawhip", "peachpuff", "peru", "plum", "powderblue", "purple", "rebeccapurple", "red", "rosybrown", "royalblue", "saddlebrown", "salmon", "sandybrown", "seagreen", "seashell", "sienna", "silver", "skyblue", "slateblue", "slategray", "slategrey", "snow", "springgreen", "steelblue", "tan", "teal", "thistle", "tomato", "turquoise", "violet", "wheat", "white", "whitesmoke", "yellow", "yellowgreen"]
plate_color = random.choice(random_color)


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



wn = trtl.Screen()
wn.mainloop()