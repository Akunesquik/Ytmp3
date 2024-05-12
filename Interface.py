import tkinter as tk
from tkinter import filedialog, messagebox
import pytube
import os

def download_video(url, save_dir, format):
    try:
        # Create YouTube object
        yt = pytube.YouTube(url)

        # Get video title
        title = yt.title
        filename = "".join(c for c in title if c.isalnum() or c.isspace() or c in "-_.") + "." + format
        # Set save path
        save_path = os.path.join(save_dir)

        # Download video or audio based on format
        if format == "mp4":
            yt.streams.filter(file_extension="mp4").first().download(save_path)
        elif format == "mp3":
            audio_stream = yt.streams.filter(only_audio=True).first()  # Utiliser only_audio
            # Télécharger l'audio
            audio_stream.download(save_path,filename=filename)
        else:
            raise ValueError("Invalid format: " + format)

        messagebox.showinfo("Téléchargement terminé", f"{title} téléchargé dans {save_path}")
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec du téléchargement : {e}")


def main():
    window = tk.Tk()
    window.title("Convertisseur YouTube")
    window.geometry("920x640")
   
   # Create grid layout
    window.rowconfigure(0, weight=1, minsize=50)  # Row 1: min=50, max=100
    window.rowconfigure(1, weight=1, minsize=50)  # Row 2: min=50, max=100
    window.rowconfigure(2, weight=1, minsize=50)  # Row 3: min=50, max=100
    window.columnconfigure(0, weight=1, minsize=100)  # Column 1: min=100, max=200
    window.columnconfigure(1, weight=3, minsize=200)  # Column 2: min=200, max=400
    window.columnconfigure(2, weight=1, minsize=100)  # Column 3: min=100, max=200

    # URL
    url_label = tk.Label(window, text="URL de la vidéo YouTube :")
    url_label.grid(row=0, column=0)
    url_entry = tk.Entry(window)
    url_entry.grid(row=0, column=1)

    # Save directory
    save_dir_label = tk.Label(window, text="Dossier de sauvegarde :")
    save_dir_label.grid(row=1, column=0)
    save_dir_entry = tk.Entry(window)
    save_dir_entry.grid(row=1, column=1)
    save_dir_button = tk.Button(window, text="Sélectionner", command=lambda: select_save_dir(save_dir_entry))
    save_dir_button.grid(row=1, column=2)

    # Download buttons
    mp3_button = tk.Button(window, text="MP3", command=lambda: download_video(url_entry.get(), save_dir_entry.get(), "mp3"))
    mp3_button.grid(row=2, column=0)
    mp4_button = tk.Button(window, text="MP4", command=lambda: download_video(url_entry.get(), save_dir_entry.get(), "mp4"))
    mp4_button.grid(row=2, column=2)

    # Center the window (optional)
    window.update_idletasks()  # Update window dimensions
    x = (window.winfo_screenwidth() - window.winfo_width()) // 2
    y = (window.winfo_screenheight() - window.winfo_height()) // 2
    window.geometry(f"+{x}+{y}")

    window.mainloop()


def select_save_dir(save_dir_entry):
    save_dir = filedialog.askdirectory()
    if save_dir:
        save_dir_entry.delete(0, tk.END)
        save_dir_entry.insert(0, save_dir)


if __name__ == "__main__":
    main()
