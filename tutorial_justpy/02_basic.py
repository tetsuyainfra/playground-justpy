import justpy as jp

def hello_world():
    # webpageを作って
    wp = jp.WebPage()

    # p要素クラスを作って
    p = jp.P(text='Hello World!')

    # webpageにぶちこむ
    wp.add(p)  # Same as p.add_to(wp), wp = wp + p, wp += p

    return wp

def hello_world2():
    wp = jp.WebPage()
    for i in range(1,11):
        jp.P(text=f'{i}) Hello World!', a=wp, style=f'font-size: {10*i}px')
    return wp

# jp.justpy(hello_world)
jp.justpy(hello_world2)


