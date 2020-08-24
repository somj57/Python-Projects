from PIL import Image
from tkinter import *
#import sys
from os import path
import os,glob
exepath = os.path.dirname(sys.executable)
#exepath=os.getcwd()
window=Tk("")
window.wm_title("Converter")

def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    os.chdir(selected_tuple)
    file_name = sorted(glob.glob("./*"))
    sorted(file_name)
    list1.delete(0,END)
    for row in file_name:
    	disp=os.path.basename(row)
    	list1.insert(END,disp)

def go():
	#os.chdir('..')
	from PIL import Image
	# file_name = glob.glob("./*")
	file_name=sorted(os.listdir(os.getcwd()))
	list1.delete(0,END)
	imlist=[]
	for i in file_name:
		if (i.endswith(".jpg"))or(i.endswith(".png"))or(i.endswith(".jpeg"))or(i.endswith(".JPG"))or(i.endswith(".JPEG")):
			pt=os.path.basename(i)
			list1.insert(END,pt)
			image1= Image.open(pt)
			im1 = image1.convert('RGB')
			imlist.append(im1)
		

	img1= imlist[0]
	imlist.pop(0)
	img1.save(r'Work.pdf',save_all=True,append_images=imlist)
	

def back():
	os.chdir('..')
	#os.chdir(exepath)
	file_name = sorted(glob.glob("./*"))
	sorted(file_name)
	list1.delete(0,END)
	for row in file_name:
		disp=os.path.basename(row)
		list1.insert(END,disp)
def st():
	os.chdir(exepath)
	file_name = sorted(glob.glob("./*"))
	list1.delete(0,END)
	for row in file_name:
		disp=os.path.basename(row)
		list1.insert(END,disp)


b1=Button(window,text="Go",width=12,command=go)
b1.grid(row=2,column=3)

b2=Button(window,text="Back",width=12,command=back)
b2.grid(row=3,column=3)

b3=Button(window,text="Start",width=12,command=st)
b3.grid(row=4,column=3)

list1=Listbox(window, height=8,width=50)
list1.grid(row=0,column=0,rowspan=6,columnspan=2)

# sb1=Scrollbar(window)
# sb1.grid(row=2,column=2,rowspan=6)

# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)
b6=Button(window,text="Close", width=12,command=window.destroy)
b6.grid(row=5,column=3)


#window.geometry("500x100")
window.mainloop()