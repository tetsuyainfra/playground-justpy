import justpy as jp

# こうすれば同じページはリクエスト毎に作成されない

wp = jp.WebPage(delete_flag=False)
my_paragraph_design = "w-64 bg-blue-500 m-2 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
for i in range(1,11):
    jp.P(text=f'{i}) Hello World!', a=wp, classes=my_paragraph_design)

# こいつがリクエスト毎に呼び出される
def hello_world():
    return wp

jp.justpy(hello_world)