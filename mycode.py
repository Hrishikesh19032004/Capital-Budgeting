import customtkinter

app = customtkinter.CTk()
app.title("CapitalCraft")
customtkinter.set_appearance_mode("dark")

def adjust_window():
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()
    app.geometry(f"{screen_width}x{screen_height}+0+0")

    # Calculate the width of l1 as 40% of the screen width
    label_width = int(0.09* screen_width)

    # Create the label widget with the calculated width
    l1 = customtkinter.CTkLabel(app, text="Capital Craft", width=label_width, text_color="#118ab2")
    l1.pack()
    l2 = customtkinter.CTkLabel(app, text="Crafting Your Financial Future, One Investment at a Time!", width=label_width, text_color="#faf9f9")
    l2.pack()
    b1 = customtkinter.CTkButton(app, text="Get Started", width=0.09*screen_width, height=0.05*screen_height,corner_radius=50)
    b1.pack()

    # Adjust the font size of the label
    l1.configure(font=("Arial", label_width))
    l1.place(x=int(0.25*screen_width), y=int(0.2*screen_height))
    l2.configure(font=("Arial", 20))
    l2.place(x=int(0.3*screen_width), y=int(0.45*screen_height))
    b1.place(x=int(0.43*screen_width), y=int(0.55*screen_height))

# Adjust the window size and create the label widget
adjust_window()

# Run the application
app.mainloop()
