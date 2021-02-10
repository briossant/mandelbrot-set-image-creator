from PIL import Image
import os

default_inter = {
    're_start': -0.5,
    're_end': 0,
    'im_start': 0.5,
    'im_end': -0.5
}


def mandelbrot_fct(c, max_iteration):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iteration:
        z = z * z + c
        n += 1
    return n


def px_calculator(l=400, h=400, name='img', is_save=True, inter=None, max_iteration=80, colors=None):
    if colors is None:
        colors = [255, 0, 255]
    if inter is None:
        inter = default_inter

    print('start')
    img = Image.new('RGB', (l, h))
    for x in range(-l // 2, l // 2):
        print("\rProgress :" + str(round((x + l // 2) * l / (l * h) * 100, 3)) + "%", end="")
        for y in range(-h // 2, h // 2):
            c = complex(inter['re_start'] + (x / l) * (inter['re_end'] - inter['re_start']),
                        inter['im_start'] + (y / h) * (inter['im_end'] - inter['im_start']))
            m = mandelbrot_fct(c, max_iteration)
            r = int((colors[0] * (m / 255)) % 255)
            g = int((colors[1] * (m / 255)) % 255)
            b = int((colors[2] * (m / 255)) % 255)
            img.putpixel((x + l // 2, y + h // 2), (r, g, b))

    if is_save:
        name = "./images/" + name + ".jpg"
        img.save(name)
        os.system("xdg-open " + name)
    else:
        img.show()

