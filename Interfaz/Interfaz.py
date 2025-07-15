import tkinter as tk

app = tk.Tk()
nombre = tk.StringVar(app)
entrada = tk.StringVar(app)  # Esta variable se usará para el Entry
app.geometry('600x400')  # forma de la ventana(anchura x altura)
app.configure(background='black')
tk.Wm.wm_title(app, 'Peleas Ninja')

def saludar():
    nombre.set("Bienvido al entrenamiento ninja: " + entrada.get())

# Campo de entrada (Entry)
tk.Entry(
    app,
    font=('Courier', 14),  # Tipo de letra y tamaño
    bg="white",
    fg='black',
    justify='center',
    textvariable=entrada  # Vinculamos el Entry con la variable 'entrada'
).pack(
    fill=tk.BOTH,  # rellenar el botón
    expand=True  # se expande si hay un cambio de tamaño
)

# Botón
tk.Button(
    app,
    text="Click me",
    font=('Courier', 14),  # Tipo de letra y tamaño
    bg="#e5f1f6",
    fg='black',
    command=saludar,  # Usamos entrada.get() para capturar lo que el usuario ingresa
    relief='flat'
).pack(
    fill=tk.BOTH,  # rellenar el botón
    expand=True  # se expande si hay un cambio de tamaño
)

# Imprime texto (Label)
tk.Label(
    app,
    text="Inge",
    textvariable=nombre,
    font=('Courier', 14),
    bg='white',
    fg='black',
    justify='center'
).pack(
    fill=tk.BOTH,  # rellenar el botón
    expand=True  # se expande si hay un cambio de tamaño
)

app.mainloop()  # actualiza los cambios
