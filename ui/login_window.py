import tkinter as tk

class LoginWindow(tk.Tk):
    def __init__(self, master_password_set=False):
        super().__init__()
        self.title('Gestor de Credenciales - Login')
        self.geometry('900x600')
        self.configure(bg='white')
        self.master_password_set = master_password_set
        self._draw_ui()

    def _draw_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
        if not self.master_password_set:
            self._draw_set_password()
        else:
            self._draw_login()

    def _draw_set_password(self):
        tk.Label(self, text='Genera tu nueva contrasena maestra', bg='white', font=('Arial', 14)).pack(pady=(180, 20))
        entry_frame = tk.Frame(self, bg='white')
        entry_frame.pack(pady=10)
        tk.Entry(entry_frame, font=('Arial', 14), bg='#dddddd', width=50).pack(ipady=10)
        tk.Label(self, text='Placeholder sobre agregar la nueva contrasena maestra', bg='#dddddd', font=('Arial', 12), anchor='w', width=50).pack(pady=(10, 30))
        tk.Button(self, text='Agregar', font=('Arial', 14), bg='#666666', fg='white', width=20, height=2).pack()

    def _draw_login(self):
        tk.Label(self, text='Inicia sesion', bg='white', font=('Arial', 14)).pack(pady=(180, 20))
        entry_frame = tk.Frame(self, bg='white')
        entry_frame.pack(pady=10)
        tk.Entry(entry_frame, font=('Arial', 14), bg='#dddddd', width=50, show='*').pack(ipady=10)
        tk.Label(self, text='Placeholder ingresar contrasena para iniciar sesion', bg='#dddddd', font=('Arial', 12), anchor='w', width=50).pack(pady=(10, 30))
        tk.Button(self, text='Iniciar sesion', font=('Arial', 14), bg='#666666', fg='white', width=20, height=2).pack()

if __name__ == '__main__':
    # Change master_password_set to True to show login screen
    app = LoginWindow(master_password_set=False)
    app.mainloop()
