from class_video import Video
import pydub, os

metadatos = Video("https://youtu.be/TZ2d7KsaCmI?si=agPPUM-lkwH8-1Rj")
metadata = {
    "title": metadatos.get_title(),
    "artist": metadatos.obj.author,
    "date": metadatos.obj.publish_date
}

metadatos.descargar()

path = f"./descargas_mp3/{metadatos.get_title()}.mp4"
audio_segment = pydub.AudioSegment.from_file(path, format="mp4")

mp3_path = os.path.join("./descargas_mp3", f"audio_{metadatos.get_title()}.mp3")
audio_segment.export(mp3_path, format="mp3", tags = metadata)
# Elimina el archivo de video original
os.remove(path)
print(f"{metadatos.get_title()} completado!!")