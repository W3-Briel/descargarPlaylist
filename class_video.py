import pytube,pydub, re
import os
### agregar expresiones regulares para los titulos
## arreglar la expresion regular, no tiene que aceptar & ni -

class Video():
    def __init__(self,url):
        self.obj = pytube.YouTube(url)
        self.audio = None
        self.title = self.obj.title
        self.path = "./descargas_mp3/"

        patron = re.compile("[A-Za-z/()\ñ\u00E0-\u00FC ]+")
        self.title = "".join(re.findall(patron,self.title))
        self.title = "".join(self.title.split())

    def get_minutes(self):
        minutes = self.obj.length/60
        return float(f"{minutes:.3}")

    def get_title(self):
        return self.title

    def get_info(self):
        return {"titulo": self.get_title(),
                "minutos": self.get_minutes(),
                "tamaño_audio_mb": self.set_audio().filesize_mb}
    def get_metadata(self):
        return {
            "title": self.get_title(),
            "artist": self.obj.author,
            "date": self.obj.publish_date
            }

    def set_audio(self):
        if self.audio == None:
            print("obteniendo audio...",end="\r")
            self.audio = self.obj.streams.get_audio_only()
        return self.audio
    def set_path(self,nueva_ruta):
        self.path = nueva_ruta

    def descargar(self):
        try:
            self.arc = f"{self.get_title()}.mp4"
            
            print(f"descargando '{self.get_title()}' ; {self.set_audio().filesize_mb:.2}MB...",end="\r")
            self.audio.download(output_path=self.path,filename=self.arc)
            self.path = os.path.join(self.path,self.arc)

            print("\n")
            print("*"*30)
            print(f"COMPLETO - '{self.get_title()}'")
            print("*"*30)
        except:
            print("error en Descargar - Video")

class Cargar_playlist():
    def __init__(self,url):
        self.lista = pytube.Playlist(url).video_urls
        self.videos_obj = []

    def guardar_videos(self):
        largo = len(self.lista)
        print(f"puede tardar un ratito! quedan cargar {largo}...", end="\r")

        for video_link in self.lista:
            largo -=1
            print(f"puede tardar un ratito! quedan para cargar {largo}...", end="\r")
            self.videos_obj.append(Video(video_link))

        print("*"*50)
        print("PLAYLIST INSTANCIADA")

    def obtener_audios(self):
        for video in self.videos_obj:
            video.set_audio()
    def descargar_todos(self):
        for video in self.videos_obj:
            video.descargar()

    def preparar_y_descargar_todo(self):
        self.guardar_videos()
        self.obtener_audios()
        self.descargar_todos()

class Convertir():
    def __init__(self,lista_Playlist):
        self.list_obj = lista_Playlist

    def convertir_todo_a_mp3(self):
        for archivo in self.list_obj:
            try:
                print("convirtiendo: ", archivo.get_title())
                print(archivo.path)

                if os.path.exists(archivo.path):
                    audio_segment = pydub.AudioSegment.from_file(archivo.path, format="mp4")
                    mp3_path = os.path.join("./descargas_mp3", f"audio_{archivo.get_title()}.mp3")
                    audio_segment.export(mp3_path, format="mp3", tags = archivo.get_metadata())

                    # Elimina el archivo de video original
                    os.remove(archivo.path)

                    print(f"{archivo.get_title()} completado!!")
                else:
                    print(f"Error: El archivo no se encontró: {archivo.path}")
            except Exception as e:
                print(f"Error al procesar {archivo.get_title()}: {e}")