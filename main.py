import class_video as c

## ahi adentro mete el link de la playlist, tiene que estar en publica o en no listada.
miPlaylist = c.Cargar_playlist("https://youtube.com/playlist?list=PLJHs0bVpt5Y7IS2mCjhChTjVic3vAWxrW&si=P1OyYyXbCtulO1Og")
miPlaylist.preparar_y_descargar_todo()

opcion = input("deseas convertir todo a mp3??-> (si) (no): ").lower()
match opcion:
    case "si":
        print("se convertira todo a mp3\n")
        conversor = c.Convertir(miPlaylist.videos_obj)
        conversor.convertir_todo_a_mp3()
        opcion = input("te gustaria comprimir la carpeta en zip? -> (si) (no): ").lower()
        if opcion == "si": 
            c.Compresor().zip(conversor.get_path())
            print(" *** ACCION COMPLETADA" * 3)
        else: print("ok, no comprimiere nada.")
    case _: print("quedaran como archivo de audio pero en .mp4")

print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")
print("FIN DEL PROGRAMA")