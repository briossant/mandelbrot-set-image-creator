from PIL import Image, ImageDraw
import os

default_inter = {
    're_start': 0,
    're_zoom': 1,
    'im_start': 0,
    'im_zoom': 1
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
        colors = [255, 1, 255]
    if inter is None:
        inter = default_inter

    print('start')
    img = Image.new('HSV', (l, h))
    draw = ImageDraw.Draw(img)

    for x in range(-l // 2, l // 2):
        print("\rProgress :" + str(round((x + l // 2) * l / (l * h) * 100, 3)) + "%", end="")
        for y in range(-h // 2, h // 2):
            c = complex(inter['re_start'] + (x / l) / inter['re_zoom'],
                        inter['im_start'] + (y / h) / inter['im_zoom'])
            m = mandelbrot_fct(c, max_iteration)
            hue = int(255 * m / (max_iteration / colors[1]) + colors[0]) % 255
            saturation = colors[2]
            value = colors[2] if m < max_iteration else 0
            draw.point((x + l // 2, y + h // 2), (hue, saturation, value))

    img = img.convert('RGB')
    if is_save:
        name = "./images/" + name + ".jpg"
        img.save(name)
        os.system("xdg-open " + name)
    else:
        img.show()

