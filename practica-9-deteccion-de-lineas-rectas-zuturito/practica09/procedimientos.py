import math
import numpy as np
from auxiliar import *

try:
    import cv2
except:
    pass

def etiquetado_de_notas(img, componentes):
    font = cv2.FONT_HERSHEY_SIMPLEX 
    fontScale = .5
    color = (0, 0, 255) 
    thickness = 1
    _, bina = cv2.threshold(img,185,255,cv2.THRESH_BINARY)
    edges = cv2.Canny(bina,50,150,apertureSize = 3)
    minimoVal=1250
    maximo_valLine=55
    lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=100,lines=np.array([]), minLineLength=minimoVal,maxLineGap=maximo_valLine)
    a,b,c = lines.shape
    mascara_img=np.zeros((img.shape[0],img.shape[1]), dtype='i')
    img2 = cv2.imread("salida_etiquetas.png")
    lineas=0
    bandera_checa=False
    for i in range(a):
        x1=lines[i][0][0]
        y1=lines[i][0][1]
        x2=lines[i][0][2]
        y2=lines[i][0][3]
        org = (x1, y1)
        text = str(y1)
        img2=cv2.line(img2,(x1,y1+1),(x2,y2+1),(0, 0, 255), 1, cv2.LINE_AA) 
        img2 = cv2.putText(img2, text, org, font, fontScale, color, thickness, cv2.LINE_AA, False)
        for j in range(len(mascara_img[i])):
            mascara_img[y1][j]=1
    u, indices = np.unique(componentes, return_inverse=True)
    bandera_checa=False
    notas= []
    for i in range(len(u)-1):
        notas.append("")
    cont=0
    compas=1
    for i in range(len(mascara_img)):
        bandera_checa=False
        for j in range(len(mascara_img[i])):
            pixelmascara=mascara_img[i][j]
            if pixelmascara ==1:
                bandera_checa=True          
        if bandera_checa==True:
            if cont == 0:
                maximo_val=0
                minimo=0
                k=0
                for k in range(11):
                    if k == 0:
                        minimo=i-8
                        maximo_val = i
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="G5"
                    if k==1:
                        minimo=maximo_val
                        maximo_val = maximo_val+3
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="F5"
                    if k==2:
                        minimo=maximo_val
                        maximo_val = maximo_val+11
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="E5"
                    if k==3:
                        minimo=maximo_val
                        maximo_val = maximo_val+5
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="D5"
                    if k == 4:
                        minimo=maximo_val-1
                        maximo_val = maximo_val+11
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="C5"
                    if k == 5:
                        minimo=maximo_val-1
                        maximo_val = maximo_val+4
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="B5"
                    if k==6:
                        minimo=maximo_val
                        maximo_val = maximo_val+9
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="A5"
                    if k==7:
                        minimo=maximo_val
                        maximo_val = maximo_val+3
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="G4"
                    if k==8:
                        minimo=maximo_val
                        maximo_val = maximo_val+9
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="F4"
                    if k==9:
                        minimo=maximo_val
                        maximo_val = maximo_val+4
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="E4"
                    if k==10:
                        minimo=maximo_val
                        maximo_val = maximo_val+8
                        for g in range(minimo,maximo_val):
                            for f in range(len(componentes[g])):
                                eti=componentes[g][f]
                                if eti !=0:
                                    notas[eti-1]="D4"
                cont+=1
            elif cont==4:
                cont=0
                compas+=1
            else:
                cont+=1
            lineas+=1
    etiquetamiento=notas
    return np.array(etiquetamiento)
