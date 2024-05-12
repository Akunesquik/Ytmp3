import pytube
from moviepy.editor import VideoFileClip

def download_video(url, title, audio_format):
    # Télécharger la vidéo YouTube
    yt = pytube.YouTube(url)

    # Filtrer les flux audio
    audio_stream = yt.streams.filter(only_audio=True).first()  # Utiliser only_audio

    filename = "".join(c for c in title if c.isalnum() or c.isspace() or c in "-_.") + "." + audio_format

    # Télécharger l'audio
    audio_stream.download(filename=filename)

def convert_video_to_audio(video_path, audio_format):
    # Extraire l'audio de la vidéo
    audio = VideoFileClip(video_path)
    audio = audio.audio

    # Enregistrer l'audio au format MP3
    audio.write_audiofile(filename=video_path.replace(video_path.split(".")[-1], audio_format))

def main():
    # Obtenir l'URL de la vidéo YouTube
    video_url = input("Entrez l'URL de la vidéo YouTube: ")

    # Obtenir le titre de la vidéo
    video_title = pytube.YouTube(video_url).title

    # Choisir le format audio
    audio_format = input("Choisissez le format audio (MP3, WAV): ")

    # Télécharger et convertir la vidéo
    download_video(video_url, video_title, audio_format)
    # convert_video_to_audio(video_title + "." + audio_format, audio_format)

    print("Conversion terminée ! Le fichier audio est enregistré sous :", video_title + "." + audio_format)

if __name__ == "__main__":
    main()