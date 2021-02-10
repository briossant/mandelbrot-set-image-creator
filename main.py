#!/home/bcr/anaconda3/bin/python
# -*- coding: utf-8 -*-

import tkinter as tk
import functions


class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Mandelbrot')
        master.geometry('700x250')

        self.create_widgets()

    def create_widgets(self):
        # entry
        self.size_label = tk.Label(self.master, text='Image size length x height :', font=('bold', 14), pady=10)
        self.size_label.grid(row=0, column=0, sticky=tk.W)
        self.size_entry = tk.Entry(self.master, width=15)
        self.size_entry.insert(tk.END, '400x400')
        self.size_entry.grid(row=0, column=1, columnspan=10, sticky=tk.W)

        self.name_label = tk.Label(self.master, text='Image name :', font=('bold', 14), pady=10)
        self.name_label.grid(row=1, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, width=15)
        self.name_entry.insert(tk.END, 'myImage')
        self.name_entry.grid(row=1, column=1, columnspan=10, sticky=tk.W)

        self.iter_label = tk.Label(self.master, text='max iterations :', font=('bold', 14), pady=10)
        self.iter_label.grid(row=2, column=0, sticky=tk.W)
        self.iter_entry = tk.Entry(self.master, width=15)
        self.iter_entry.insert(tk.END, '80')
        self.iter_entry.grid(row=2, column=1, columnspan=10, sticky=tk.W)

        self.re_label = tk.Label(self.master, text='real start x end :', font=('bold', 14), pady=10)
        self.re_label.grid(row=3, column=0, sticky=tk.W)
        self.re_entry = tk.Entry(self.master, width=25)
        self.re_entry.insert(tk.END, '0.36x0.37')
        self.re_entry.grid(row=3, column=1, columnspan=10, sticky=tk.W)

        self.im_label = tk.Label(self.master, text='imaginary start x end :', font=('bold', 14), pady=10)
        self.im_label.grid(row=4, column=0, sticky=tk.W)
        self.im_entry = tk.Entry(self.master, width=25)
        self.im_entry.insert(tk.END, '-0.63x-0.64')
        self.im_entry.grid(row=4, column=1, columnspan=10, sticky=tk.W)

        # Colors

        self.red_label = tk.Label(self.master, text='red :', font=('bold', 14), pady=10)
        self.red_label.grid(row=0, column=2, sticky=tk.E)
        self.red = tk.Scale(self.master, from_=0, to=255, orient='horizontal')
        self.red.set(255)
        self.red.grid(row=0, column=3, sticky=tk.E)

        self.green_label = tk.Label(self.master, text='green :', font=('bold', 14), pady=10)
        self.green_label.grid(row=1, column=2, sticky=tk.E)
        self.green = tk.Scale(self.master, from_=0, to=255, orient='horizontal')
        self.green.set(0)
        self.green.grid(row=1, column=3, sticky=tk.E)

        self.blue_label = tk.Label(self.master, text='blue :', font=('bold', 14), pady=10)
        self.blue_label.grid(row=2, column=2, sticky=tk.E)
        self.blue = tk.Scale(self.master, from_=0, to=255, orient='horizontal')
        self.blue.set(255)
        self.blue.grid(row=2, column=3, sticky=tk.E)

        # save check

        self.check_var = tk.IntVar()
        self.save_check = tk.Checkbutton(self.master, text='Save image ?', variable=self.check_var, onvalue=1,
                                         offvalue=0)
        self.save_check.grid(row=3, column=3, pady=10)

        # Buttons
        self.create_btn = tk.Button(self.master, text="Create image", width=12, command=self.create_img)
        self.create_btn.grid(row=5, column=1, pady=10)

    def create_img(self):
        try:
            [L, H] = self.size_entry.get().split('x')
            name = self.name_entry.get()

            re = self.re_entry.get().split('x')
            im = self.im_entry.get().split('x')

            max_iter = int(self.iter_entry.get())

            inter = {
                're_start': float(re[0]),
                're_end': float(re[1]),
                'im_start': float(im[0]),
                'im_end': float(im[1])
            }

            colors = [int(self.red.get()),
                      int(self.green.get()),
                      int(self.blue.get())]

            functions.px_calculator(l=int(L), h=int(H), name=name, is_save=self.check_var.get(), inter=inter,
                                    max_iteration=max_iter, colors=colors)
        except ValueError:
            functions.px_calculator(is_save=1)


l = 4000
h = 4000

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(root)
    app.mainloop()
