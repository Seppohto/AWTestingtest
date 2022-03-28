def tiedostonlukija(filename,index):
    try :
        with open(filename,"r") as f:
            content = f.readlines()   
            if len(content) == 0 :
                vastaus='Empty file'
            elif len(content) == (index-1):
                vastaus='IndexError'
            else :
                vastaus=content[index-1]
    except:
        vastaus = 'File not found'    
    return vastaus
