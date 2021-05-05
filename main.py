import tkinter as tk
 
 
def updateList(new_data):
    auto_complete_list.delete(0,tk.END)
    
    for item in new_data:
        auto_complete_list.insert(tk.END,item)
        
def auto_complete_entry(event):
    text = entry.get()
    entry.insert(len(text), auto_complete_list.get(tk.ANCHOR))

def outo_complete(event):
     text = entry.get()
     print(text)
     # TODO:  
     # get the last 2 words
     # using the model sugest list of words[]
     # call updateList(words[])
    

root = tk.Tk()
root.title("Auto Complete")
root.geometry("500x300")
    
        
title = tk.Label(root,text="Start Typing.." , font=(30))
title.pack(pady=20)


entry = tk.Entry(root,font=(20),)
entry.pack(pady=20)


auto_complete_list = tk.Listbox(root,width = 50 ,font=(20))
auto_complete_list.pack(pady=20)


data = ['word1','word2','word3','word4','word5','word6','word7','word8','word9']
updateList(data)


auto_complete_list.bind("<<ListboxSelect>>" , auto_complete_entry)

entry.bind("<space>", outo_complete)

root.mainloop()