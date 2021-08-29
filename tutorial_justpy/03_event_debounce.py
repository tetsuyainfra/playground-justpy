
import justpy as jp

# マウスの感度的なのを制御する
def mouse_event(self, msg):
    try:
        self.counter += 1
    except:
        self.counter = 1
    msg.page.info_div.add_first(jp.Div(text=f'{self.counter}) {msg.event_type}'))

def debounce_test():
    wp = jp.WebPage()
    d = jp.Div(style='height: 100vh', a=wp)
    d.add_event('mousemove')
    d.on('mousemove', mouse_event, throttle=1000)
    d.on('click', mouse_event, debounce=2000, immediate=False)
    wp.info_div = jp.Div(text='Recent mouse events', classes='m-4 text-lg', a=d)
    return wp

jp.justpy(debounce_test)