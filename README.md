# FUNCIONALITAT
Aquest codi consisteix en mitjançant l'introducció d'un arxiu en .in, aquest comprovarà la possibilitat de generar un aqüeducte entre els punts cardinals de l'arxiu i calcularà un cost òptim mitjançant la eqüació de la pràctica.\
backtracking.py --> Algorisme en backtracking.\
dynamic.py --> Algorisme en programació dinàmica.

# ÚS
Possibilitat d'executar el codi mitjançant bash script: ./aqueducte.sh < arxiu >\
I mitjançant codi python v.3: python3 aqueducte.py < arxiu >


# CODI
## FUNCIÓ QUE LLEGEIX L'ARXIU PASSAT COM A PARÀMETRE 
## readfile()
Transforma els espais del fitxer en posicions de nombres de 2 en 2 de la llista 'variables'.\
Després, trasllada les variables de punts a la llista 'points'.\
I finalment, prepara el return perquè retorni el nombre de punts, l'alçada, cost alpha, cost beta i la llista dels punts.


## FUNCIÓ QUE PRINTA "impossible" I SURT DEL PROGRAMA 
## impossible()
def impossible():\
    print("impossible")\
    exit()


## FUNCIÓ QUE COMPROVA UN POSSIBLE PONT O AQÜEDUCTE NO VÀLID 
## wrong_cases()
Si un radi de l'arc fos major que l'alçada requerida, seria impossible generar un arc vàlid.\
Si un punt per sobre del centre de l'arc estigues fora del seu radi, voldrà dir que el pont xocaria contra el terreny considerant-ho no vàlid.


## FUNCIÓ QUE CALCULA EL COST MITJANÇANT LA FORMULA PROPOSADA
## cost()
def cost(height, x):\
    return alpha * height + beta * x

Github repository:
https://github.com/sergisabate/Algor-Aqueductus2