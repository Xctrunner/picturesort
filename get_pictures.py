import os
from os import listdir
import tkinter
from PIL import Image, ImageTk, ExifTags
import numpy as np

def get_list_of_img_from_directory(directory, search_subdir = False):
    return [os.path.join(directory, f) for f in listdir(directory) if f.endswith((".jpg", ".jpeg", ".png", ".JPG", ".JPEG", ".PNG", ".HEIC"))]

class PictureHandler():
    def __init__(self, pilImage):
        self.root = tkinter.Tk()
        self.root.overrideredirect(1)
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.focus_set()
        self.root.focus_force()   
        self.root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.canvas = tkinter.Canvas(self.root,width=self.w,height=self.h)
        self.canvas.pack()
        self.canvas.configure(background='black')
        self.left_better = None
        self.root.bind("<Key>", self.key_press)
        imgWidth, imgHeight = pilImage.size
        if imgWidth > self.w or imgHeight > self.h:
            ratio = min(self.w/imgWidth, self.h/imgHeight)
            imgWidth = int(imgWidth*ratio)
            imgHeight = int(imgHeight*ratio)
            pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(pilImage)
        imagesprite = self.canvas.create_image(self.w/2,self.h/2,image=image)
        self.root.mainloop()

    def key_press(self, event):
        key = event.char
        if key == "a":
            self.root.destroy()
            self.left_better = True
        elif key == "l":
            self.root.destroy()
            self.left_better = False

def is_left_img_better(img1, img2):
    im1 = Image.open(img1)
    im2 = Image.open(img2)

    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation] == 'Orientation':
            break

    exif1 = dict(im1._getexif().items())
    if exif1[orientation] == 8:
        im1 = im1.rotate(90, expand=True)
    elif exif1[orientation] == 6:
        im1 = im1.rotate(270, expand=True)

    exif2 = dict(im2._getexif().items())
    if exif2[orientation] == 8:
        im2 = im2.rotate(90, expand=True)
    elif exif2[orientation] == 6:
        im2 = im2.rotate(270, expand=True)

    background_color = (0, 0, 0)

    if im1.size[1] < im2.size[1]:
        result = Image.new(im1.mode, (im1.size[0], im2.size[1]), background_color)
        result.paste(im1, (0, 0))
        im1 = result
    if im2.size[1] < im1.size[1]:
        result = Image.new(im2.mode, (im2.size[0], im1.size[1]), background_color)
        result.paste(im2, (0, 0))
        im2 = result
    merged_img = Image.fromarray(np.hstack((np.array(im1),np.array(im2))))
    pic_handler = PictureHandler(merged_img)
    return pic_handler.left_better

def get_album_from_google(album_name):
    pass # TODO