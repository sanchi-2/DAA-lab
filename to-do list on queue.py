import tkinter as tk
from tkinter import messagebox
# Function to add a task
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)  # Insert task in listbox
        task_entry.delete(0, tk.END)  # Clear the entry field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove the selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]  # Get the index of the selected task
        task_listbox.delete(selected_task_index)  # Delete the task from listbox
    except IndexError:
        messagebox.showinfo("No selection", "Please select a task to remove.")
# Function to mark the selected task as completed
def mark_task_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, f"{task} - Completed")  # Mark as completed
        task_listbox.itemconfig(selected_task_index, {'fg': 'green'})  # Change color to green
    except IndexError:
        messagebox.showinfo("No selection", "Please select a task to mark as completed.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)  # Clear all tasks from listbox
# Set up the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.configure(bg='grey')
# Entry field for adding tasks
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)
task_entry.bind("<Return>", add_task)  # Bind Enter key to add_task function

# Frame for buttons
button_frame = tk.Frame(root, bg='grey')
button_frame.pack(pady=10)

# Button to add a task
add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.grid(row=0, column=0, padx=5)

# Button to remove the selected task
remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

# Button to mark the selected task as completed
complete_button = tk.Button(button_frame, text="Mark as Completed", command=mark_task_completed)
complete_button.grid(row=0, column=2, padx=5)

# Button to clear all tasks
clear_button = tk.Button(button_frame, text="Clear All", command=clear_tasks)
clear_button.grid(row=0, column=3, padx=5)
# Frame for the listbox and scrollbar
listbox_frame = tk.Frame(root)
listbox_frame.pack(pady=10)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
task_listbox = tk.Listbox(listbox_frame, height=10, width=40, selectmode=tk.SINGLE, 
                          yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)
scrollbar.pack(side="right", fill="y")
task_listbox.pack(side="left", fill="both")

# Run the application
root.mainloop()
