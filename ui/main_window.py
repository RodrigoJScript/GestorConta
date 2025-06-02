import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Gestor de Credenciales')
        self.geometry('1200x800')
        self.configure(bg='white')

        # Input fields
        self.web_label = tk.Label(self, text='Web', anchor='w', bg='white')
        self.web_label.pack(fill='x', padx=100, pady=(40, 0))
        self.web_entry = tk.Entry(self, font=('Arial', 16), bg='#dddddd')
        self.web_entry.pack(fill='x', padx=100, pady=(0, 20), ipady=15)

        self.user_label = tk.Label(self, text='Usuario', anchor='w', bg='white')
        self.user_label.pack(fill='x', padx=100)
        self.user_entry = tk.Entry(self, font=('Arial', 16), bg='#dddddd')
        self.user_entry.pack(fill='x', padx=100, pady=(0, 20), ipady=15)

        self.pass_label = tk.Label(self, text='Password', anchor='w', bg='white')
        self.pass_label.pack(fill='x', padx=100)
        self.pass_entry = tk.Entry(self, font=('Arial', 16), bg='#dddddd', show='*')
        self.pass_entry.pack(fill='x', padx=100, pady=(0, 30), ipady=15)

        self.add_btn = tk.Button(self, text='Agregar nueva credencial', font=('Arial', 14), bg='#a0a0a0', fg='black', height=2)
        self.add_btn.pack(pady=(0, 30), ipadx=100)

        # Credentials table
        self.table_frame = tk.Frame(self, bg='white')
        self.table_frame.pack(fill='both', expand=True, padx=60, pady=10)

        columns = ('web', 'actions')
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show='headings', height=5)
        self.tree.heading('web', text='Web')
        self.tree.heading('actions', text='Acciones')
        self.tree.column('web', width=400)
        self.tree.column('actions', width=400)
        self.tree.pack(side='left', fill='x', expand=True)

        # Placeholder data
        for i in range(1, 6):
            self.tree.insert('', 'end', values=(f'Web {i}', ''))

        # Action buttons for each row
        self.action_buttons = []
        for i, item in enumerate(self.tree.get_children()):
            btn_frame = tk.Frame(self.table_frame, bg='white')
            view_btn = tk.Button(btn_frame, text='Ver', width=8, bg='#888888', fg='white')
            edit_btn = tk.Button(btn_frame, text='Editar', width=8, bg='#888888', fg='white')
            del_btn = tk.Button(btn_frame, text='Eliminar', width=8, bg='#888888', fg='white')
            view_btn.pack(side='left', padx=2)
            edit_btn.pack(side='left', padx=2)
            del_btn.pack(side='left', padx=2)
            #self.tree.window_create(item, column='actions', window=btn_frame)
            self.action_buttons.append((view_btn, edit_btn, del_btn))

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()
