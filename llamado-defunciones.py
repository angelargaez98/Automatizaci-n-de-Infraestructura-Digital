#importacion o llamado de el archivo.py
import sys 
sys.path.append('C:descargas/funcionesexterna1.py')
import funcionesexterna as F

F.funcion1 ()
#llamamos las funciones en aotro archivo
q = input('introduzca un dato:')
w = input('introduzca un datos:')
print (F.funcion2 (q,w))
