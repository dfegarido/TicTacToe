from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config

Config.set("graphics","width","500")
Config.set("graphics","height","500")
Config.set("graphics","borderless","0")




Builder.load_string('''
<Cstm@Button>
    font_size:"80dp"


<RootWidget>
    id:tictac
    rows: 5
    
    BoxLayout:
        Label:
            id:text_label
            font_size:'40dp'
            text: 'Tic-Tac-Toe Games' 
    BoxLayout:
        Cstm:
            id:text_1
            text: ''
            on_press: text_1.text = "X"
        Cstm:
            id:text_2
            text: ''
            on_press: text_2.text = "X"
        Cstm:
            id:text_3
            text: ''
            on_press: text_3.text = "X"

    BoxLayout:
        Cstm:
            id:text_4
            text: ''
            on_press: text_4.text = "X"
        Cstm:
            id:text_5
            text: ''
            on_press: text_5.text = "X"
        Cstm:
            id:text_6
            text: ''
            on_press: text_6.text = "X"
    BoxLayout:
        Cstm:
            id:text_7
            text: ''
            on_press: text_7.text = "X"
        Cstm:
            id:text_8
            text: ''
            on_press: text_8.text = "X"
        Cstm:
            id:text_9
            text: ''
            on_press: text_9.text = "X"

    BoxLayout:
        Label:
            font_size:'30dp'
            text: "O : 10"
        Button:
            font_size:'30dp'
            text: "Start"
        Label:
            font_size:'30dp'
            text: "X : 10"
        


''')


class RootWidget(GridLayout):
    pass




class MainApp(App):

    def build(self):
        return RootWidget()



if __name__ == '__main__':
    MainApp().run()
