import solucion2
from assertpy import assert_that
'''
	Para instalar assertpy hay que instalar primero pip con:
	~ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
	~ python get-pip.py  

	Luego hacer lo siguiente:
	~ python3 -m pip install assertpy  

	Listo ;)
	
'''

solucionEsperada = open("salida.txt").readlines()

solucionReal = open("salida_chris.txt").readlines()

assert_that(solucionReal).is_equal_to(solucionEsperada)