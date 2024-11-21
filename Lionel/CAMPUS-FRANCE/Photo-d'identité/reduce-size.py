from PIL import Image
import os

def reduce_image_size(input_path, output_path, target_size_kb):
    with Image.open(input_path) as img:
        # Vérifier la taille initiale
        initial_size = os.path.getsize(input_path) / 1024  # en Ko
        print(f"Taille initiale de l'image: {initial_size:.2f} Ko")

        # Réduire la taille et la qualité progressivement
        quality = 85  # Initialiser la qualité
        img_format = "JPEG" if img.mode != "RGBA" else "PNG"  # Utiliser JPEG si possible
        while initial_size > target_size_kb and quality > 10:
            # Redimensionner l'image (50% des dimensions originales, par exemple)
            img_resized = img.resize((img.width // 2, img.height // 2), Image.LANCZOS)

            # Enregistrer avec une qualité réduite
            img_resized.save(output_path, format=img_format, quality=quality, optimize=True)
            initial_size = os.path.getsize(output_path) / 1024  # en Ko

            # Diminuer la qualité pour compresser davantage
            quality -= 5
            print(f"Taille de l'image après compression : {initial_size:.2f} Ko, qualité : {quality}")

        if initial_size > target_size_kb:
            print(f"Impossible d'atteindre exactement {target_size_kb} Ko, mais l'image est réduite au maximum.")
        else:
            print(f"Image compressée avec succès à {initial_size:.2f} Ko")

# Utilisation
input_image_path = "Photo-identite-TOTON-Lionel.png"  # Remplacez par le chemin de votre image
output_image_path = "Photo-identite-TOTON-Lionel-compresser.jpg"  # L'image compressée sera en JPEG

reduce_image_size(input_image_path, output_image_path, 50)  # Cible : 50 Ko
