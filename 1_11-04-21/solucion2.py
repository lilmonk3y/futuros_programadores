import datetime as dt

def obtenerListaDePersonasDesdeStrings(personaComoString):
	lineaDelArchivo = personaComoString.rstrip('\n')
	return [x.strip() for x in lineaDelArchivo.split(";")]
	
def armarFechaDesdeUnString(datosDeUnaPersona):
	fechaDeCumpleaños = dt.datetime.strptime(datosDeUnaPersona[1],"%Y/%m/%d").date()
	return [datosDeUnaPersona[0], fechaDeCumpleaños]

def edadDeUnaPersonaEnDias(persona):
	edadEnDias = dt.date.today() - persona[1]
	return [persona[0],persona[1], edadEnDias]

def conviertoLaPersonaALaFormaEsperada(persona):
	años = int(persona[2].days / 365)
	return [persona[0], persona[1].strftime("%Y/%m/%d"), años]

archivoDeEntrada = open("entrada.txt")

listaDePersonas = map(obtenerListaDePersonasDesdeStrings, archivoDeEntrada.readlines())

archivoDeEntrada.close()


listaDePersonasConEdad = map(armarFechaDesdeUnString, listaDePersonas)

listaDePersonasConEdadEnDias = list(map(edadDeUnaPersonaEnDias, listaDePersonasConEdad))

listaDePersonasConEdadEnDias.sort(key= lambda persona : persona[2])

listaDePersonasEsperada = map(conviertoLaPersonaALaFormaEsperada, listaDePersonasConEdadEnDias)

archivoDeSalida = open("salida_chris.txt", "w")

for persona in listaDePersonasEsperada:
	archivoDeSalida.write("{} ; {} ; {}\n".format(persona[0], persona[1], persona[2]))

archivoDeSalida.close()
