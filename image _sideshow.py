from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow")

# list of images
Image_path = [
    r"C:\Users\lenovo\OneDrive\图片\IMG_20260226_221710_280.jpg.jpeg",
    r"C:\Users\lenovo\OneDrive\图片\Prince_Fill_the_area_with_suitable_background_--chaos_5_--ar_91_91f2ebd8-678a-45ca-8abe-8f07e5f8a13a.png.jpg",
    r"C:\Users\lenovo\OneDrive\图片\whatsapp image 2026-01-11 at 4.27.57 pm.jpeg",
    r"C:\Users\lenovo\OneDrive\图片\Camera Roll\WIN_20251231_17_46_47_Pro.jpg",
    r"C:\Users\lenovo\OneDrive\图片\Camera Roll\WIN_20260322_23_39_02_Pro.jpg",
    r"C:\Users\lenovo\OneDrive\图片\Screenshots\Screenshot (27).png"
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