import tkinter as tk
root = tk.Tk()
root.title("Tk Example")
root.configure(background="lightgray")
root.minsize(200, 200)
root.maxsize(1920, 1080)
root.geometry("300x300+50+50")
def create_windows():
    k=1
    for j in range(50):
        k += 1
        for i in range(90):
            new_window = tk.Toplevel()
            new_window.title(f"Window {i+k}")
            new_window.geometry(f"10x10+{i*20}+{k*20}")  # Offset each window

root = tk.Tk()
root.title("Main Window")
tk.Button(root, text="Open 2500 Windows", command=create_windows).pack(pady=20)
root.mainloop()