import tkinter as tk

app = tk.Tk()
nombre = tk.StringVar(app)
entrada = tk.StringVar(app)
app.geometry('600x400')#forma de la ventana(anchura x altura)
app.configure(background='black')
tk.Wm.wm_title(app, 'Peleas Ninja')


#Boton
tk.Button(
    app,
    text="Click me",
    font=('Courier',14),#Tipo de letra y tamano
    bg='#00a8e8',
    fg='white',
    command=lambda: print('Bienvenidos al Entrenamiento Ninja' + nombre.get()),
    relief='flat'
).pack(
    fill=tk.BOTH,#rellenar el boton
    expand=True#se expande si hay un cambio de tamano
)

#imprime texto
tk.Label(
    app,
    textvariable=nombre,
    fg='white',
    justify='center'
).pack(
    fill=tk.BOTH,#rellenar el boton
    expand=True#se expande si hay un cambio de tamano
)

tk.Entry(
    app,
    font=('Courier',14),#Tipo de letra y tamano
    bg="#713838",
    fg='white',
    justify='center'
).pack(
    fill=tk.BOTH,#rellenar el boton
    expand=True#se expande si hay un cambio de tamano
)

app.mainloop()#actualiza los cambios