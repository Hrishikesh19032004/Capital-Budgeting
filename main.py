import customtkinter as ctk
from tkinter import ttk

class ProjectSelectionGUI:
    def __init__(self, root):
        self.projects = []
        self.root = root
        self.root.title("Project Selection")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.screen_width}x{self.screen_height}+0+0")
        self.root.configure(bg="#000")

        label_font_size = int(self.screen_width * 0.02)
        entry_font_size = int(self.screen_width * 0.015)
        button_font_size = int(self.screen_width * 0.018)

        self.label = ctk.CTkLabel(self.root, text="Project Selection", font=("Book Antiqua", label_font_size))
        self.label.pack(pady=int(self.screen_height * 0.02))

        self.capital_label = ctk.CTkLabel(self.root, text="Enter the capital budget:", font=("Arial", entry_font_size))
        self.capital_label.pack(pady=int(self.screen_height * 0.015))

        self.capital_entry = ttk.Entry(self.root, font=("Arial", entry_font_size))
        self.capital_entry.pack(pady=int(self.screen_height * 0.015))

        self.add_project_section(label_font_size, entry_font_size, button_font_size)

        self.submit_button = ctk.CTkButton(self.root, text="Submit", command=self.calculate_schedule, font=("Arial", button_font_size))
        self.submit_button.pack(pady=int(self.screen_height * 0.02))

    def add_project_section(self, label_font_size, entry_font_size, button_font_size):
        self.name_label = ctk.CTkLabel(self.root, text="Project Name:", font=("Arial", label_font_size))
        self.name_label.pack(pady=int(self.screen_height * 0.015))

        self.name_entry = ttk.Entry(self.root, font=("Arial", entry_font_size))
        self.name_entry.pack(pady=int(self.screen_height * 0.015))

        self.initial_cost_label = ctk.CTkLabel(self.root, text="Initial cost:", font=("Arial", label_font_size))
        self.initial_cost_label.pack(pady=int(self.screen_height * 0.015))

        self.initial_cost_entry = ttk.Entry(self.root, font=("Arial", entry_font_size))
        self.initial_cost_entry.pack(pady=int(self.screen_height * 0.015))

        self.cash_flows_label = ctk.CTkLabel(self.root, text="Cash flows (separated by comma):", font=("Arial", label_font_size))
        self.cash_flows_label.pack(pady=int(self.screen_height * 0.015))

        self.cash_flows_entry = ttk.Entry(self.root, font=("Arial", entry_font_size))
        self.cash_flows_entry.pack(pady=int(self.screen_height * 0.015))

        self.add_button = ctk.CTkButton(self.root, text="Add Project", command=self.save_project, font=("Arial", button_font_size))
        self.add_button.pack(pady=int(self.screen_height * 0.02))

    def save_project(self):
        name = self.name_entry.get()
        initial_cost = float(self.initial_cost_entry.get())
        cash_flows = [float(x.strip()) for x in self.cash_flows_entry.get().split(",")]

        self.projects.append(Project(name, initial_cost, cash_flows))

        # Clear entry fields
        self.name_entry.delete(0, ctk.END)
        self.initial_cost_entry.delete(0, ctk.END)
        self.cash_flows_entry.delete(0, ctk.END)

    def calculate_schedule(self):
        capital_budget = float(self.capital_entry.get())

    
        max_cash_flow = [0]
        selected_projects_final = []

    
        max_cash_flow[0] = sum(self.projects[0].cash_flows)  
        selected_projects_final = self.projects[:]  
        result_window = ctk.CTk()
        result_window.title("Results")
        result_window.geometry("300x300")
        result_window.configure(bg="#000")

        max_cash_label = ctk.CTkLabel(result_window, text=f"Maximum Cash Flow: {max_cash_flow[0]}")
        max_cash_label.pack(pady=5)

        selected_projects_label = ctk.CTkLabel(result_window, text="Selected Projects:")
        selected_projects_label.pack(pady=5)

        for project in selected_projects_final:
            project_label = ctk.CTkLabel(result_window, text=f"- {project.name}")
            project_label.pack(pady=2)

        result_window.mainloop()


class Project:
    def __init__(self, name, initial_cost, cash_flows):
        self.name = name
        self.initial_cost = initial_cost
        self.cash_flows = cash_flows

def start_project_selection(root):
    root.destroy() 
    project_selection_root = ctk.CTk()
    project_selection = ProjectSelectionGUI(project_selection_root)
    project_selection_root.mainloop() 


def main():
    root = ctk.CTk()
    root.title("CapitalCraft")

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    label_width = int(0.09 * screen_width)

    l1 = ctk.CTkLabel(root, text="Capital Craft", width=label_width, text_color="#118ab2")
    l1.pack()
    l2 = ctk.CTkLabel(root, text="Crafting Your Financial Future, One Investment at a Time!", width=label_width, text_color="#000")
    l2.pack()
    b1 = ctk.CTkButton(root, text="Get Started", width=0.09*screen_width, height=0.05*screen_height, corner_radius=50, command=lambda: start_project_selection(root))
    b1.pack()

    l1.configure(font=("Arial", label_width))
    l1.place(x=int(0.25*screen_width), y=int(0.2*screen_height))
    l2.configure(font=("Arial", 20))
    l2.place(x=int(0.3*screen_width), y=int(0.45*screen_height))
    b1.place(x=int(0.43*screen_width), y=int(0.55*screen_height))

    root.mainloop()

if __name__ == "__main__":
    main()
