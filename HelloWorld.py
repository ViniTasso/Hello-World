# -*- coding: utf-8 -*-

import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.button import Button

#Referência:   
#https://www.letscode.com.br/blog/kivy-criando-apps-em-python
#O Android.txt é necessário para rodar em celular, contem informaçoes sobre orientação do app autor etc.
kivy.require('1.9.1')

var = 0
def soma_um(instance):
    global var
    var += 2
    instance.text = instance.text + str(var)    
    
class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                padding=[40, 20, 40, 20])
        
        layout.add_widget(Label(text='Hello by Kivy!'))
        layout.add_widget(Label(text='New Label!'))
        btn = Button(text='Pressione-me!', size=(100,50))
        
        btn.bind(on_press=soma_um)
        layout.add_widget(btn)
        return layout 
    
if __name__ == '__main__':
    MeuApp().run()