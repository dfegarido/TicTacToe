from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.config import Config


Config.set("graphics","width","500")
Config.set("graphics","height","500")
Config.set("graphics","borderless","1")




Builder.load_string('''
<Cstm@Button>
    font_size:"80dp"
    

<RootWidget>
    id:tictac
    orientation:'vertical'
    rows: 3
    
    Label:
        id: label
        text: 'Tic-Tac-Toe Game' 
        size_hint_y:None 
        height: '50dp'
    BoxLayout:
        orientation:'horizontal'
        size_hint_y:None
        height: '100dp'
        Button:
            id: start
            text: "Start"
            size_hint_y: None
            height: '30dp' 
            on_press: root.start()
        Button:
            id: close
            text: 'Exit'
            size_hint_y: None
            height: '30dp' 
            on_press: root.exit()
        
    
    GridLayout:
        cols:3
        rows:3
        padding: '10dp'
        spacing: '10dp'
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
        self.coordinate_one = []
        self.coordinate_cpu = []
        self.cpu_brain()
       
    #check if whos turn
    def turn(self, ids):
        
        one = self.player_one
        cpu = self.player_cpu

        if(one == False):
            #print('done move for one')
            self.player_one = True
            self.player_cpu = False
            self.coordinate_one.append(self.ids[ids].display)
            return 'X'
        else:
            #print('done move for cpu')
            self.player_cpu = True
            self.player_one = False
            self.coordinate_cpu.append(self.ids[ids].display)
            return 'O'

        
    def whos_win(self, x, o):
        
        list_win = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
        for one in x:
            if one in list_win:
                return 'One Player Win'

        for cpu in o:
            if cpu in list_win:
                return 'CPU Win'


		
    def check_coordinate(self):
        one = self.coordinate_one
        cpu = self.coordinate_cpu
        one.sort()
        cpu.sort()
        print(one)
        x = (tuple(one[:3]), tuple(one[1:]))
        o = (tuple(cpu[:3]), tuple(cpu[1:]))

        return self.whos_win(x, o)

    def cpu_brain(self):
        pass

    def start(self):
        self.player_one = False
        self.player_cpu = False
        self.coordinate_one = []
        self.coordinate_cpu = []
        for i in range(1,10):
            set = "set_" + str(i)
            self.ids[set].disabled = False
            self.ids[set].text = ''
            self.ids['label'].text = "Tic-Tac-Toe Game"

    def exit(self):
        exit()



    def main(self, ids):
        
        x = self.ids[ids]
        x.disabled = True
        x.text = self.turn(ids)
        game_output = self.check_coordinate()

        if game_output != None:
            self.ids['label'].text = game_output
            for i in range(1,10):
                set = 'set_' + str(i)
                self.ids[set].disabled = True


        

         

class MainApp(App):

    def build(self):
        return RootWidget()



if __name__ == '__main__':
    MainApp().run()
