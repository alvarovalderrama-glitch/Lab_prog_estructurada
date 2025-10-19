def toque(numero,adivinanza):
    toques=0
    for i in numero:
        if i in adivinanza:
            toques+=1
    return str(toques)
def fama(numero,adivinanza):
    famas=0
    for i in numero:
        if i == adivinanza[numero.index(i)]:
            famas+=1
    return str(famas)
numero=str(34018)
adivinanza=str(31409)
if fama(numero,adivinanza)=="5":
    print("¡Has ganado el juego!")
else:
    print("hay "+toque(numero,adivinanza)+" toques y "+fama(numero,adivinanza)+" famas")
