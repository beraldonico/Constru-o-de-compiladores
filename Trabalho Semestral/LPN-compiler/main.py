from Lexico import lexical as LX
from Sintatico import syntactical as ST
import sys

def print_header():
    print(
        """
========================================

 (     (        )          One
 )\ )  )\ )  ( /(         Exotic
(()/( (()/(  )\())       Language
 /(_)) /(_))((_)\  
(_))  (_))   _((_)     Do not forget
| |   | _ \ | \| |     to use SPACE
| |__ |  _/ | .` |    between lexemas.
|____||_|   |_|\_|

========================================           
        """
    )

if __name__ == '__main__':
    #main()
    print_header()
    
    try:
        LX.lexical_analyzer("Tests files/test3.lpn")
        ST.Syntactical_Analyzer()
        #LX.lexical_analyzer(sys.argv[1])
    except IndexError:
        print("ERROR: Não há codigo para compilar")

