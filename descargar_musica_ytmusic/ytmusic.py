import os
import yt_dlp

# Crear la carpeta 'music' si no existe
output_folder = 'music'
os.makedirs(output_folder, exist_ok=True)

def descargar_audio(url):
    opciones = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Guardar en la carpeta 'music'
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Calidad de audio
        }],
        'writethumbnail': True,  # Descargar miniatura
        'postprocessors_append': [{
            'key': 'EmbedThumbnail'
        }]
    }
    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Ingrese el enlace de la canción o álbum de YouTube Music: ")
    descargar_audio(url)
