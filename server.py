import requests,os,sys

#Parametros Servidor: PORT CARPETA_ARCHIVOS

if __name__ == '__main__':
	print "Server"
	
	os.system("mkdir -p "+sys.argv[2])#Creacion y acceso carpeta
	os.chdir(sys.argv[2])

	os.system("python -m SimpleHTTPServer "+sys.argv[1])
