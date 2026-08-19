from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

# list of images
Image_path = [
   #Uplaod your own image path
   #Uplaod your own image path
   #Uplaod your own image path
   #Uplaod your own image path
   #Uplaod your own image path
]

images = []
for path in Image_path:
    image = Image.open(path)
    image.thumbnail((1080, 1080))
    images.append(image)
    
photo_image = [ImageTk.PhotoImage(image) for image in images]
label = tk.Label(root)
label.pack()

slideshow = cycle(photo_image)
def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo
    root.after(3000, update_image)

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Play", command=start_slideshow)
play_button.pack()

root.mainloop()
