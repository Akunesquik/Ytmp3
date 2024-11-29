import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube
from PIL import Image, ImageTk
import os
from os import path




def download_video(url, save_dir, format):
        # Create YouTube object
        yt = YouTube(url)
        # Get video title
        title = yt.title


        filename = "".join(c for c in title if c.isalnum() or c.isspace() or c in "-_.") + "." + format 
        if format == "mp3":
            format = "m4a"
        filename = filedialog.asksaveasfilename(initialfile=filename, initialdir=save_dir, defaultextension=f".{format}", filetypes=[(f"{format.upper()} files", f"*.{format}")])
        
        if not filename:  # Si l'utilisateur annule la sélection
            return
        filename = os.path.basename(filename)
        print(filename)
        # Download video or audio based on format
        if format == "mp4":
            yt.streams.get_highest_resolution().download(output_path=save_dir, filename=filename)
        elif format == "mp3" or format == "m4a":
            yt.streams.get_audio_only().download(output_path=save_dir, filename=filename)
        else:
            raise ValueError("Format invalide : " + format)

        messagebox.showinfo("Téléchargement terminé", f"{filename} téléchargé dans {save_dir}")


def main():
    window = tk.Tk()
    window.title("Youtube MP3/MP4")
    window.geometry("640x320")
    window.resizable(False, False)

   # Create grid layout
    window.columnconfigure(0, weight=1, minsize=100)  # Column 1: min=100, max=200
    window.columnconfigure(1, weight=3, minsize=200)  # Column 2: min=200, max=400
    window.columnconfigure(2, weight=1, minsize=100)  # Column 3: min=100, max=200

    # IMG
    image_path = "public/img/pngwing.com.png"
    path_to_icon = path.abspath(path.join(path.dirname(__file__), image_path)) 
    image = Image.open(path_to_icon)
    image = image.resize((150, 150))
    tk_image = ImageTk.PhotoImage(image)
    image_label = tk.Label(window, image=tk_image)
    image_label.grid(row=0, column=1)

    # URL
    url_label = tk.Label(window, text="URL de la vidéo YouTube :")
    url_label.grid(row=1, column=0)
    url_entry = tk.Entry(window)
    url_entry.grid(row=1, column=1,sticky='ew')

    # Save directory
    ## Variables
    default_download_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    save_dir_var = tk.StringVar(value=default_download_dir)
    ## Affichage
    save_dir_label = tk.Label(window, text="Dossier de sauvegarde :")
    save_dir_label.grid(row=2, column=0)
    save_dir_entry = tk.Entry(window, textvariable=save_dir_var)
    save_dir_entry.grid(row=2, column=1,sticky='ew')
    save_dir_button = tk.Button(window, text="Sélectionner le dossier", command=lambda: select_save_dir(save_dir_entry))
    save_dir_button.grid(row=2, column=2)

    # Download buttons
    # Création d'une sous-frame pour les boutons
    button_frame = tk.Frame(window)
    button_frame.grid(row=3, column=1, sticky='nsew')

    # Configuration de la sous-frame pour que les boutons occupent chacun 50% de la largeur
    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    # Download buttons
    mp3_button = tk.Button(button_frame, text="MP3", command=lambda: download_video(url_entry.get(), save_dir_entry.get(), "mp3"))
    mp3_button.grid(row=0, column=0, sticky='ew')  # Ancré à l'est et à l'ouest
    mp4_button = tk.Button(button_frame, text="MP4", command=lambda: download_video(url_entry.get(), save_dir_entry.get(), "mp4"))
    mp4_button.grid(row=0, column=1, sticky='ew')  # Ancré à l'est et à l'ouest

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
