import tkinter as tk
from tkinter import messagebox
import sqlite3



def create_table():
    conn = sqlite3.connect('listOfTasks.db')


    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT)''')
    conn.commit()
    conn.close()


def add_task():
    task = task_entry.get()
    if task:
        conn = sqlite3.connect('listOfTasks.db')
        c = conn.cursor()
        c.execute('INSERT INTO tasks VALUES (?)', (task,))
        conn.commit()
        conn.close()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Warning', 'Please enter a task.')

def remove_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        conn = sqlite3.connect('listOfTasks.db')
        c = conn.cursor()
        task_id = tasks[selected_task_index[0]][0]
        c.execute('DELETE FROM tasks WHERE title = ?', (task_id,))
        conn.commit()
        conn.close()
        update_listbox()
    else:
        messagebox.showwarning('Warning', 'Please select a task to remove.')

def delete_all_tasks():
    confirmed = messagebox.askyesno('Confirm', 'Are you sure you want to delete all tasks?')
    if confirmed:
        conn = sqlite3.connect('listOfTasks.db')
        c = conn.cursor()
        c.execute('DELETE FROM tasks')
        conn.commit()
        conn.close()
        update_listbox()

def update_listbox():
    tasks_listbox.delete(0, tk.END)
    conn = sqlite3.connect('listOfTasks.db')
    c = conn.cursor()
    c.execute('SELECT * FROM tasks')
    global tasks
    tasks = c.fetchall()
    for task in tasks:
        tasks_listbox.insert(tk.END, task)
    conn.close()

# GUI setup
root = tk.Tk()
root.title('To-Do List')

create_table()

task_label = tk.Label(root, text='Enter Task:')
task_label.pack(pady=5)

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=5)

add_button = tk.Button(root, text='Add Task', command=add_task)
add_button.pack(pady=5)

remove_button = tk.Button(root, text='Remove Task', command=remove_task)
remove_button.pack(pady=5)

delete_all_button = tk.Button(root, text='Delete All Tasks', command=delete_all_tasks)
delete_all_button.pack(pady=5)

tasks_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)
tasks_listbox.pack(pady=10)

update_listbox()

root.mainloop()
