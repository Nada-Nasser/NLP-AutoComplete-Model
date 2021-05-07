import tkinter as tk
import trigram_model
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer("[\w']+")


def update_list(new_data):
    auto_complete_list.delete(0, tk.END)

    for item in new_data:
        auto_complete_list.insert(tk.END, item[1])


def auto_complete_entry(event):
    text = entry.get()
    entry.focus_set()
    entry.insert(len(text), auto_complete_list.get(tk.ANCHOR))


def auto_complete(event):
    text = entry.get()
    print(text)

    tokens = tokenizer.tokenize(text)
    accumulator = 1.0
    for i in range(len(tokens) - 2):
        t = " ".join(tokens[i:i + 2])
        if t in trigram_model.unsorted_model:
            prob = trigram_model.unsorted_model[t, tokens[i + 2]]
            accumulator *= prob
        else:
            accumulator *= 0

    t = " ".join(tokens[-2:])

    if t in trigram_model.model:
        suggest = trigram_model.model[t]
        print(trigram_model.model[t][0][1])
        accumulator *= trigram_model.model[t][0][0]
    else:
        print("no suggestion")
        suggest = []

    update_list(suggest)
    print("Probability of text = ", accumulator)


root = tk.Tk()
root.title("Auto Complete")
root.geometry("500x300")

title = tk.Label(root, text="Start Typing..", font=30)
title.pack(pady=20)

entry = tk.Entry(root, font=20,width=50,)
entry.pack(pady=20)

auto_complete_list = tk.Listbox(root, width=50, font=20, justify="right")
auto_complete_list.pack(pady=20)

auto_complete_list.bind("<<ListboxSelect>>", auto_complete_entry)

entry.bind("<space>", auto_complete)

root.mainloop()
