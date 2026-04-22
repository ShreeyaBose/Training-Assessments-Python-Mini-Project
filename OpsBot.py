import re
import os
from datetime import datetime
from tkinter import *
from tkinter import filedialog, messagebox

def process_log(fp):
    pattern=re.compile(r"(CRITICAL|ERROR|FAILED LOGIN)")
    c={"CRITICAL": 0, "ERROR": 0, "FAILED LOGIN": 0}
    date=datetime.now().strftime("%Y-%m-%d")
    output_file=f"security_alert_{date}.txt"
    with open(fp,"r") as log, open(output_file, "w") as alert:
        for i in log:
            match=pattern.search(i)
            if match:
                keyword=match.group()
                c[keyword]+=1
                if keyword=="CRITICAL":
                    alert.write(i)
    fsize=os.path.getsize(output_file)
    return c,output_file,fsize

def browse_log():
    path=filedialog.askopenfilename(title="Select server.log file")
    entry_path.delete(0, END)
    entry_path.insert(0, path)

def opsbot():
    path=entry_path.get()
    if not os.path.exists(path):
        messagebox.showerror("Error", "Please select a valid log file!")
        return
    counts,outfile,size=process_log(path)

    report=f"""Security Alert Summary:
    CRITICAL      : {counts['CRITICAL']}
    ERROR         : {counts['ERROR']}
    FAILED LOGIN  : {counts['FAILED LOGIN']}
    Alert File Created: {outfile}
    File Size: {size} bytes
    """
    messagebox.showinfo("OpsBot Report",report)

root = Tk()
root.title("OpsBot - Server Log Security Scanner")
root.geometry("520x300")
Label(root,text="OpsBot Security Log Scanner",font=("Arial", 16, "bold")).pack(pady=15)
fr=Frame(root)
fr.pack(pady=10)
entry_path=Entry(fr,width=42)
entry_path.pack(side=LEFT,padx=5)
Button(fr,text="Browse Log File",command=browse_log).pack(side=LEFT)
Button(root, text="Run OpsBot",bg="red", fg="white",font=("Arial", 12),command=opsbot).pack(pady=25)
root.mainloop()