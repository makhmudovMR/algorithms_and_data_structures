import graphics as gr

window = gr.GraphWin("Jenkslex and Ganzz project", 400, 400)

window.setBackground('black')



def draw_rocket():
    first_module = gr.Rectangle(gr.Point(100, 150), gr.Point(150, 250))
    first_module.setFill('white')

    second_module = gr.Polygon(gr.Point(100, 150), gr.Point(150, 150), gr.Point(125, 100))
    second_module.setFill('white')

    rocket_window = gr.Circle(gr.Point(125, 180), 15)
    rocket_window.setFill('#ccffff')

    base_rocket = gr.Polygon(gr.Point(100, 250), gr.Point(90, 270), gr.Point(160, 270), gr.Point(150, 250))
    base_rocket.setFill('white')

    first_module.draw(window)
    second_module.draw(window)
    rocket_window.draw(window)
    base_rocket.draw(window)

def draw_land():
    moon_land = gr.Rectangle(gr.Point(0, 200), gr.Point(400, 400))
    moon_land.setFill('gray')
    moon_land.draw(window)

def draw_earth():
    earth = gr.Circle(gr.Point(300, 100), 20)
    earth.setFill('blue')
    earth.draw(window)

def draw():
    draw_land()
    draw_rocket()
    draw_earth()


draw()



window.getMouse()
window.close()