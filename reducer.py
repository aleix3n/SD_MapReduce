from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
from operator import add
from collections import Counter
import requests,sys,time

#Parametros Reducer: IP PORT IP_REGISTRY PORT_REGISTRY

class Reducer(object):
    _tell = ['inicializa','wordCount','countWords']

    def __init__(self,registry):
        self.diccionariofinal=[] #Diccionario final
        self.mappers=0
	self.numpalabras=0

        self.reduct=None #Para las funciones que se invocaran luego
	self.master=None
        self.registry=registry

        self.tiempoinicial=0


    def inicializa(self,nmap):
        self.mappers=nmap
	master_host=self.registry.lookup('master')
	master=master_host.lookup('master')
	self.master=master
        self.tiempoinicial=time.time()


    def wordCount(self,dicc):
        self.diccionariofinal.append(dicc)
	self.mappers=self.mappers -1

	if self.mappers==0: 
		self.reduct=dict(reduce(add, (Counter(dict(diccionario)) for diccionario in self.diccionariofinal)))
		self.master.informacion(self.reduct)

		tiempo=time.time()-self.tiempoinicial
		print "Tiempo de ejecucion: " +str(tiempo)		                


    def countWords(self,nump):
	self.numpalabras=self.numpalabras+nump
	self.mappers=self.mappers -1

	if self.mappers==0:
		self.master.informacion(self.numpalabras)

		tiempo=time.time()-self.tiempoinicial
		print "Tiempo de ejecucion: " +str(tiempo)
			




if __name__ == "__main__":
	print 'Reducer'
	set_context()

	host = create_host('http://'+sys.argv[1]+':'+sys.argv[2])
	registry = host.lookup_url('http://'+sys.argv[3]+':'+sys.argv[4]+'/registre', 'Registry','registry')	

	registry.bind('reducer',host)	
	reducer=host.spawn('reducer','reducer/Reducer',registry)

	serve_forever()

