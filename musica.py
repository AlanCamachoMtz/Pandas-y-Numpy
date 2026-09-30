import os
import yt_dlp

# Leer canciones desde un archivo de texto
with open("lista_canciones.txt", "r", encoding="utf-8") as f:
    canciones = [linea.strip() for linea in f if linea.strip()]

# Carpeta de destino
carpeta = "Musica"
os.makedirs(carpeta, exist_ok=True)

# Opciones de yt-dlp
opciones = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(carpeta, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'noplaylist': True
}

# Descargar cada canción
with yt_dlp.YoutubeDL(opciones) as ydl:
    for cancion in canciones:
        print(f"\n🔎 Buscando y descargando: {cancion}")
        ydl.download([f"ytsearch1:{cancion}"])