#usare un file python come libreria oppure come file esecutivo in un singolo file.
def somma(a:float,b:float):
    '''questa function fa cose'''
    s=a+b
    print(s)
    return s

def main():
    a=5
    b=6
    somma(a,b)

if __name__=="__main__": #stringa di esecuzione funzione principale
    main()
#template generale di come far funzionare i file del pitone
