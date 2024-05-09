import class_video as c

## al ejecutar el codigo, la consola se queda esperando un link de una playlist publica o no listada, de youtube para poder descargar sus
## videos mp3 de la lista.


### trabajar excepsiones
while True:
    link  = input("Ingresa el link de la playlist.\nTiene que estar Publica o No listada; ")
    try:
        miPlaylist = c.Cargar_playlist(link); break
    except: print("ocurrio un error - intenta poner un link valido"); continue

miPlaylist.setup()

convertir = c.Convertir(miPlaylist.videos_obj)
convertir.todo_mp3() ## deberia trabajar con hilos.
c.Compresor().zip(convertir.path)

print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")