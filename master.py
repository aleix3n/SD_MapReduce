#!/usr/bin/python
from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
import sys, os,re
import requests

#Parametros Master: IP PORT CARPETA_ARCHIVOS PORT_SERVIDOR FICHERO NUM_MAPPERS IP_REGISTRY PORT_REGISTRY FUNCION

def particiona(num,fichero,carpeta):
	mappers=num

	with open(fichero) as f:
		for i, l in enumerate(f):
			pass
	linias=i+1	
	parte=(linias/mappers)	

	texto=open(fichero,'r')
	
	n=0
	while(n<mappers):
		fi=open(carpeta+'/Map'+str(n)+'.txt','w')
		m=0
		while(m<parte):
			line=texto.readline()
			fi.write(line)
			m+=1
		fi.close()
		n+=1

	fi=open(carpeta+'/Map'+str(n-1)+'.txt','a')
	m=0
	while True:
		line=texto.readline()
		if not line: break
		fi.write(line)
	print "Particionado del fichero hecho"
	fi.close()
	texto.close()
	

class Master(object):
	_tell = ['informacion']

	def informacion(self,result):
		print 'Palabras '+str(result)


if __name__ == "__main__":
	
	nummappers=int(sys.argv[6])
	particiona(nummappers,sys.argv[5],sys.argv[3])

 	set_context()

	host = create_host('http://'+sys.argv[1]+':'+sys.argv[2])
	registry = host.lookup_url('http://'+sys.argv[7]+':'+sys.argv[8]+'/registre', 'Registry','registry')
	registry.bind('master',host)	
	master=host.spawn('master', 'master/Master')

	reducer_host=registry.lookup('reducer')
	reducer=reducer_host.lookup('reducer')

	""" Guardaremos los mappers para llamar a la funcion """
	mappers=[]
	texto=[]
	for i in range(0,nummappers):
		mapper_host=registry.lookup('mapper'+str(i))
		mappers.append(mapper_host.lookup('mapper'+str(i)))
		texto.append(requests.get("http://"+sys.argv[1]+":"+sys.argv[4]+"/Map"+ str(i) +".txt").text.encode('utf-8'))

	""" Empezara a contar el tiempo """
	reducer.inicializa(nummappers)

	""" Segun la funcion especificada en el ultimo parametro"""
	for i in range(0,nummappers):
		if(sys.argv[9]=='wordCount'):
			mappers[i].wordCount(texto[i])
		elif(sys.argv[9]=='countWords'):
			mappers[i].countWords(texto[i])

	serve_forever()

	shutdown()
	


