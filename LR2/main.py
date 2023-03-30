import os
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter import RIGHT
from tkinter import BOTTOM
from tkinter import Scrollbar
from tkinter import Y
from tkinter import X
from tkinter import filedialog
 
def main():
    root = tk.Tk()
 
    root.withdraw()
    folder_name = filedialog.askdirectory(initialdir='../../')
    root.deiconify()
 
    photos = []
    mode_to_bpp = {'1' : 1, 'L' : 8, 'P' : 8, 'RGB' : 24, 'RGBA' : 32, 'CMYK' : 32, 'YCbCr' : 24, 'I' : 32, 'F' : 32}
 
    
    root.title("Image data viewer")
    root.geometry("1280x640+240+240")
 
    columns = ("file", "size", "resolution", "dpi", "color_depth", "compression")
 
    img_scroll1 = Scrollbar(root)
    img_scroll1.pack(side=RIGHT, fill=Y)
 
    img_scroll2 = Scrollbar(root ,orient='horizontal')
    img_scroll2.pack(side= BOTTOM,fill=X)
 
    tree = ttk.Treeview(root, columns=columns, show="headings", 
                        yscrollcommand=img_scroll1.set, xscrollcommand=img_scroll2.set)
    tree.pack(fill=tk.BOTH, expand=1)
 
    img_scroll1.config(command=tree.yview)
    img_scroll2.config(command=tree.xview)
 
    tree.heading("file", text="文件:")
    tree.heading("size", text="尺寸:")
    tree.heading("resolution", text="解決:")
    tree.heading("dpi", text="新聞部:")
    tree.heading("color_depth", text="顏色深度:")
    tree.heading("compression", text="壓縮:")
 
    for image in photos:
        tree.insert("", tk.END, values=image)
 
    root.mainloop()
 
 

if __name__ == '__main__':
    main()
