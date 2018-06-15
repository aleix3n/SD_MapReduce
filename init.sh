#!/bin/bash



#Parametros de entrada para iniciar todo el procedimiento:
# PORT_SERVIDOR CARPETA IP_REGISTRY PORT_REGISTRY IP_REDUCER PORT_REDUCER IP_MAPPER PORT_MAPPER IP_MASTER PORT_MASTER FICHERO NUMERO_MAPPERS FUNCION

gnome-terminal -e "python server.py $1 $2"

gnome-terminal -e "python registry.py $3 $4"
sleep 1

gnome-terminal -e "python reducer.py $5 $6 $3 $4"
sleep 1


for (( i=0;i<${12};i++ ))
do
gnome-terminal -e "python mapper.py $7 $(($8+$i)) $i $3 $4"
done

sleep 1
gnome-terminal -e "python master.py $9 ${10} $2 $1 ${11} ${12} $3 $4 ${13}"
