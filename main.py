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
    
    Label:
        text: 'Tic-Tac-Toe Game' 
        
    BoxLayout:
        Cstm:
            id: set_1
            display: 1
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_2
            display: 2
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_3
            display: 3
            on_press: self.text = root.whos_turn(self.display)
    BoxLayout:
        Cstm:
            id: set_4
            display: 4
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_5
            display: 5
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_6
            display: 6
            on_press: self.text = root.whos_turn(self.display)
    BoxLayout:
        Cstm:
            id: set_7
            display: 7
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_8
            display: 8
            on_press: self.text = root.whos_turn(self.display)
        Cstm:
            id: set_9
            display: 9
            on_press: self.text = root.whos_turn(self.display)
    BoxLayout:
        Label:
            text: 'O = 1' 
        Button:
            text: 'Start Game'
            on_press: #root.start_game()
        Label:
            text: 'X = 5'
        


''')


class RootWidget(GridLayout):
    
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.turn = None # x or o
        self.color = None

    

    def cpu_brain(self):
        pass

    def start_game(self):
        root_widget = self.ids['set_1']
        root_widget.add_widget()

    def whos_turn(self, btn_id):
        set_id = 'set_{}'.format(btn_id)
        button = self.ids[set_id]
        button.disabled = True
        
        
        if self.turn == 'x' or self.turn == '':
            self.turn = 'o'
            self.color = (0,9,0,1)
        else:
            self.turn = 'x'
            self.color = (9,0,0,1)
        button.background_color = self.color   
        return self.turn
                
        
        
        
            
        
  
        
        




class MainApp(App):

    def build(self):
        return RootWidget()



if __name__ == '__main__':
    MainApp().run()
