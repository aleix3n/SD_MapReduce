from pyactor.context import set_context, create_host, sleep, shutdown, serve_forever
import sys, time, re


#Parametros Mapper: IP PORT NUM_MAPPERS IP_REGISTRY PORT_REGISTRY

class Mapper(object):
    _tell = ['wordCount','countWords']


    def __init__(self,registry,reducer):
        self.val=None
        self.registry=registry
	self.reducer=reducer
      
    def wordCount(self,text):
	texto=re.sub('[^ a-zA-Z0-9]',' ',text ).split()

	self.val={}
	for word in texto:
		if word not in self.val:
			self.val[word]=1
		else:
			self.val[word]=self.val[word]+1
	self.reducer.wordCount(self.val)
        print "Mapper Finalizado" 

    def countWords(self,text):
        texto=re.sub('[^ a-zA-Z0-9]',' ',text ).split()	

        self.val=0
        for word in texto:
	        self.val=self.val+1
        
	self.reducer.countWords(self.val)
        print "Mapper Finalizado"



if __name__ == "__main__":	 

	set_context()

	print 'Mapper ' + str(sys.argv[3])

	host = create_host('http://'+sys.argv[1]+':'+sys.argv[2])

	registry = host.lookup_url('http://'+sys.argv[4]+':'+sys.argv[5]+'/registre', 'Registry','registry')

	registry.bind('mapper'+sys.argv[3],host)

	reducer_host=registry.lookup('reducer')
	reducer=reducer_host.lookup('reducer')

	mapper=host.spawn('mapper'+sys.argv[3], 'mapper/Mapper', registry, reducer)
	
	serve_forever()

