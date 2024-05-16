from math import sin,cos,tan,radians
angulo = float(input('Informe um angulo '))
rad = radians(angulo)
s = sin(rad)
c = cos(rad)
t = tan(rad)
print('O angulo {} tem seno {:.2f} cosseno {:.2f} e tangente {:.2f}'.format(angulo,s,c,t))