import turtle as t
from datetime import datetime

t.bgcolor('black')
t.tracer(0)

def fundo (t, posx, posy, raio, color):
    t.pu()
    t.goto(posx, posy)
    for i in range(60):
        if i%5==0:
            t.width(3)
            d=0.2
        else:
            d=0.1
            t.width(1)
        t.fd(raio*(1-d))
        t.pd()
        t.fd(raio*d)
        t.pu()
        t.bk(raio)
        t.rt(360/60)
        
def ponteiro (t, posx, posy, raio, ang, width, color):
    t.ht()
    t.pu()
    t.goto(posx, posy)
    t.pd()
    t.seth(90)
    t.rt(ang)
    t.width(width)
    t.fd(raio)
    
posx=0
posy=0
raio=300
micro=1/1000000*6

while True:
    t.reset()
    
    now= datetime.now()
    h_ang= now.hour*30 + now.minute*0.5
    m_ang= now.minute*6 + now.second*0.1
    s_ang= now.second*6 + now.microsecond* micro
    
    fundo(t, posx, posy, raio, t.color('white'))
    ponteiro(t, posx, posy, raio*0.7, h_ang, 5, t.color('white'))
    ponteiro(t, posx, posy, raio*0.9, m_ang, 5, t.color('white'))
    ponteiro(t, posx, posy, raio, s_ang, 2, t.color('red'))
    
    t.update()