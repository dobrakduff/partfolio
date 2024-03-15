import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import os


def add_watermark():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)

        font = cv2.FONT_HERSHEY_SIMPLEX

        text = "Dobrakduff"
        font_scale = 1
        font_thickness = 2
        text_size = cv2.getTextSize(text, font, font_scale, font_thickness)[0]
        text_width, text_height = text_size
        x = image.shape[1] - text_width - 10
        y = image.shape[0] - 10

        cv2.putText(image, text, (x, y), font, font_scale, (255, 255, 255), font_thickness)

        if not os.path.exists("watermark_images"):
            os.makedirs("watermark_images")
        watermark_image_path = os.path.join("watermark_images", os.path.basename(file_path))
        cv2.imwrite(watermark_image_path, image)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        pil_image = Image.fromarray(image_rgb)
        display_image(pil_image)
        save_path_label.config(text="Watermarked image saved at:\n" + watermark_image_path)


def display_image(pil_image):
    window = tk.Toplevel(root)
    window.title("Watermarked Image")
    tk_image = ImageTk.PhotoImage(pil_image)
    label = tk.Label(window, image=tk_image)
    label.image = tk_image
    label.pack()


root = tk.Tk()
root.minsize(300, 300)
root.title("Add Watermark")

button = tk.Button(root, text="Choose Image", command=add_watermark)
button.pack(padx=125, pady=125)

save_path_label = tk.Label(root, text="")
save_path_label.pack()

root.mainloop()
