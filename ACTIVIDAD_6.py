import tkinter as tk
from tkinter import messagebox
import os


CONTACT_FILE = r"C:\Users\user\Desktop\UNIVERSITY_2025_1\POO\ACTIVITY_6\GITHUB\Contacts.txt"

def create_contact():

    name = name_entry.get().strip()
    number_str = number_entry.get().strip()
    if not name or not number_str:
        messagebox.showwarning("Error de Entrada", "El Nombre y el Número no pueden estar vacíos para crear.")
        return
    try:
        number = int(number_str)
    except ValueError:
        messagebox.showerror("Error de Entrada", "El Número de Contacto debe ser un entero válido.")
        number_entry.delete(0, tk.END) 
        return
    if not os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, 'w') as f:
            pass 

    found = False
    contacts = []
    try:
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('!')
                    if len(parts) == 2:
                        existing_name = parts[0]
                        existing_number = int(parts[1])
                        if existing_name == name or existing_number == number:
                            found = True
                        contacts.append(line)
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"Error al leer el archivo: {e}")
        return
    if found:
        messagebox.showinfo("Contacto Duplicado", f"Ya existe un contacto con el nombre '{name}' o el número '{number}'.")
    else:
        try:
            with open(CONTACT_FILE, 'a') as f:
                f.write(f"{name}!{number}\n")
            messagebox.showinfo("Éxito", f"Contacto '{name}' agregado exitosamente.")
            clear_inputs()
        except Exception as e:
            messagebox.showerror("Error de Archivo", f"Error al escribir en el archivo: {e}")

def search_contact():

    name_to_search = name_entry.get().strip()
    number_to_search_str = number_entry.get().strip()
    if not name_to_search and not number_to_search_str:
        messagebox.showwarning("Error de Entrada", "Por favor, ingresa un Nombre o un Número para buscar.")
        return
    if not os.path.exists(CONTACT_FILE):
        messagebox.showerror("Error de Archivo", "El archivo de contactos no existe. No hay contactos para buscar.")
        return

    found = False
    try:
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('!')
                    if len(parts) == 2:
                        existing_name = parts[0]
                        existing_number = parts[1] 
                        if name_to_search and existing_name == name_to_search:
                            number_entry.delete(0, tk.END)
                            number_entry.insert(0, existing_number)
                            messagebox.showinfo("Éxito", f"Contacto '{name_to_search}' encontrado.")
                            found = True
                            break
                        elif not name_to_search and number_to_search_str and existing_number == number_to_search_str:
                            name_entry.delete(0, tk.END)
                            name_entry.insert(0, existing_name)
                            messagebox.showinfo("Éxito", f"Contacto con número '{number_to_search_str}' encontrado.")
                            found = True
                            break
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"Error al leer el archivo para buscar: {e}")
        return
    if not found:
        messagebox.showinfo("Contacto No Encontrado", "El contacto no existe.")
        if name_to_search:
            number_entry.delete(0, tk.END)
        elif number_to_search_str: 
            name_entry.delete(0, tk.END)
        else: 
            clear_inputs()


def update_contact():

    name_to_update = name_entry.get().strip()
    new_number_str = number_entry.get().strip()

    if not name_to_update or not new_number_str:
        messagebox.showwarning("Error de Entrada", "El Nombre y el Nuevo Número no pueden estar vacíos para actualizar.")
        return
    try:
        new_number = int(new_number_str)
    except ValueError:
        messagebox.showerror("Error de Entrada", "El Nuevo Número de Contacto debe ser un entero válido.")
        number_entry.delete(0, tk.END)
        return
    if not os.path.exists(CONTACT_FILE):
        messagebox.showerror("Error de Archivo", "El archivo de contactos no existe. No hay contactos para actualizar.")
        return

    updated = False
    lines = []
    try:
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('!')
                    if len(parts) == 2:
                        existing_name = parts[0]
                        if existing_name == name_to_update:
                            lines.append(f"{name_to_update}!{new_number}")
                            updated = True
                        else:
                            lines.append(line)
                    else:
                        lines.append(line) 
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"Error al leer el archivo para actualizar: {e}")
        return
    if updated:
        try:
            with open(CONTACT_FILE, 'w') as f:
                for line in lines:
                    f.write(line + "\n")
            messagebox.showinfo("Éxito", f"Contacto '{name_to_update}' actualizado exitosamente.")
            clear_inputs()
        except Exception as e:
            messagebox.showerror("Error de Archivo", f"Error al escribir el archivo actualizado: {e}")
    else:
        messagebox.showinfo("Contacto No Encontrado", f"No se encontró el contacto con el nombre '{name_to_update}'.")

def delete_contact():

    name_to_delete = name_entry.get().strip()

    if not name_to_delete:
        messagebox.showwarning("Error de Entrada", "El Nombre no puede estar vacío para la operación de eliminación.")
        return
    if not os.path.exists(CONTACT_FILE):
        messagebox.showerror("Error de Archivo", "El archivo de contactos no existe. No hay contactos para eliminar.")
        return

    deleted = False
    lines = []
    try:
        with open(CONTACT_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split('!')
                    if len(parts) == 2:
                        existing_name = parts[0]
                        if existing_name == name_to_delete:
                            deleted = True
                        else:
                            lines.append(line)
                    else:
                        lines.append(line)
    except Exception as e:
        messagebox.showerror("Error de Archivo", f"Error al leer el archivo para eliminar: {e}")
        return
    if deleted:
        try:
            with open(CONTACT_FILE, 'w') as f:
                for line in lines:
                    f.write(line + "\n")
            messagebox.showinfo("Éxito", f"Contacto '{name_to_delete}' eliminado exitosamente.")
            clear_inputs()
        except Exception as e:
            messagebox.showerror("Error de Archivo", f"Error al escribir el archivo después de eliminar: {e}")
    else:
        messagebox.showinfo("Contacto No Encontrado", f"No se encontró el contacto con el nombre '{name_to_delete}'.")

def clear_inputs():
    name_entry.delete(0, tk.END)
    number_entry.delete(0, tk.END)

# ventana
app = tk.Tk()
app.title("CONTACTS")
app.geometry("500x250")
app.resizable(False, False)

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=0) 
app.rowconfigure(1, weight=0) 

input_frame = tk.Frame(app, padx=10, pady=10, bd=2, relief="groove")
input_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
input_frame.columnconfigure(1, weight=1)

tk.Label(input_frame, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(input_frame, width=40)
name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

tk.Label(input_frame, text="Número:").grid(row=1, column=0, sticky="w", pady=5)
number_entry = tk.Entry(input_frame, width=40)
number_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

button_frame = tk.Frame(app, padx=10, pady=10)
button_frame.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
for i in range(4):
    button_frame.columnconfigure(i, weight=1)

create_btn = tk.Button(button_frame, text="Create", command=create_contact, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
create_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

search_btn = tk.Button(button_frame, text="Read", command=search_contact, bg="#00BCD4", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
search_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

update_btn = tk.Button(button_frame, text="Update", command=update_contact, bg="#6E1CDA", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
update_btn.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

delete_btn = tk.Button(button_frame, text="Delete", command=delete_contact, bg="#F44336", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
delete_btn.grid(row=0, column=3, padx=5, pady=5, sticky="ew")

clear_btn = tk.Button(button_frame, text="Clear", command=clear_inputs, bg="#7995A3", fg="white", font=("Arial", 10, "bold"), relief="raised", bd=3)
clear_btn.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")

app.mainloop()