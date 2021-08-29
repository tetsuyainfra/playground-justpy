
import justpy as jp

def my_click(self, msg):
    self.text = 'I was clicked'

def event_demo():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click)
    return wp

def my_click2(self, msg):
    # self.text = 'I was clicked'
    # print(msg.event_type)    # click
    # print(msg['event_type']) # click
    print(msg)               # {'event_type': 'click, 'id': 1, ....}

def event_demo2():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet@my_click2', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click2)
    # 追加のイベントプロパティを追加する
    d.additional_properties =['screenX', 'pageY','altKey','which','movementX','button', 'buttons']

    return wp

def my_click3(self, msg):
    self.num_clicked += 1
    self.text = f'I was clicked {self.num_clicked}'
    # print(msg.event_type)    # click
    # print(msg['event_type']) # click
    print(msg)               # {'event_type': 'click, 'id': 1, ....}

def event_demo3():
    wp = jp.WebPage()
    d = jp.Div(text='Not clicked yet@my_click2', a=wp, classes='w-48 text-xl m-2 p-1 bg-blue-500 text-white')
    d.on('click', my_click3)
    d.num_clicked = 0

    return wp

# jp.justpy(event_demo)
# jp.justpy(event_demo2)
jp.justpy(event_demo3)