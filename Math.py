from tkinter import *
from calculadora import Calculadora as C

class window:
  def __init__(self):
    self.window()

  def window(self):
    self.window=Tk()
    self.window.title("Calculadora")
    self.window.geometry("500x410")
    self.window.configure(background="#00091a")
    self.label()
    self.button()
    self.lines(self.label())
    self.window.mainloop()

  def label(self):
    label=Label(self.window,background="#0A1530")
    label.place(x=0,y=2,width=500,height=280)
    return label
  
  def lines(self,window):
    global canvas
    canvas=Canvas(self.window,height=280,width=500,bg='#0a1530',bd=0,highlightthickness = 0)
    linex=canvas.create_line(0,140,500,140,fill="#00b8ff",dash = (5, 2))
    liney=canvas.create_line(250,0,250,280,fill="#00b8ff",dash = (5, 2))
    canvas.pack()

  def button(self):
      button_media=Button(self.window,text="P-médio", background="#020015",foreground="white",highlightthickness = 0, bd = 0, command=lambda:[self.entry('médio'),self.press_button('médio')]).place(x=0,y=285,width=90,height=60)

      button_extremo=Button(self.window,text="P-extremo",background="#020015",foreground="white",highlightthickness = 0, bd = 0, command=lambda:[self.entry('extremo'),self.press_button('extremo')]).place(x=0,y=350,width=90,height=60)

      button_baricentro=Button(self.window,text="P-Baricentro",background="#020015",foreground="white",highlightthickness = 0, bd = 0, command=lambda:[self.entry('baricentro'),self.press_button('baricentro')]).place(x=95,y=285,width=90,height=60)

      button_triangulo=Button(self.window,text="P-Triangulo",background="#020015",foreground="white",highlightthickness = 0, bd = 0, command=lambda:[self.entry('triangulo'),self.press_button('triangulo')]).place(x=95,y=350,width=90,height=60)

  def press_button(self,button_press):
      global press
      press=None
      if button_press=="médio":
        press="médio"
      elif button_press=="extremo":
        press="extremo"
      elif button_press=="triangulo":
        press="triangulo"
      elif button_press=="baricentro":
        press="baricentro"

  def apagar_widget(self, modo='str'):
    canvas.delete('lines')
    lista_place = self.window.place_slaves()

    if modo == "str":
      for widget in lista_place:
        
        if str(widget) == '.!label2':
          break
        else:
          widget.destroy()
    else:
      for widget in lista_place:
        
        if str(type(widget)) == "<class 'tkinter.Button'>":
          break
        else:
          widget.destroy()


  def entry(self, evento):
    eventos = {'médio': ['x, y do ponto 1:', 'x, y do ponto 2:'],
               'extremo': ['x, y do ponto extremo:', 'x, y do ponto médio:'],
               'baricentro': ['x, y do primeiro ponto:','x, y do segundo ponto:','x, y do terceiro ponto:'],
               'triangulo': ['x, y do primeiro ponto:', 'x, y do segundo ponto:', 'x, y do baricentro:']
               }

    self.apagar_widget()
    lista_eventos = eventos[evento]

    text = max(lista_eventos, key=len)
    tamanho = len(text)
    
    tamanho_label = tamanho * 6 +50
    x, y = 210, 315

    for c in range(len(lista_eventos)):
      Label(self.window, text=lista_eventos[c],background="#091933",foreground="white").place(x= x,y= y,width=tamanho_label,height=20)
      e = Entry(self.window)
      e.bind('<Return>', lambda e: self.calcular())
      e.place(x= x +tamanho_label,y= y,width=50,height=20)
      y+=25
    
    Button(self.window, text="Calcular", command= lambda:self.calcular()).place(x= x +tamanho_label-10,y= y,width=60,height=20)

   
  def pegar_valores(self):
    lista_place = self.window.place_slaves()

    valores = []
    for widget in lista_place:
      if str(type(widget)) == "<class 'tkinter.Entry'>":
        valores.append(widget.get())

    return valores

  def calcular(self):
    self.apagar_widget('type')
    values=self.pegar_valores()
    new_val=[]
    for i in values:
      new_val.append(i.split(","))
    print(press,"-",new_val)
    if press=="médio":
      result=C.ponto_medio(self,float(new_val[1][0]),float(new_val[0][0]),float(new_val[1][1]),float(new_val[0][1]))

      self.pos(result,(float(new_val[1][0]),float(new_val[0][0])),(float(new_val[1][1]),float(new_val[0][1])))

    elif press=="extremo":
      result=C.coordenadas_extremo(self,float(new_val[1][0]),float(new_val[0][0]),float(new_val[1][1]),float(new_val[0][1]))
      print('resultado-',result)
      self.pos(result,(float(new_val[1][0]),float(new_val[0][0])),(float(new_val[1][1]),float(new_val[0][1])))

    elif press=="baricentro":
      result=C.baricentro(self,float(new_val[2][0]),float(new_val[1][0]),float(new_val[0][0]),float(new_val[2][1]),float(new_val[1][1]),int(new_val[0][1]))

      self.pos(result,(float(new_val[2][0]),float(new_val[1][0]),float(new_val[0][0])),(float(new_val[2][1]),float(new_val[1][1]),float(new_val[0][1])))

    elif press=="triangulo":
      result=C.coordenadas_triangulo(self,float(new_val[0][0]),float(new_val[1][0]),float(new_val[2][0]),float(new_val[0][1]),float(new_val[1][1]),float(new_val[2][1]))

      self.pos(result,(float(new_val[0][0]),float(new_val[1][0]),float(new_val[2][0])),(float(new_val[0][1]),float(new_val[1][1]),float(new_val[2][1])))

    self.LabelResult(press, result)

  

  def LabelResult(self, press, result):
    print(type(result))
    Label(self.window, text=f'{press} = {result}', foreground="#e601d5", background='#020015').place(x=220,y=285,height=20)

  def pos(self,value,*result):
    dicty={'x1':'','y1':'','x2':'','y2':'','x_result':'','y_result':''}

    
    if press=="médio" or press=="extremo":
    
      dicty.update({'x1':result[0][0],'y1':result[1][0],'x2':result[0][1],'y2':result[1][1],'x_result':value[0],'y_result':value[1]})

    elif press=="triangulo" or press=="baricentro":

      dicty.update({'x1':result[0][0],'y1':result[1][0],'x2':result[0][1],'y2':result[1][1],'x3':result[0][2],'y3':result[1][2],'x_result':value[0],'y_result':value[1]})

    x_base,y_base=240,135


    distancia_x = 35
    distancia_y = 20

    c_x = 0
    c_y = 0

    print(dicty)
    for key, value in dicty.items():
      #escrever no x
      if key in ['x1','x2','x3','x_result']:
        if key=='x_result':
            print('resultado', dicty[key])
            colour='#e601d5'
        else:
            # colour='#feff6e'
            colour = "#feff6e"
            c_x+=1
        
        #negativo
        if value<0:
          x = x_base + (value * distancia_x)+5
          print(value, '-x:',x, c_x)
          Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=x,y=y_base,width=30,height=10)

        elif value>0:
          x = x_base + (value * distancia_x)+5
          print(value, 'x:',x, c_x)
          Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=x + 5,y=y_base,width=30,height=10)
        
        elif dicty['x_result'] == 0.0 or dicty[key] in [0.0,0]:
              x = x_base - (value * distancia_x)-5
              Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=235,y=135,width=30,height=10)

       
        
      #escrever no y
      elif key in['y1','y2','y3','y_result']:
        if key=="y_result":
            colour='#e601d5'
           
        else:
            # colour='#feff6e'
            colour = "#feff6e"
            c_y += 1
        #negativo
        if value<0:
          y = y_base - (value * distancia_y)-5
          print('-y:',y)
          Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=x_base,y=y,width=30,height=10) 
        
        elif dicty['y_result'] == 0.0 or dicty[key] in [0.0,0]:
              y = y_base - (value * distancia_y)-5
              Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=230,y=135,width=30,height=10)

        #positivo
        elif value>0:
          y = y_base - (value * distancia_y)+5
          print(value, 'y:',y)
          Label(self.window,text=value,background='#0a1530',foreground=colour).place(x=x_base,y=y,width=30,height=10)


        linex=canvas.create_line(x_base,y+5,x+15,y+5,fill=colour,tags='lines' ,dash = (5, 2)) #liney
        liney=canvas.create_line(x+15,y_base,x+15,y+5,fill=colour,tags='lines' ,dash = (5, 2)) #linex

        
           
      canvas.pack()

window()