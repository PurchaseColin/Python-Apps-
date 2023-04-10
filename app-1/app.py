import tkinter as tk 
from tkinter import filedialog, Text
import os 
import subprocess

root = tk.Tk()

apps = []


if os.path.isfile('save.txt'): 
 with open('save.txt', 'r') as f: 
  tempApps = f.read()
  tempApps = tempApps.split(',')
  apps = [x for x in tempApps if x.strip()]




def addApp (): 

 for widget in frame.winfo_children(): 
  widget.destroy()

 filename = filedialog.askopenfilename(initialdir = "/", title="Select File", filetypes=(("executables", "*.app"),("all files", "all files", ".txt"),))

 apps.append(filename)
 print(filename)
 for app in apps: 
  label = tk.Label(frame, text=app, bg="#2F5061")
  label.pack()



def runApps(): 
 for app in apps: 
  appname = str(app)
  subprocess.call(['open', appname])



canvas = tk.Canvas(root, height = 500, width=500, bg="#FBC490")
canvas.pack()

frame = tk.Frame(root, bg="#F67B50")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

openFile = tk.Button(root, text="Open File", padx= 10, pady=5, fg="#FBAA60", bg ="#A82810", command=addApp)
openFile.pack()

runApps = tk.Button(root, text = "Run Apps", padx= 10, pady=5, fg="#FBAA60", bg ="#A82810", command=runApps)
runApps.pack()

for app in apps: 
 label = tk.Label(frame, text=app )
 label.pack()


root.mainloop() 

with open("save.txt", 'w') as f: 
 for app in apps: 
  f.write(app + ',')