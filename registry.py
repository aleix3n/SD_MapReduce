
from pyactor.context import set_context, create_host, serve_forever
import sys

#Parametros Registry: IP PORT


class NotFound(Exception):
    pass


class Registry(object):
    _ask = ['bind','lookup']
    _ref = ['bind','lookup']

    def __init__(self):
        self.actors = {}

    def bind(self, name, actor):
        print "Se ha registrado ",name
        self.actors[name] = actor


    def lookup(self, name):
        if name in self.actors:
            return self.actors[name]
        else:
            return None


if __name__ == "__main__":
    print "Registry"

    set_context()
    host = create_host('http://'+sys.argv[1]+':'+sys.argv[2]+'/')

    registry = host.spawn('registre', Registry)

    print 'host '+sys.argv[1]+' listening at port: '+sys.argv[2]

    serve_forever()
