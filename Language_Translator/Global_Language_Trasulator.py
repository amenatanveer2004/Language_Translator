#***IMPORTING REQUIRED MODULES***
import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES
from tkinter import messagebox,font


#***CREATE MAIN WINDOW***
root = tk.Tk()
root.title("Global Language Translator")
root.geometry("650x700") #HEIGHT * WIDTH
root.configure(bg='#f0f8f4')


#***FRAME LAYOUT***
main_frame = tk.Frame(root, bg='#F0F4F8')
main_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

#***SETTING TITTLE***
title_label = tk.Label(main_frame, text="GLOBAL LANGUAGE TRASULATOR", 
                       font=font.Font(
                           family='roman',
                           size=18,
                           weight='bold',
                           underline=True),
                       bg='#F0F4F8',
                       fg='red')
title_label.pack(pady=10)


#***FUNCTION TO TRANSLATE TEXT***
def translate():
    # GET INPUT TEXT.....
    input_text = input_field.get("1.0", tk.END).strip()
    source_lang = source_language.get()
    dest_lang = destination_language.get()

    # VALIDATE LANGUAGE SELECETION.....
    if dest_lang == "Select Language":
        messagebox.showwarning("Warning", "Please select a Destination Language!")
        return

    # CHECKING INPUT IS EMPTY OR NOT.....
    if input_text:
        try:
            tran = Translator()
            
            # Translate tex
            result = tran.translate(
                input_text, 
                src=source_lang, 
                dest=dest_lang
            )
            
            # Clear and insert translated text
            output_field.delete("1.0", tk.END)
            output_field.insert(tk.END, result.text)
        
        except Exception as e:
            output_field.delete("1.0", tk.END)
            output_field.insert(tk.END, f"Translation error: {str(e)}")
    else:
        messagebox.showinfo("Info", "Please enter text to translate")


#***CUSTOM STYLE***
style = ttk.Style()
style.configure('TCombobox', background='#E6F2FF', font=('Arial', 10))
style.configure('TButton', background='#4CAF50', foreground='white')

#***LANGUAGE SELECTION*** 
language_list = list(LANGUAGES.values())


#***Source language***
source_label = tk.Label(main_frame, text="Source Language:", 
                        bg='#F0F4F8', 
                        font=('Arial', 12))
source_label.pack(pady=5)
source_language = ttk.Combobox(main_frame, values=language_list, width=40)
source_language.set("Auto")  #Auto-detect
source_language.pack(pady=5)

#***INPUT TEXT FIELD***
input_label = tk.Label(main_frame, text="Enter Text to Translate:", 
                       font=('Arial', 12 ,'bold'),
                       bg='#F0F4F8', 
                       fg='crimson')
input_label.pack(pady=5)
input_field = tk.Text(main_frame, 
                      height=10, 
                      width=70, 
                      font=('Arial', 10), 
                      bg='#FFFFFF', 
                      relief=tk.RIDGE, 
                      borderwidth=2)
input_field.pack(pady=5)

#***Destination language***
dest_label = tk.Label(main_frame, text="Destination Language:", 
                      bg='#F0F4F8', 
                      font=('Arial', 12))
dest_label.pack(pady=5)
destination_language = ttk.Combobox(main_frame, values=language_list, width=40)
destination_language.set("Select Language")
destination_language.pack(pady=5)

#***TRANSLATE BUTTON***
translate_button = tk.Button(main_frame, 
                              text="Translate", 
                              command=translate, 
                              bg='#4CAF50', 
                              fg='white', 
                              font=('Arial', 12, 'bold'),
                              activebackground='#45a049')
translate_button.pack(pady=10)

#***OUTPUT TEXT FIELD***
output_label = tk.Label(main_frame, text="Translated Text:", 
                        bg='#F0F4F8', 
                        font=('Arial', 12,'bold'),
                        fg='crimson')
output_label.pack(pady=5)
output_field = tk.Text(main_frame, 
                       height=10, 
                       width=70, 
                       font=('Arial', 10), 
                       bg='#FFFFFF', 
                       relief=tk.RIDGE, 
                       borderwidth=2)
output_field.pack(pady=5)

# RUN THE APPLICATION
root.mainloop()
