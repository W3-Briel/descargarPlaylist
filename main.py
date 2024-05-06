import class_video as c

## ahi adentro mete el link de la playlist, tiene que estar en publica o en no listada.

link  = input("Ingresa el link de la playlist.\nTiene que estar Publica o No listada; ")

miPlaylist = c.Cargar_playlist(link)
miPlaylist.preparar_y_descargar_todo()

print("se convertira todo a mp3\n")
conversor = c.Convertir(miPlaylist.videos_obj)
conversor.convertir_todo_a_mp3()
c.Compresor().zip(conversor.get_path())

print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")