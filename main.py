from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def select_file():
    root = tk.Tk()
    root.withdraw()  # Masquer la fenêtre principale
    print("Fenêtre de sélection de fichier ouverte")  # Message de débogage
    file_path = filedialog.askopenfilename(initialdir='.', title='Sélectionner un fichier', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    print(f"Fichier sélectionné : {file_path}")  # Message de débogage
    return file_path

def process_image(file_path):
    output_path = 'output.png'
    input_image = Image.open(file_path)
    output_image = remove(input_image)
    output_image.save(output_path)
    return output_path

# Afficher le fichier
if __name__ == "__main__":
    selected_file = select_file()
    if selected_file:
        output_file = process_image(selected_file)
        print(f"Image traitée enregistrée sous : {output_file}")
    else:
        print("Aucun fichier sélectionné.")

