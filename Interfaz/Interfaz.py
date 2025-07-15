import tkinter as tk                # Importa la biblioteca Tkinter para interfaces gráficas
from tkinter import messagebox      # Importa la función de cuadros de mensaje
from CrudAdministrador.CRUD import CrudAdministracion as admin#Usar __init__.py para usar directorios como paquetes


# Datos de acceso correctos (puedes cambiarlos)
USUARIO_CORRECTO = "ninja"          # Usuario válido
CONTRASENA_CORRECTA = "1234"        # Contraseña válida
# Crea la ventana principal
app = tk.Tk()
app.geometry('600x400')             # Establece el tamaño de la ventana (ancho x alto)
app.configure(background='black')   # Color de fondo de la ventana
app.title('Login Ninja') # Título de la ventana

# Variables de control que se enlazan con los campos de texto
usuario = tk.StringVar(app)         # Variable para almacenar el nombre de usuario ingresado
contrasena = tk.StringVar(app)      # Variable para almacenar la contraseña ingresada
mensaje = tk.StringVar(app)         # Variable para mostrar mensajes (ej: error o bienvenida)

# Función que verifica si los datos ingresados son correctos
def verificar_login():
    # Compara lo que el usuario ingresó con los datos correctos
    if usuario.get() == USUARIO_CORRECTO and contrasena.get() == CONTRASENA_CORRECTA:
        mensaje.set(f"Bienvenido, ninja {usuario.get()}!")  # Muestra mensaje de éxito
        # Aquí podrías abrir otra ventana o continuar al siguiente menú
    else:
        mensaje.set("Usuario o contraseña incorrectos")  # Muestra mensaje de error
        # También podrías mostrar una ventana emergente de error:
        # messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# ===== INTERFAZ GRÁFICA (Widgets) =====

# Campo de texto para ingresar el nombre de usuario
tk.Entry(
    app,
    font=('Courier', 14),           # Fuente y tamaño del texto
    bg="white",                     # Fondo blanco
    fg='black',                     # Texto en negro
    justify='center',               # Centra el texto dentro del Entry
    textvariable=usuario            # Enlaza la entrada con la variable 'usuario'
).pack(pady=10, fill=tk.X, padx=50) # Agrega márgenes verticales y horizontales, y llena en X
"""pady=10: Agrega espacio vertical (padding) de 10 píxeles arriba y abajo del widget.
Hace que no esté "pegado" a otros elementos verticalmente.

padx=50: Agrega espacio horizontal (padding) de 50 píxeles a la izquierda y derecha del widget.
Se separa de los bordes laterales de la ventana o de otros widgets.

fill=tk.X: Hace que el widget se expanda horizontalmente (a lo ancho) hasta llenar el espacio disponible.
Útil cuando quieres que un Entry, Button, Label, etc., ocupen todo el ancho disponible en su línea."""

# Campo de texto para ingresar la contraseña
tk.Entry(
    app,
    font=('Courier', 14),
    bg="white",
    fg='black',
    justify='center',
    textvariable=contrasena,        # Enlaza con la variable 'contrasena'
    show="*"                        # Oculta el texto ingresado (por seguridad)
).pack(pady=10, fill=tk.X, padx=50)

# Botón que al hacer clic ejecuta la función de verificación
tk.Button(
    app,
    text="Iniciar Sesión",         # Texto del botón
    font=('Courier', 14),
    bg="#e5f1f6",                   # Color de fondo
    fg='black',                     # Color del texto
    command=verificar_login,       # Función que se ejecuta al hacer clic
    relief='flat'                  # Estilo plano del botón (sin borde resaltado)
).pack(pady=10, fill=tk.X, padx=50)

# Etiqueta que mostrará mensajes al usuario (por ejemplo, éxito o error)
tk.Label(
    app,
    textvariable=mensaje,           # Texto que mostrará la etiqueta
    font=('Courier', 14),
    bg='white',
    fg='black',
    justify='center'
).pack(pady=10, fill=tk.X, padx=50)

# Inicia el bucle principal de la aplicación (permite que la ventana se muestre y funcione)
app.mainloop()
