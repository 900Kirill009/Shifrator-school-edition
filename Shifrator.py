import tkinter as tk
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import rsa
import os

def displayStart():
  nadpis_Text.grid_remove()
  first_btn_Text.grid_remove()
  second_btn_Text.grid_remove()
  third_btn_Text.grid_remove()
  back_btn.grid_remove()

  nadpis1_Graphic.grid_remove()
  vvodpath.grid_remove()
  nadpis2_Graphic.grid_remove()
  vvodkey.grid_remove()
  knopka_Graphice.grid_remove()
  knopka_Graphicd.grid_remove()

  nadpis1_Files.grid_remove()
  nadpis2_Files.grid_remove()
  vvodpathkey.grid_remove()
  knopka_Filese.grid_remove()
  knopka_Filesd.grid_remove()
  knopka_newkey.grid_remove()

  nadpis.grid(row=1, column=2)
  probel.grid(row=2, column=2)
  first_btn.grid(row=3, column=1)
  second_btn.grid(row=3, column=2)
  third_btn.grid(row=3, column=3)

def displayTextt():
  nadpis.grid_remove()
  first_btn.grid_remove()
  second_btn.grid_remove()
  third_btn.grid_remove()

  nadpis1_Caesar.grid_remove()
  vvodteksta.grid_remove()
  nadpis2_Caesar.grid_remove()
  Cypher.grid_remove()
  nadpis3_Caesar.grid_remove()
  vvodshag.grid_remove()
  knopka_Caesar.grid_remove()
  back2Textt_btn.grid_remove()

  nadpis1_Sim.grid_remove()
  vvodteksta.grid_remove()
  nadpis2_Sim.grid_remove()
  Cypher.grid_remove()
  nadpis3_Sim.grid_remove()
  vvodkey.grid_remove()
  knopka_Sim.grid_remove()

  nadpis1_Asim.grid_remove()
  nadpis2_Asim.grid_remove()
  nadpis3_Asim.grid_remove()
  vvodpublickey.grid_remove()
  nadpis4_Asim.grid_remove()
  vvodprivatkey.grid_remove()
  tretiyprobel.grid_remove()
  knopka_Asim.grid_remove()
  knopka2_Asim.grid_remove()

  nadpis_Text.grid(row=1, column=2)
  probel.grid(row=2, column=2)
  first_btn_Text.grid(row=3, column=1)
  second_btn_Text.grid(row=3, column=2)
  third_btn_Text.grid(row=3, column=3)
  echoprobel.grid(row=4, column=2)
  back_btn.grid(row=5, column=2)

def displayCaesar():
  nadpis_Text.grid_remove()
  probel.grid_remove()
  first_btn_Text.grid_remove()
  second_btn_Text.grid_remove()
  third_btn_Text.grid_remove()
  echoprobel.grid_remove()
  back_btn.grid_remove()

  nadpis1_Caesar.grid(row=1, column=1)
  vvodteksta.grid(row=3, column=1)
  nadpis2_Caesar.grid(row=1, column=2)
  Cypher.grid(row=3, column=2)
  nadpis3_Caesar.grid(row=1, column=3)
  vvodshag.grid(row=3, column=3)
  probel.grid(row=2, column=2)
  echoprobel.grid(row=4, column=2)
  back2Textt_btn.grid(row=5, column=1)
  knopka_Caesar.grid(row=5, column=3)

def displaySim():
  nadpis_Text.grid_remove()
  probel.grid_remove()
  first_btn_Text.grid_remove()
  second_btn_Text.grid_remove()
  third_btn_Text.grid_remove()
  echoprobel.grid_remove()
  back_btn.grid_remove()

  nadpis1_Sim.grid(row=1, column=1)
  vvodteksta.grid(row=3, column=1)
  nadpis2_Sim.grid(row=1, column=2)
  Cypher.grid(row=3, column=2)
  nadpis3_Sim.grid(row=1, column=3)
  vvodkey.grid(row=3, column=3)
  probel.grid(row=2, column=2)
  echoprobel.grid(row=4, column=2)
  back2Textt_btn.grid(row=5, column=1)
  knopka_Sim.grid(row=5, column=3)

def displayAsim():
  nadpis_Text.grid_remove()
  probel.grid_remove()
  first_btn_Text.grid_remove()
  second_btn_Text.grid_remove()
  third_btn_Text.grid_remove()
  echoprobel.grid_remove()
  back_btn.grid_remove()

  nadpis1_Asim.grid(row=1, column=1)
  vvodteksta.grid(row=3, column=1)
  nadpis2_Asim.grid(row=1, column=3)
  Cypher.grid(row=3, column=3)
  nadpis3_Asim.grid(row=1, column=5)
  vvodpublickey.grid(row=3, column=5)
  nadpis4_Asim.grid(row=1, column=7)
  vvodprivatkey.grid(row=3, column=7)
  probel.grid(row=2, column=2)
  echoprobel.grid(row=4, column=4)
  tretiyprobel.grid(row=1, column=6)
  back2Textt_btn.grid(row=5, column=1)
  knopka_Asim.grid(row=5, column=7)
  knopka2_Asim.grid(row=5, column=5)

def displayGraphic():
  nadpis.grid_remove()
  first_btn.grid_remove()
  second_btn.grid_remove()
  third_btn.grid_remove()
  nadpis1_Graphic.grid(row=1,column=1)
  vvodpath.grid(row=3,column=1)
  nadpis2_Graphic.grid(row=1,column=2)
  vvodkey.grid(row=3,column=2)
  probel.grid(row=2,column=1)
  echoprobel.grid(row=4,column=2)
  back_btn.grid(row=5, column=1)
  knopka_Graphice.grid(row=5,column=2)
  knopka_Graphicd.grid(row=3,column=3)

def displayFiles():
  nadpis.grid_remove()
  first_btn.grid_remove()
  second_btn.grid_remove()
  third_btn.grid_remove()
  nadpis1_Files.grid(row=1,column=1)
  vvodpath.grid(row=1,column=2)
  nadpis2_Files.grid(row=3,column=1)
  vvodpathkey.grid(row=3,column=2)
  probel.grid(row=2,column=2)
  echoprobel.grid(row=4,column=3)
  knopka_newkey.grid(row=1,column=4)
  knopka_Filese.grid(row=3,column=4)
  knopka_Filesd.grid(row=5,column=4)
  back_btn.grid(row=7,column=4)

def Caesar():
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя0123456789,<.>/?;:[]\|=+-_()*&^%$#№@!`~ '
  tekst = str(vvodteksta.get())
  shifr = str(Cypher.get())
  shag = int(vvodshag.get())
  novCypher = ''
  novtekst = ''
  if abs(shag)>158:
    if shag<0:
      shag = shag%(-158)
      shag+=1
    elif shag>0:
      shag = shag%158
      shag-=1
  if tekst !='':
    for i in tekst:
      mesto = alphabet.find(i)
      new_mesto = mesto + shag
      if new_mesto>158:
        new_mesto-=159
      if new_mesto<0:
        new_mesto+=1
      novCypher+=str(alphabet[new_mesto])
    Cypher.delete(0, tk.END)
    Cypher.insert(0,novCypher)
  elif shifr !='':
    for i in shifr:
      mesto = alphabet.find(i)
      new_mesto = mesto - shag
      if new_mesto>158:
        new_mesto-=159
      if new_mesto<0:
        new_mesto+=1
      novtekst+=str(alphabet[new_mesto])
    vvodteksta.delete(0, tk.END)
    vvodteksta.insert(0,novtekst)

def Sim():
  tekst = str(vvodteksta.get())
  shifr = str(Cypher.get())
  key = str(vvodkey.get())
  if tekst !='':
    key = Fernet.generate_key()  
    fernet = Fernet(key)
    shifr = fernet.encrypt(tekst.encode())
    vvodkey.delete(0, tk.END)
    vvodkey.insert(0,key)
    Cypher.delete(0, tk.END)
    Cypher.insert(0,shifr)
  elif shifr!='' and key!='':
    shifr = shifr.encode()
    fernet = Fernet(key)
    tekst = fernet.decrypt(shifr).decode()
    vvodteksta.delete(0, tk.END)
    vvodteksta.insert(0, tekst)

def Asim(publickey, privatkey):
  tekst = str(vvodteksta.get())
  shifr = str(Cypher.get())
  if tekst !='':
    shifr = rsa.encrypt(tekst.encode(),publickey)
    Cypher.delete(0, tk.END)
    Cypher.insert(0, shifr)
  elif shifr!='':
    tekst = rsa.decrypt(shifr.encode,privatkey).decode()
    vvodteksta.delete(0, tk.END)
    vvodteksta.insert(0, tekst)
def genkeys():
  publickey, privatkey = rsa.newkeys(512)
  vvodpublickey.delete(0, tk.END)
  vvodpublickey.insert(0,publickey)
  vvodprivatkey.delete(0, tk.END)
  vvodprivatkey.insert(0,privatkey)
  return publickey, privatkey

def Graphice():
  path = str(vvodpath.get())
  key = int(vvodkey.get())
  try:
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    messagebox.showinfo('УСПЕХ!','Шифрование изображения успешно проведено. Проверьте файл, путь на который Вы указывали.')
  except Exception:
    messagebox.showinfo('НЕУДАЧА!','Что-то пошло не так...')
def Graphicd():
  path = str(vvodpath.get())
  key = int(vvodkey.get())
  try:
    fin = open(path, 'rb')
    image = fin.read()
    fin.close()
    image = bytearray(image)
    for index, values in enumerate(image):
      image[index] = values ^ key
    fin = open(path, 'wb')
    fin.write(image)
    fin.close()
    messagebox.showinfo('УСПЕХ!','Дешифрование изображения успешно проведено. Проверьте файл, путь на который Вы указывали.')
  except Exception:
    messagebox.showinfo('НЕУДАЧА!','Что-то пошло не так...')

def newkey():
  key = Fernet.generate_key()
  with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

def Filese():
  path = str(vvodpath.get())
  key = str(vvodpathkey.get())
  with open(key, 'rb') as filekey:
    key = filekey.read()
  fernet = Fernet(key)
  with open(path, 'rb') as file:
    original = file.read()
  encrypted = fernet.encrypt(original)
  with open(path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

def Filesd():
  path = str(vvodpath.get())
  key = str(vvodpathkey.get())
  with open(key, 'rb') as filekey:
    key = filekey.read()
  fernet = Fernet(key)
  with open(path, 'rb') as enc_file:
      encrypted = enc_file.read()
  decrypted = fernet.decrypt(encrypted)
  with open(path, 'wb') as dec_file:
      dec_file.write(decrypted)

window = Tk()
window.title("Ваш личный криптограф")
window.geometry('1600x450')

f = open('lock-1913236-1619570.png')
icon = os.path.realpath(f.name)
f.close()
window.iconphoto(True, tk.PhotoImage(file=icon))

frame = Frame(window,padx = 10,pady = 10)
frame.pack(expand=True)
nadpis = Label(frame,text="Вы хотите зашифровать/дешифровать:",font='Calibry 15')
probel = Label(frame)
first_btn = Button(frame,text='Текст',font='Calibry 15',command=displayTextt, cursor='hand2')
second_btn = Button(frame,text='Графика',font='Calibry 15',command=displayGraphic, cursor='hand2')
third_btn = Button(frame,text='Файл',font='Calibry 15',command=displayFiles, cursor='hand2')

nadpis_Text = Label(frame,text="Выберите способ шифровки:",font='Calibry 15')
first_btn_Text = Button(frame,text='Шифр Цезаря',font='Calibry 15',command=displayCaesar, cursor='hand2')
second_btn_Text = Button(frame,text='Симметричное шифрование',font='Calibry 15',command=displaySim, cursor='hand2')
third_btn_Text = Button(frame,text='Асимметричное шифрование',font='Calibry 15',command=displayAsim, cursor='hand2')
echoprobel = Label(frame)
back_btn = Button(frame,text='Назад',font='Calibry 15',command=displayStart, cursor='hand2')

nadpis1_Caesar = Label(frame,text="Текст",font='Calibry 15')
vvodteksta = Entry(frame, width=50, justify=['center'])
nadpis2_Caesar = Label(frame,text="Шифр",font='Calibry 15')
Cypher = Entry(frame, width=50)
nadpis3_Caesar = Label(frame,text="Шаг",font='Calibry 15')
vvodshag = Entry(frame, width=50)
knopka_Caesar = Button(frame,text='Преобразование',font='Calibry 15',command=Caesar, cursor='hand2')
back2Textt_btn = Button(frame,text='Назад',font='Calibry 15',command=displayTextt, cursor='hand2')

nadpis1_Sim = Label(frame,text="Текст",font='Calibry 15')
vvodteksta = Entry(frame, width=50)
nadpis2_Sim = Label(frame,text="Шифр",font='Calibry 15')
Cypher = Entry(frame, width=50)
nadpis3_Sim = Label(frame,text="Ключ",font='Calibry 15')
vvodkey = Entry(frame, width=50)
knopka_Sim = Button(frame,text='Преобразование',font='Calibry 15',command=Sim, cursor='hand2')

nadpis1_Asim = Label(frame,text="Текст",font='Calibry 15')
vvodteksta = Entry(frame, width=50)
nadpis2_Asim = Label(frame,text="Шифр",font='Calibry 15')
Cypher = Entry(frame, width=50)
nadpis3_Asim = Label(frame,text="Публичный ключ",font='Calibry 15')
vvodpublickey = Entry(frame, width=50)
nadpis4_Asim = Label(frame,text="Закрытый ключ",font='Calibry 15')
vvodprivatkey = Entry(frame, width=50)

if vvodpublickey.get()=='' and vvodprivatkey.get()=='':
  publickey, privatkey = genkeys()

knopka_Asim = Button(frame,text='Шифрование',font='Calibry 15',command=lambda: Asim(publickey, privatkey), cursor='hand2')
knopka2_Asim = Button(frame,text='Смена ключей',font='Calibry 15',command=genkeys, cursor='hand2')
tretiyprobel = Label(frame)

nadpis1_Graphic = Label(frame,text="Путь к изображению",font='Calibry 15')
vvodpath = Entry(frame, width=50)
nadpis2_Graphic = Label(frame,text="Ключ",font='Calibry 15')
vvodkey = Entry(frame, width=50)
knopka_Graphice = Button(frame,text='Шифрование',font='Calibry 15',command=Graphice, cursor='hand2')
knopka_Graphicd = Button(frame,text='Дешифрование',font='Calibry 15',command=Graphicd, cursor='hand2')

nadpis1_Files = Label(frame,text="Путь к файлу",font='Calibry 15')
vvodpath = Entry(frame, width=50)
nadpis2_Files = Label(frame,text=" Путь к файлу-ключу ",font='Calibry 15')
vvodpathkey = Entry(frame, width=50)
knopka_Filese = Button(frame,text='Шифрование',font='Calibry 15',command=Filese, cursor='hand2')
knopka_Filesd = Button(frame,text='Дешифрование',font='Calibry 15',command=Filesd, cursor='hand2')
knopka_newkey = Button(frame, text='Сгенерировать новый ключ', font='Calibry 15',command=newkey, cursor='hand2')

nadpis.grid(row=1, column=2)
probel.grid(row=2, column=2)
first_btn.grid(row=3, column=1)
second_btn.grid(row=3, column=2)
third_btn.grid(row=3, column=3)
window.mainloop()