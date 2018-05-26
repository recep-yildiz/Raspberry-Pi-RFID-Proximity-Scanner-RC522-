# -*- coding: utf-8 -*-
#GUI, DB libs
from tkinter import *
import sys
import sqlite3
import time
import datetime

#RFID Libs
sys.path.insert(0, "/home/pi/pi-rc522/")
from pirc522 import RFID
import signal

#Create DB
mydb = sqlite3.connect('userrecords.db')
myc = mydb.cursor()

rdr = RFID()
util = rdr.util()
util.debug = False

root=Tk()

class MainWindow():
     def __init__(self,master, **kwargs):
          self.master=master
          self.master.geometry('320x130+100+200')
          self.master.title('PROJECT MIFARE')
          
          self.label1=Label(self.master,text='\tRFID TANI SISTEMINE HOSGELDINIZ\t ',fg='white', bg='black').grid(row=0,column=1)
          self.button1=Button(self.master,text="KULLANICI EKLE",fg='black', bg='white', command=self.goto_addUser, width=16).grid(row=1,column=1)
          self.button2=Button(self.master,text="KULLANICI SORGULA",fg='black', bg='white', command=self.goto_userQuery, width=16).grid(row=2,column=1)
          self.button3=Button(self.master,text="KAYITLAR",fg='black', bg='white', command=self.gotorecords, width=16).grid(row=3,column=1)
          self.button4=Button(self.master,text="CIKIS",fg='black', bg='white', command=self.exit, width=16).grid(row=4,column=1)

     def exit(self):
          self.master.destroy()

     def goto_addUser(self):
          #Add User Window    
          root2=Toplevel(self.master)
          myGUI=addUser(root2)

     def goto_userQuery(self):
          root2=Toplevel(self.master)
          myGUI=userQuery(root2)

     def gotorecords(self):
         #Records before adding new user
          root2=Toplevel(self.master)
          myGUI=records(root2)

class addUser():
     def __init__(self,master):
          
          myc.execute("""CREATE TABLE IF NOT EXISTS KayitDefteri(Tarih TEXT, Ad TEXT, Soyad TEXT, OGR TEXT, uid TEXT)""")
                    
          self.name=StringVar()
          self.surname=StringVar()
          self.number=StringVar()

          self.master=master
          self.master.geometry('445x360+100+200')
          self.master.title('KULLANICI EKLE')

          self.label2=Label(self.master,text='>>Kullanıcı Parametreleri\n',fg='blue').grid(row=0,column=1)
          self.label2=Label(self.master,text='Ad: ',fg='black').grid(row=3,column=0)
          self.label2=Label(self.master,text='Soyad: ',fg='black').grid(row=4,column=0)
          self.label2=Label(self.master,text='Numara: ',fg='black').grid(row=5,column=0)
          
          self.mynamevar=Entry(self.master,textvariable=str(self.name)).grid(row=3,column=1)
          self.mysurnamevar=Entry(self.master,textvariable=str(self.surname)).grid(row=4,column=1)
          self.mynumbervar=Entry(self.master,textvariable=str(self.number)).grid(row=5,column=1)
          self.button5=Button(self.master,text="OLUSTUR",fg='blue',command=self.createRecord, width=18).grid(row=3,column=2)
          self.button6=Button(self.master,text="CIKIS",fg='red',command=self.exit, width=18).grid(row=5,column=2)

          
     def readTag(self):
          global readTag
          global cardid
          #Card ID Query Loop
          while True:
               (error, data) = rdr.request()
               if not error:
                    self.label2=Label(self.master, text='\nTespit Edildi!', fg='purple').grid(row=11, column=1)
                    (error, uid) = rdr.anticoll()
                    if not error:
                         #Get Card ID
                         self.label3=Label(self.master, text='\nOkunan Kart ID: ' + str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]), fg='purple').grid(row=12, column=1)
                         time.sleep(0.2)
                         break
          time.sleep(1)
          cardid=str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
          self.button6=Button(self.master,text="VERI TABANINA EKLE",fg='blue',command=self.dynamic_data_entry, width=18).grid(row=4,column=2)

          
                    
     def createRecord(self):
          #self.label1=Label(self.master,text='>SIMDI \'RFID TAG\' ILE KARTI CIHAZA\nOKUTUNUZ!', fg='green').grid(row=9,column=1)
          self.label1=Label(self.master,text='SIMDI RFID TAG ILE KARTI OKUTUNUZ', fg='green').grid(row=7,column=1)
          self.button4=Button(self.master,text="RFID TAG",fg='red',command=self.readTag).grid(row=10,column=1)
          

     def dynamic_data_entry(self):
          global dynamic_data_entry
          tarih = str(datetime.datetime.now().date()) 
          getname = str(self.name.get())
          getsurname = str(self.surname.get())
          getnumber=str(self.number.get())
          myc.execute("INSERT INTO KayitDefteri (Tarih, Ad, Soyad, OGR, uid) VALUES (?, ?, ?, ?, ?)",(tarih, getname, getsurname, getnumber, cardid))
          mydb.commit()
          self.writetodatabase()

     def writetodatabase(self):
          for i in range(1):
               time.sleep(1)
          #When execute two lines below, can't be adding new user more from mainwindow
          #myc.close()
          #mydb.close()

     def exit(self):
          self.master.destroy()

class userQuery():
     def __init__(self,master):
        self.master=master
        self.master.geometry('375x220+100+200')
        self.master.title('KULLANICI')
        self.connection = sqlite3.connect('userrecords.db')
        self.cur = self.connection.cursor()
        self.orderLabel=Label(self.master,text='LUTFEN KARTI\n TARAYICIYA OKUTUNUZ... ',fg='blue', width=45).grid(row=2,column=1)
        self.rfidgif=Button(self.master,text="RFID ON",fg='green',command=self.gif_display, width=15).grid(row=5,column=1)


     #image adding test
     def gif_display(self):
        #Imaged Button Test
        """self.rfidgif=Button(root, justify=LEFT)
        photo=PhotoImage(file="rfid.gif")
        self.rfidgif.config(image=photo, width="200", height="200")
        self.rfidgif.grid(row=4, column=2)"""
        while True:
               (error, data) = rdr.request()
               if not error:
                    self.label2=Label(self.master, text='\nTespit Edildi!', fg='purple').grid(row=11, column=1)
                    (error, uid) = rdr.anticoll()
                    if not error:
                         #Kart ID
                         self.label3=Label(self.master, text='\nOkunan Kart ID: ' + str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]), fg='purple').grid(row=12, column=1)
                         ctrlID=str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
                         time.sleep(0.2)
                         break

        myc.execute("SELECT * FROM KayitDefteri WHERE uid=:id", {"id": ctrlID})
        id_exist = myc.fetchone()

        if id_exist:
             self.deneme=Label(self.master,text='{}'.format(id_exist),fg='red', width=45).grid(row=14,column=1)
             
        else:
             self.orderLabel=Label(self.master,text='SONUC: KULLANICI BULUNAMADI!',fg='red', width=50).grid(row=16,column=1)
        
class records():
    def __init__(self,master):
        self.master=master
        self.master.geometry('470x320+100+200')
        self.master.title('KAYITLAR')
        self.connection = sqlite3.connect('userrecords.db')
        self.cur = self.connection.cursor()
        self.dateLabel = Label(self.master, text="TARIH", width=10)
        self.dateLabel.grid(row=0, column=0)
        self.nameLabel = Label(self.master, text="AD", width=10)
        self.nameLabel.grid(row=0, column=1)
        self.surnameLabel = Label(self.master, text="SOYAD", width=10)
        self.surnameLabel.grid(row=0, column=2)
        self.numberLabel = Label(self.master, text="OGR No", width=13)
        self.numberLabel.grid(row=0, column=3)
        self.uidLabel = Label(self.master, text="UID", width=13)
        self.uidLabel.grid(row=0, column=4)
        
        self.showallrecords()

    def showallrecords(self):
        data = self.readfromdatabase()
        for index, dat in enumerate(data):
            Label(self.master, text=dat[0]).grid(row=index+1, column=0)
            Label(self.master, text=dat[1]).grid(row=index+1, column=1)
            Label(self.master, text=dat[2]).grid(row=index+1, column=2)
            Label(self.master, text=dat[3]).grid(row=index+1, column=3)
            Label(self.master, text=dat[4]).grid(row=index+1, column=4)

    def readfromdatabase(self):
        self.cur.execute("SELECT * FROM KayitDefteri")
        return self.cur.fetchall()

def main():
     myGUIWelcome=MainWindow(root)
     root.mainloop()

if __name__ == '__main__':
     main()

