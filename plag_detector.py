import tkinter as tk
from tkinter import filedialog
from plagiarism_check import compare_text

def load_file_or_display_contents(entry, text_widget):
    file_path = filedialog.askopenfilename()
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(tk.END, file_path)
        with open(file_path, 'r') as file:
            text = file.read()
            text_widget.delete(1.0, tk.END)
            text_widget.insert(tk.END, text)

def load_multiple_files():
    file_paths = filedialog.askopenfilenames()
    return file_paths

def show_similarity():
    text1 = text_textbox1.get("1.0", tk.END).strip()
    
    file_paths = load_multiple_files()
    if not file_paths:
        result_label.config(text="No files selected", bg='white')
        return

    for widget in result_frame.winfo_children():
        widget.destroy()

    results = []
    
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            text2 = file.read().strip()
        similarity_percentage, diff = compare_text(text1, text2)
        results.append((file_path, similarity_percentage))
    
    results.sort(key=lambda x: x[1], reverse=True)
    
    for file_path, similarity in results:
        if similarity <= 30:
            color = 'green'
        elif similarity <= 60:
            color = 'yellow'
        else:
            color = 'red'
        
        file_label = tk.Label(result_frame, text=f"File: {file_path}\nSimilarity: {similarity}%", bg=color, wraplength=400)
        file_label.pack(pady=5)

root = tk.Tk()
root.title("Plagiarism Detector")

frame = tk.Frame(root)
frame.pack(pady=10)

text_label1 = tk.Label(frame, text="Text 1")
text_label1.grid(row=0, column=0, padx=5, pady=5)
text_textbox1 = tk.Text(frame, wrap=tk.WORD, width=40, height=10)
text_textbox1.grid(row=0, column=1, padx=5, pady=5)

file_entry1 = tk.Entry(frame, width=50)
file_entry1.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
load_button1 = tk.Button(frame, text="Load Text 1 File", command=lambda: load_file_or_display_contents(file_entry1, text_textbox1))
load_button1.grid(row=1, column=0, padx=5, pady=5)

compare_button = tk.Button(root, text="Compare with Multiple Files", command=show_similarity)
compare_button.pack(pady=5)

result_frame = tk.Frame(root)
result_frame.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

root.mainloop()
 
