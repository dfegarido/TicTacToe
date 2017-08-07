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
    orientation:'vertical'
    rows: 3
    
    Label:
        text: 'Tic-Tac-Toe Game' 
    
    GridLayout:
        cols:3
        rows:3
        Button:
            id: set_1
            display: 1
            text: 
            on_press: root.main('set_1');
        Button:
            id: set_2
            display: 2
            text:
            on_press: root.main('set_2')
        Button:
            id: set_3
            display: 3
            text:
            on_press: root.main('set_3')
        Button:
            id: set_4
            display: 4
            text:
            on_press: root.main('set_4')
        Button:
            id: set_5
            display: 5
            text:
            on_press: root.main('set_5')
        Button:
            id: set_6
            display: 6
            text:
            on_press: root.main('set_6')
        Button:
            id: set_7
            display: 7
            text:
            on_press: root.main('set_7')
        Button:
            id: set_8
            display: 8
            text:
            on_press: root.main('set_8')
        Button:
            id: set_9
            display: 9
            text:
            on_press: root.main('set_9')

''')


class RootWidget(GridLayout):
    
    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.player_one = False
        self.player_cpu = False
        self.coordinate = []
        
        
         
    #check if whos turn
    def turn(self):
        
        one = self.player_one
        cpu = self.player_cpu

        if(one == False):
            #print('done move for one')
            self.player_one = True
            self.player_cpu = False
            return 'O'
        else:
            #print('done move for cpu')
            self.player_cpu = True
            self.player_one = False
            return 'X'

    def list_move(self, num, mark):
        self.coordinate.append({num : mark})
        print(self.coordinate)
        
    
    def whos_win(self):
        list_win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9)(7,5,3)]
        
        
    
    def main(self, ids):
        
        x = self.ids[ids]
        x.disabled = True
        x.text = self.turn()
        
        num = ids
        mark = x.text
        
        self.list_move(x.display, mark)
        
        
        
        

         

class MainApp(App):

    def build(self):
        return RootWidget()



if __name__ == '__main__':
    MainApp().run()
