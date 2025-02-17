import tkinter as tk

def main():
    # Crear una ventana principal
    root = tk.Tk()
    root.title("Mi ventana Tkinter")

    # Crear una etiqueta con el texto
    label = tk.Label(root, text="¡Hola, Tkinter!", font=("Arial", 24))
    label.pack(padx=20, pady=20)

    # Ejecutar el bucle principal de Tkinter para mostrar la ventana
    root.mainloop()

if __name__ == "__main__":
    main()
