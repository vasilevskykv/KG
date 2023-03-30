import cv2 as cv
from tkinter import *
from PIL import ImageTk, Image
from copy import deepcopy


class MainSolution():
    def __init__(self):
        self.image = cv.imread("chameleon.jpg")
        self.imgray = None
        self.trsh1 = None
        self.trsh2 = None

    def original(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)

    def filt(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        
        

    def local_threshold(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        

    def adaptive_threshold(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        

    def gaussian_filter(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        

    def bilateral_filter(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        

    def opening(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        

    def closing(self):
        img = Image.fromarray(self.image)
        img = img.resize((300, 300))
        return ImageTk.PhotoImage(img)
        


class MainApp():
    def __init__(self, master):
        self.master = master
        self.master.title("圖像處理")
        self.master.geometry("1000x600")
        self.master.resizable(False, False)
        self.master.configure(background="white")

        self.solution = MainSolution()

        self.frame = Frame(self.master, bg="white")
        self.frame.pack()

        self.label = Label(self.frame, text="圖像處理", font=("Arial", 20), bg="white")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.button1 = Button(self.frame, text="原圖", font=("Arial", 12), bg="white",
                              command=self.original_image)
        self.button1.grid(row=1, column=0, pady=10)

        self.button2 = Button(self.frame, text="均值漂移濾波器", font=("Arial", 12), bg="white", command=self.filt)
        self.button2.grid(row=1, column=1, pady=10)

        self.button3 = Button(self.frame, text="本地閾值", font=("Arial", 12), bg="white",
                              command=self.local_threshold)
        self.button3.grid(row=2, column=0, pady=10)

        self.button4 = Button(self.frame, text="自適應閾值", font=("Arial", 12), bg="white",
                              command=self.adaptive_threshold)
        self.button4.grid(row=2, column=1, pady=10)

        self.button5 = Button(self.frame, text="高斯濾波器", font=("Arial", 12), bg="white",
                              command=self.gaussian_filter)
        self.button5.grid(row=3, column=0, pady=10)

        self.button6 = Button(self.frame, text="雙邊過濾器", font=("Arial", 12), bg="white",
                              command=self.bilateral_filter)
        self.button6.grid(row=3, column=1, pady=10)

        self.button11 = Button(self.frame, text="開幕式", font=("Arial", 12), bg="white", command=self.opening)
        self.button11.grid(row=6, column=0, pady=10)

        self.button12 = Button(self.frame, text="關閉", font=("Arial", 12), bg="white", command=self.closing)
        self.button12.grid(row=6, column=1, pady=10)

        self.button13 = Button(self.frame, text="出口", font=("Arial", 12), bg="white", command=self.exit)
        self.button13.grid(row=7, column=0, columnspan=2, pady=10)

        self.label1 = Label(self.frame, text="原圖", font=("Arial", 12), bg="white")
        self.label1.grid(row=7, column=0, pady=10)

        self.label2 = Label(self.frame, text="處理過的圖像", font=("Arial", 12), bg="white")
        self.label2.grid(row=7, column=1, pady=10)

        self.image1 = self.solution.original()
        self.label3 = Label(self.frame, image=self.image1, bg="white")
        self.label3.grid(row=8, column=0, pady=10)

        self.image2 = self.solution.original()
        self.label4 = Label(self.frame, image=self.image2, bg="white")
        self.label4.grid(row=8, column=1, pady=10)

    def original_image(self):
        self.image1 = self.solution.original()
        self.label3.configure(image=self.image1)
        self.label3.image = self.image1

    def filt(self):
        self.image2 = self.solution.filt()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def local_threshold(self):
        self.image1 = self.solution.local_threshold()
        self.label4.configure(image=self.image1)
        self.label4.image = self.image1

    def adaptive_threshold(self):
        self.image2 = self.solution.adaptive_threshold()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def gaussian_filter(self):
        self.image2 = self.solution.gaussian_filter()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def bilateral_filter(self):
        self.image2 = self.solution.bilateral_filter()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def opening(self):
        self.image2 = self.solution.opening()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def closing(self):
        self.image2 = self.solution.closing()
        self.label4.configure(image=self.image2)
        self.label4.image = self.image2

    def exit(self):
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("圖像處理")
    root.geometry("1000x700")
    root.resizable(False, False)
    app = MainApp(root)
    root.mainloop()
