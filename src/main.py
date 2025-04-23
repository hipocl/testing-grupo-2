def determinar_mail(direccion):
    es_mail = False
    if direccion.count("@") == 1:
        ler = direccion.split("@")
        if ler[0].isalnum() and ler[1].count(".com.ar") == 1:  
            ler2 = ler[1].split(".")
            ler2.pop(len(ler2)-1)
            ler2.pop(len(ler2)-1)
            ler2 = ".".join(ler2)
            if ler2.isalpha() and len(ler2) > 0:
                es_mail = True    
    return es_mail

def sacar_dominio(direccion):
    ler = direccion.split("@")
    dom = ler[1].split(".")
    dom.pop(len(dom)-1)
    dom.pop(len(dom)-1)
    dom = dom[0]
    return dom

def generar_lista_dominios_ordenada_alfa_sin_repetir():
    dominios = []
    mail = input("Ingrese su direccion de mail, ingrese("")(nada) para terminar:")
    while mail != "":
        if determinar_mail(mail):
            if not(sacar_dominio(mail) in dominios):
                dominios.append(sacar_dominio(mail))
        mail = input("Ingrese su direccion de mail, ingrese("")(nada) para terminar:")
    dominios.sort()
    return dominios
