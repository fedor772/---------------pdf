import pdfcrowd
import sys
from tkinter import *
from tkinter import ttk
import tkinter.filedialog as fd
import webbrowser
import pypdfium2 as pdfium

def convert():
    if r_var.get():
        pdf = pdfium.PdfDocument(path.get())
        for i in range(len(pdf)):
            page = pdf[i]
            image = page.render(scale=4).to_pil()
            image.save(f"{path.get()}.jpg")
        ready.config(text = "Конвертирование успешно")
        webbrowser.open(f"{path.get()}.jpg", new=2)
    else:
        try:
            client = pdfcrowd.PdfToHtmlClient('fedorr', 'f09932d1860c7013031e105fd0270379')
            client.convertFileToFile(path.get(), path.get() + ".html")
            ready.config(text = "Конвертирование успешно")
            webbrowser.open(path.get() + ".html")
        except pdfcrowd.Error as why:
            sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))
            raise

def pickfile():
    filetypes = (("Pdf файл", "*.pdf"), ("Все файлы", "*"))
    filename = fd.askopenfilename(title="Открыть файл", initialdir="/", filetypes=filetypes)
    if filename:
        path.insert(0, filename)   

root = Tk()
root.title("Конвертировать pdf")
root.geometry("350x300")

label = ttk.Label(text="Выберите путь файла")
label.grid(row=0, column=0, columnspan=10, ipadx=0, ipady=0, padx=8, pady=2)
path = ttk.Entry()
path.grid(row=1, column=0, columnspan=10, ipadx=0, ipady=0, padx=8, pady=0)
button = ttk.Button(text="Выбрать файл", command=pickfile)
button.grid(row=1, column=10, columnspan=10, ipadx=0, ipady=0, padx=8, pady=0)
r_var = BooleanVar()
r_var.set(False)
r1 = ttk.Radiobutton(text='Конвертировать в html', variable=r_var, value=False)
r2 = ttk.Radiobutton(text='Конвертировать в jpg', variable=r_var, value=True)
r1.grid(row=2, column=0, columnspan=1, ipadx=0, ipady=0, padx=8, pady=0)
r2.grid(row=2, column=10, columnspan=10, ipadx=0, ipady=0, padx=8, pady=0)
go = ttk.Button(text="Конвертировать", command=convert)
go.grid(row=3, column=0, columnspan=1, ipadx=0, ipady=0, padx=8, pady=0)
ready = ttk.Label(text="")
ready.grid(row=4, column=0, columnspan=10, ipadx=0, ipady=0, padx=8, pady=0)

root.mainloop()

