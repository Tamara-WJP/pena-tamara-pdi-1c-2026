import py5


def setup():
    py5.size(600, 600)
    py5.background("#C1BCCF")  # color fondo


def draw():
    if py5.is_mouse_pressed:
        dibujar()


def dibujar():
    py5.no_stroke()
    py5.fill("#19B4A0")  # color pincel
    py5.circle(py5.mouse_x, py5.mouse_y, 30)


py5.run_sketch()