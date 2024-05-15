import pytube,pydub, re,os ,zipfile

class Video():
    def __init__(self,url: str):
        self.obj = pytube.YouTube(url)
        self.audio = None
        self.title = self.obj.title
        self.path = "./descargas_mp3/"

        patron = re.compile("[A-Za-z/()\ñ\u00E0-\u00FC ]+")
        self.title = "".join(re.findall(patron,self.title))
        self.title = "_".join(self.title.split())

    def get_minutes(self) -> float:
        minutes = self.obj.length/60
        return float(f"{minutes:.3}")

    def get_info(self) -> dict:
        return {"minutes": self.get_minutes(),
                "size": self.set_audio(),
                "title": self.title,
                "artist": self.obj.author,
                "date": self.obj.publish_date
                }

    def set_audio(self) -> float:
        if self.audio == None:
            print("obteniendo audio...",end="\r")
            self.audio = self.obj.streams.get_audio_only()
        return self.audio.filesize_mb

    def set_path(self,nueva_ruta: str) -> None:
        self.path = nueva_ruta

    def descargar(self) -> None:
        try:
            self.arc = f"{self.title}.mp4"
            
            print(f"descargando '{self.title}' ; {self.set_audio():.2}MB...",end="\r")
            self.audio.download(output_path=self.path,filename=self.arc)
            self.set_path(os.path.join(self.path,self.arc))
        except:
            print("error en Descargar - Video")

class Cargar_playlist():
    def __init__(self,url: str):
        self.lista = pytube.Playlist(url).video_urls
        self.videos_obj = []

    def guardar_videos(self) -> None:
        largo = len(self.lista)
        mensaje = "puede tardar un ratito! quedan cargar"
        print(f"{mensaje} {largo}...", end="\r")

        for video_link in self.lista:
            largo -=1
            print(f"{mensaje} {largo}...", end="\r")
            self.videos_obj.append(Video(video_link))

        print("*"*30,"\nPLAYLIST INSTANCIADA"*3,"\n","*"*30)

    def obtener_audios(self) -> None:
        for video in self.videos_obj:
            video.set_audio()
    def descargar_todos(self) -> None:
        for video in self.videos_obj:
            video.descargar()

    def setup(self) -> None:
        self.guardar_videos()
        self.obtener_audios()
        self.descargar_todos()

class Convertir():
    def __init__(self,lista_Playlist):
        self.list_obj = lista_Playlist
        self.path = "./descargas_mp3"

    def todo_mp3(self) -> None:
        print("<>"*20)
        print("se convertira todo a mp3\n")
        for archivo in self.list_obj:
            try:
                print("convirtiendo: ", archivo.title)

                if os.path.exists(archivo.path):
                    audio_segment = pydub.AudioSegment.from_file(archivo.path, format="mp4")
                    mp3_path = os.path.join(self.path, f"audio_{archivo.title}.mp3")
                    audio_segment.export(mp3_path, format="mp3", tags=archivo.get_info())

                    # Elimina el archivo .mp4 original y solo dejamos el .mp3
                    os.remove(archivo.path)

                    print(f"{archivo.title} completado!!")
                else:
                    print(f"Error: El archivo no se encontró: {archivo.path}")
            except Exception as e:
                print(f"Error al procesar {archivo.title}: {e}")

class Compresor():
    def zip (self,path) -> None:
        with zipfile.ZipFile("playlist.zip","w") as z:
            for folder, subfolders, cancionMP3 in os.walk(path):
                for i in cancionMP3:
                    if i.endswith(".mp3"):
                        z.write(os.path.join(path,i), compress_type=zipfile.ZIP_DEFLATED)