import datetime as dt
from operator import itemgetter



archivoDeEntrada = open("entrada.txt")

listaDePersonas = []

for lineaDelArchivo in  archivoDeEntrada:
	lineaDelArchivo = lineaDelArchivo.rstrip('\n')
	lineaDelArchivo = [x.strip() for x in lineaDelArchivo.split(";")]
	listaDePersonas.append(lineaDelArchivo)

archivoDeEntrada.close()
# la lista de personas ahora tiene a todas las lineas del archivo y cada una es de la forma [nombre, YYYY/MM/DD]
#print(listaDePersonas)

listaDePersonasConEdad = []

for datosDeUnaPersona in listaDePersonas:
	fechaDeCumpleaños = dt.datetime.strptime(datosDeUnaPersona[1],"%Y/%m/%d").date()
	listaDePersonasConEdad.append([datosDeUnaPersona[0], fechaDeCumpleaños])

# la lista de personas ahora es nombre y fecha de cumpleaños (como una fecha real de python)
#print(listaDePersonasConEdad)

listaDePersonasConEdadEnDias = []

for persona in listaDePersonasConEdad:
	edadEnDias = dt.date.today() - persona[1]
	listaDePersonasConEdadEnDias.append([persona[0],persona[1], edadEnDias])

# la lista ahora tiene a las personas más una propiedad mas que son los días de vida de la persona
#print(listaDePersonasConEdadEnDias)

listaDePersonasConEdadEnDiasOrdenada = sorted(listaDePersonasConEdadEnDias, key=itemgetter(2))

# la lista ahora tiene a las personas ordenada por los dias de vida
#print(listaDePersonasConEdadEnDiasOrdenada)

listaDePersonasEsperada = []

for persona in listaDePersonasConEdadEnDiasOrdenada:
	años = int(persona[2].days / 365)
	listaDePersonasEsperada.append([
		persona[0], 
		persona[1].strftime("%Y/%m/%d"),
		años])

# ahora la lista está exactamente como espero la respuesta. me falta armar el archivo de salida
#print(listaDePersonasEsperada)


archivoDeSalida = open("salida_chris.txt", "w")

for persona in listaDePersonasEsperada:
	archivoDeSalida.write("{} ; {} ; {}\n".format(persona[0], persona[1], persona[2]))

archivoDeSalida.close()
