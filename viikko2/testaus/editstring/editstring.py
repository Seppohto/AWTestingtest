def reverse(string):
    lista = string.split()
    for paikka, sana in enumerate(lista):
        if len(sana) >=5:
            reversedsana = sana[::-1]
            lista[paikka] = reversedsana
            sana = reversedsana
        if len(sana) == 2:
            capssana = sana.upper()
            lista[paikka] = capssana

    
    vastaus = ' '.join(lista)
    vastaus = vastaus[:1].upper() + vastaus[1:]
    loppumerkit="!?:"
    if vastaus[len(vastaus)-1] not in loppumerkit:
        vastaus += "."

    return vastaus