#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os,re,time

def countWords(texto):
	

	tiempo=time.time()	
	palabras=0
	for linea in texto.splitlines():
		linea= re.sub(r'[-,;:?!.¿¡\'\(\)\[\]\"|*+-_<>#@&^%$]'," ",linea)
		for p in linea.split():
			palabras+=1

	print ("\nCountWords: Palabras obtenidas: "+str(palabras)+"\n\ttiempo: "+str(time.time()-tiempo))

def wordCount(texto):
	
	tiempo=time.time()
	palabras={}
	for linea in texto.splitlines():
		linea= re.sub(r'[-,;:?!.¿¡\'\(\)\[\]\"|*+-_<>#@&^%$]'," ",linea)
		for p in linea.split():
			p=p.lower()
	    		if p not in palabras:
				palabras[p]=1
	    		else:
				palabras[p]=palabras[p]+1
	print palabras
	print ("\nWordCount: Palabras obtenidas: "+str(palabras)+"\n\ttiempo: "+str(time.time()-tiempo))



if __name__ == "__main__":
	

	file=open(sys.argv[1],'r')
	texto=file.read()
	countWords(texto)
	wordCount(texto)
	
