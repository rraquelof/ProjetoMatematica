class Calculadora:
  def ponto_medio(self, x1, x2, y1, y2):
    return round((x1 + x2) / 2, 1),round((y1 + y2) / 2, 1)

  def coordenadas_extremo(self, x1, x2, y1, y2):
    x=(x2*2)-x1
    y=(y2*2)-y1
    return round(x, 1),round(y, 1)

  def baricentro (self, x1, x2, x3, y1, y2, y3):
    return round((x1 + x2 + x3) / 3, 1),round((y1 + y2 + y3) / 3, 1)    #baricentro

  def coordenadas_triangulo(self, x1, x2, x3, y1, y2, y3):
    x=(x1*3)-x2-x3
    y=(y1*3)-y2-y3

    return round(x, 1),round(y, 1)