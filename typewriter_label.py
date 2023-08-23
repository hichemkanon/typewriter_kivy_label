from kivy.app import App
from kivy.uix.label import Label
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.window import Window


class TypewriterLabel(Label):
    def __init__(self, cursor_size=30, 
        cursor_color='#3cff00',
        time_interval=.07,**kwargs):
        super(TypewriterLabel, self).__init__(**kwargs)

        self.typing_event = None
        #self.pos = (Window.width /2-(self.width /2), Window.height /2)
        self.halign = 'left'
        self.valign = 'top'
        self.markup = True
        self.size_hint = (1, 1)
        self.font_size = "22sp"       
        self.cursor_size = cursor_size
        self.cursor_color = cursor_color
        self.padding = [10, 5]
        self.texto = ''
        self.time_interval = time_interval
        self.bind(size=self.setter('text_size'))
    ct = 0 
    def start_typing(self, text):
        self.text = ""
        global ct
        #self.typing_animation = Animation(opacity=1, duration=0.1)
        #self.typing_animation.start(self)
        
        def add_text(dt):
            if self.text == text or self.texto == text:
                self.typing_event.cancel()
            else:                
                self.texto = self.texto + text[len(self.texto)]
                printed = f"[size={self.cursor_size}][b][color=000000]|[/color][/b][/size]" if len(self.texto) % 2 == 1 else f"[size={self.cursor_size}][b][color={self.cursor_color}]|[/color][/b][/size]"
                self.text = self.texto + printed
           

        self.typing_event = Clock.schedule_interval(add_text, self.time_interval)


class TypewriterApp(App):
    def build(self):
        label = TypewriterLabel()
        label.start_typing("def clone_widget(widget): \n    clone = type(widget)()  # Create a new instance of the same class\n    clone.__dict__.update(widget.__dict__)  # Copy properties from the original widget\n    return clone")
        return label

if __name__ == '__main__':
    TypewriterApp().run()
