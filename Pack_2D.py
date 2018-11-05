# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as ptc
from random import *
from decimal import Decimal
 
class Container:
    def __init__(self,l,h):
        self.l = l
        self.h = h
 
 
class Objeto:
    def __init__(self,l,h,real):
        self.l = l
        self.h = h
        self.real = real;
 
    def position(self,x,y):        
        self.x = x
        self.y = y
 
 
def roulette(objs,l,h):
    i=0
    while i<len(objs) and (objs[i].h > h or objs[i].l > l):
        i+=1
    if i==len(objs):
        return False
    freq1=0
    freq2=0
    rep1=0
    rep2=0
    while i<len(objs):
        while objs[i].h == objs[freq1].h and objs[i].l == objs[freq1].l:
            rep1+=1
            i+=1
            if i==len(objs):
                break
        if i<len(objs):          
            aux = i
            repaux = 1
            while objs[i].h == objs[aux].h and objs[i].l == objs[aux].l:
                repaux+=1
                i+=1
                if i==len(objs):
                    break
            if(repaux > rep1):
                freq2, freq1 = freq1, aux
                rep2, rep1 = rep1, repaux
            elif(repaux > rep2):
                freq2 = aux
                rep2 = repaux
    if freq2 == 0:
        objs[freq1].real = False
        return objs[freq1]
    x = rep1/(rep1+rep2)
    if random() < x:
        objs[freq1].real = False
        return objs[freq1]
    else:
        objs[freq2].real = False
        return objs[freq2]      
 
 
def criar_objetos(lista):
    n = len(lista)
    lista1 = []
    for p in range(n):
        x = Objeto(lista[p][1],lista[p][0],True)
        x.position(0.0,0.0)     
        lista1.append(x)
    return lista1
 
def criar_container(objs,objsAux,cont,idcont,saveorshow):
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect = 'equal')
    plt.xlim(0,cont1.l)
    plt.ylim(0,cont1.h)
    plt.title('Container{0}'.format(idcont))
    realarea = 0
    virtualarea = 0
    container = []
    h = 0
    n = 0
    line_highest_height = 0
    l_length = 0
    full = False
    lines = []
    line = "Container "+str(idcont)+"\n\n"
    lines.append(line)
    while len(objs) > 0 and not full:        
        if l_length + objs[0].l <= cont.l and objs[0].h + h <= cont.h:
            objs[0].position(l_length,h)
            l_length += objs[0].l
            current = objs.pop(0)
            container.append(current)
            n+=1
            line = str(current.l)+" "+str(current.h)+" "+str(current.x)+" "+str(current.y)+"\n"
            lines.append(line)
            realarea += current.l * current.h
            ax1.add_patch(
              ptc.Rectangle(
                  (current.x, current.y),
                  current.l,
                  current.h,
                  edgecolor = 'black'
              )
            )
        else:
            if(l_length < cont.l):
                i = 1
                while i < len(objs):
                    if l_length + objs[i].l <= cont.l and objs[i].h <= container[line_highest_height].h:
                        objs[i].position(l_length,h)
                        l_length += objs[i].l
                        current = objs.pop(i)
                        container.append(current)
                        n+=1
                        line = str(current.l)+" "+str(current.h)+" "+str(current.x)+" "+str(current.y)+"\n"
                        lines.append(line)
                        realarea += current.l * current.h
                        ax1.add_patch(
                          ptc.Rectangle(
                              (current.x, current.y),
                              current.l,
                              current.h,
                              edgecolor = 'black'
                          )
                        )
                    else:
                        i+=1
                         
                objec = 1
                while objec:
                    objec = roulette(objsAux, cont.l-l_length, container[line_highest_height].h)
                    if(objec):
                        objec.position(l_length,h)
                        l_length += objec.l
                        container.append(objec)
                        n+=1
                        line = str(objec.l)+" "+str(objec.h)+" "+str(objec.x)+" "+str(objec.y)+" (roleta)"+"\n"
                        lines.append(line)
                        virtualarea += objec.l * objec.h
                        ax1.add_patch(
                          ptc.Rectangle(
                              (objec.x, objec.y),
                              objec.l,
                              objec.h,
                              hatch = '/',
                              facecolor = 'none',
                              edgecolor = 'black'
                          )
                        )
 
            h = container[line_highest_height].y + container[line_highest_height].h
            l_length = 0
            line_highest_height = n
            if h + objs[0].h <= cont.h:              
                objs[0].position(l_length,h)
                l_length += objs[0].l
                current = objs.pop(0)
                container.append(current)               
                n+=1
                line = str(current.l)+" "+str(current.h)+" "+str(current.x)+" "+str(current.y)+"\n"
                lines.append(line)
                realarea += current.l * current.h
                ax1.add_patch(
                  ptc.Rectangle(
                      (current.x, current.y),
                      current.l,
                      current.h,
                      edgecolor = 'black'
                  )
                )
            else:
                i = 1
                fits = False
                while i < len(objs) and not fits:
                    if h + objs[i].h <= cont.h:              
                        objs[i].position(l_length,h)
                        l_length += objs[i].l
                        current = objs.pop(i)
                        container.append(current)               
                        n+=1
                        fits = True
                        line = str(current.l)+" "+str(current.h)+" "+str(current.x)+" "+str(current.y)+"\n"
                        lines.append(line)
                        realarea += current.l * current.h
                        ax1.add_patch(
                          ptc.Rectangle(
                              (current.x, current.y),
                              current.l,
                              current.h,
                              edgecolor = 'black'
                          )
                        )
                    else:
                        i+=1
                if not fits:
                    objec = roulette(objsAux, cont.l, cont.h-h)
                    if(objec):
                        objec.position(l_length,h)
                        l_length += objec.l
                        container.append(objec)
                        n+=1
                        line = str(objec.l)+" "+str(objec.h)+" "+str(objec.x)+" "+str(objec.y)+"\n"
                        lines.append(line)
                        virtualarea += objec.l * objec.h
                        ax1.add_patch(
                          ptc.Rectangle(
                              (objec.x, objec.y),
                              objec.l,
                              objec.h,
                              hatch = '/',
                              facecolor = 'none',
                              edgecolor = 'black'
                          )
                        )
                    else:
                        full = True
     
    while not full:
        objec = roulette(objsAux, cont.l-l_length, container[line_highest_height].h)
        if objec:
            objec.position(l_length,h)
            l_length += objec.l
            container.append(objec)
            n+=1
            line = str(objec.l)+" "+str(objec.h)+" "+str(objec.x)+" "+str(objec.y)+" (roleta)"+"\n"
            lines.append(line)
            virtualarea += objec.l * objec.h
            ax1.add_patch(
              ptc.Rectangle(
                  (objec.x, objec.y),
                  objec.l,
                  objec.h,
                  hatch = '/',
                  facecolor = 'none',
                  edgecolor = 'black'
              )
            )
 
        else:
            h = container[line_highest_height].y + container[line_highest_height].h
            l_length = 0
            line_highest_height = n
            objec = roulette(objsAux, cont.l, cont.h-h)
            if objec:               
                objec.position(l_length,h)
                l_length += objec.l
                container.append(objec)
                n+=1
                line = str(objec.l)+" "+str(objec.h)+" "+str(objec.x)+" "+str(objec.y)+" (roleta)"+"\n"
                lines.append(line)
                virtualarea += objec.l * objec.h
                ax1.add_patch(
                  ptc.Rectangle(
                      (objec.x, objec.y),
                      objec.l,
                      objec.h,
                      hatch = '/',
                      facecolor = 'none',
                      edgecolor = 'black'
                  )
                )
            else:
                full = True
             
    lines.append("\n\n")
    arq1.writelines(lines)
    if saveorshow == 0:
      fig1.savefig('Container{0}.png'.format(idcont))
    elif saveorshow == 1:
      fig1.show()
    elif saveorshow == 2:
      fig1.savefig('Container{0}.png'.format(idcont))
      fig1.show()
    sobra = (cont.l * cont.h) - (realarea + virtualarea)
    return container, objs, realarea, virtualarea, sobra
 
def criar_conjunto(objs,cont,saveorshow):
    objsAux = objs[:]
    conjunto = []
    i = 1
    container,restantes,realarea,virtualarea,sobra = criar_container(objs,objsAux,cont,i,saveorshow)
    conjunto.append(container)
    while len(restantes) > 0:
        i+=1
        container,restantes,realarea0,virtualarea0,sobra0 = criar_container(objs,objsAux,cont,i,saveorshow)
        conjunto.append(container)
        realarea += realarea0
        virtualarea += virtualarea0
        sobra += sobra0
    return conjunto
 
arq = open('item.txt','r')
arq1 = open('packed.txt','w')
objs = arq.read().splitlines()
arq.close()
x = len(objs)
i = 0
while i < x:
    if not objs[i]:
        objs.pop(i)
        x-=1
    else:
        i+=1
x = len(objs)
for i in range(x):
    objs[i] = objs[i].split()
    for j in range(2):
        objs[i][j] = Decimal(objs[i][j])
    objs[i][0],objs[i][1] = objs[i][1],objs[i][0]
 
objs.sort(reverse = True)
objs1 = criar_objetos(objs)
 
saveorshow = int(input("Digite: \n 0 - Para salvar as imagens \n 1 - Para apenas mostrar as imagens \n 2 - Para mostrar as imagens e salvar \n 3 - Para não gerar imagens\n Entrada: "))
 
cont1 = Container(10,10)
allconts = criar_conjunto(objs1,cont1,saveorshow)
 
arq1.close()
 
#eof = input("\nPressione Enter para encerrar...")
