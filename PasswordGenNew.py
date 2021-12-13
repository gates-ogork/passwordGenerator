import random
import tkinter

main_window=tkinter.Tk()
main_window.title("Gates' Password Generator")
main_window.geometry('285x175')
padd=50
main_window['padx']=padd
chk1=tkinter.IntVar()
chk2=tkinter.IntVar()
chk3=tkinter.IntVar()
chk4=tkinter.IntVar()


def password_generate(leng):
    valid_char="abcdefghijklmnopqrstuvwxvyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    password="".join(random.sample(valid_char, leng))
    display_result.delete(0, tkinter.END)
    display_result.insert(0, password)

def checkbox_check():
    if chk1.get()==6:
        password_generate(6)
    elif chk2.get()==10:
        password_generate(10)
    elif chk3.get()==12:
        password_generate(12)
    elif chk4.get()==15:
        password_generate(15)
    else:
        password_generate(8)


title_text=tkinter.Label(text= 'Gates Password Generator')
title_text.grid(row=0, column=0)
display_result=tkinter.Entry()
display_result.grid(row=1, column=0)
chkone=tkinter.Checkbutton(text='6 Character', onvalue= 6, offvalue= 0, variable= chk1)
chkone.grid(row=2, column= 0)
chktwo=tkinter.Checkbutton(text='10 Character', onvalue= 10, offvalue= 0, variable= chk2)
chktwo.grid(row=3, column= 0)
chkthree=tkinter.Checkbutton(text='12 Character', onvalue= 12, offvalue= 0, variable= chk3)
chkthree.grid(row=4, column= 0)
chkfour=tkinter.Checkbutton(text='15 Character', onvalue= 15, offvalue= 0, variable= chk4)
chkfour.grid(row=5, column= 0)
pass_generate=tkinter.Button(text='Generate', command= checkbox_check)
pass_generate.grid(row=6, column=0)
main_window.mainloop()