This project is a Global Language Translator application built using Python's Tkinter library for the graphical user interface (GUI) and the Googletrans library for text translation. Below is an explanation of its components, functionality.

Modules Installed:
python from https://www.python.org/downloads/

tkinter command-- pip install tkinter

googletrans command-- pip install googletrans==4.0.0-rc1

How It Works:
1.Input Text: --Users type the text they want to translate into the input field.

2.Language Selection: --The source language can be set to "Auto" for automatic detection or manually selected from a dropdown menu. --The destination language must be selected from another dropdown menu.

3.Translation Process: --When the "Translate" button is clicked, the translate() function is called. --The function retrieves the input text, source language, and destination language. --It uses Translator().translate() from Googletrans to perform the translation.

4.Output Display: --The translated text is displayed in the output field.

key features:
1.Graphical User Interface (GUI): --Built using Tkinter, a Python library for creating desktop applications. --Includes dropdown menus for language selection, text input and output fields, and buttons.

2.Translation Functionality: --Utilizes the Googletrans library to perform translations. --Supports automatic detection of the source language. --Provides translations for a wide range of languages.

3.Error Handling: --Displays warnings if no destination language is selected or if the input text field is empty. --Catches exceptions during translation and displays error messages in the output field.

4.Custom Styling: --Uses Tkinter's ttk.Style to customize dropdown menus and buttons for a modern look.
