import class_video as c

## al ejecutar el codigo, la consola se queda esperando un link de una playlist publica o no listada, de youtube para poder descargar sus
## videos mp3 de la lista.

while True:
    try:
        link  = input("Ingresa el link de la playlist.\nTiene que estar Publica o No listada; ")
        miPlaylist = c.Cargar_playlist(link); break
    except: print("ocurrio un error - intenta poner un link valido"); continue

miPlaylist.preparar_y_descargar_todo()

print("se convertira todo a mp3\n")
conversor = c.Convertir(miPlaylist.videos_obj)
conversor.convertir_todo_a_mp3()
c.Compresor().zip(conversor.get_path())

print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")