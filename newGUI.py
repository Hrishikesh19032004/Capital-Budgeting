import tkinter as tk
from tkinter import ttk

class Project:
    def __init__(self, name, initial_cost, cash_flows):
        self.name = name
        self.initial_cost = initial_cost
        self.cash_flows = cash_flows

def branch_and_bound(capital, projects, current_cash_flow, current_cost, idx, selected_projects, max_cash_flow, selected_projects_final):
    if current_cost > capital:
        return

    if idx == len(projects):
        if current_cash_flow > max_cash_flow[0]:
            max_cash_flow[0] = current_cash_flow
            selected_projects_final[:] = selected_projects[:]
        return

    # Branch without selecting the project
    branch_and_bound(capital, projects, current_cash_flow, current_cost, idx + 1, selected_projects, max_cash_flow, selected_projects_final)

    # Branch by selecting the project
    project = projects[idx]
    selected_projects.append(project)
    branch_and_bound(capital, projects, current_cash_flow + sum(project.cash_flows), current_cost + project.initial_cost, idx + 1, selected_projects, max_cash_flow, selected_projects_final)
    selected_projects.pop()

class ProjectSelectionGUI:
    def __init__(self):
        self.projects = []
        self.root = tk.Tk()
        self.root.title("Project Selection")
        self.root.geometry("500x500")
        self.root.configure(bg="#006d77")

        self.label = tk.Label(self.root, text="Project Selection", font=("Book Antiqua", 20), fg="#edf6f9", bg="#006d77")
        self.label.pack(pady=10)

        self.capital_label = tk.Label(self.root, text="Enter the capital budget:", fg="#edf6f9", bg="#006d77")
        self.capital_label.pack(pady=5)
        self.capital_entry = ttk.Entry(self.root)
        self.capital_entry.pack(pady=5)

        self.add_project_section()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.calculate_schedule)
        self.submit_button.pack(pady=10)

        self.root.mainloop()

    def add_project_section(self):
        self.name_label = tk.Label(self.root, text="Name:", fg="#edf6f9", bg="#006d77")
        self.name_label.pack(pady=5)
        self.name_entry = ttk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.initial_cost_label = tk.Label(self.root, text="Initial cost:", fg="#edf6f9", bg="#006d77")
        self.initial_cost_label.pack(pady=5)
        self.initial_cost_entry = ttk.Entry(self.root)
        self.initial_cost_entry.pack(pady=5)

        self.cash_flows_label = tk.Label(self.root, text="Cash flows (separated by comma):", fg="#edf6f9", bg="#006d77")
        self.cash_flows_label.pack(pady=5)
        self.cash_flows_entry = ttk.Entry(self.root)
        self.cash_flows_entry.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Project", command=self.save_project)
        self.add_button.pack(pady=10)

    def save_project(self):
        name = self.name_entry.get()
        initial_cost = float(self.initial_cost_entry.get())
        cash_flows = [float(x.strip()) for x in self.cash_flows_entry.get().split(",")]

        self.projects.append(Project(name, initial_cost, cash_flows))

        # Clear entry fields after adding project
        self.name_entry.delete(0, tk.END)
        self.initial_cost_entry.delete(0, tk.END)
        self.cash_flows_entry.delete(0, tk.END)

    def calculate_schedule(self):
        capital_budget = float(self.capital_entry.get())

        max_cash_flow = [0]
        selected_projects_final = []

        branch_and_bound(capital_budget, self.projects, 0, 0, 0, [], max_cash_flow, selected_projects_final)

        result_window = tk.Toplevel(self.root)
        result_window.title("Results")
        result_window.geometry("300x300")
        result_window.configure(bg="#006d77")

        max_cash_label = tk.Label(result_window, text=f"Maximum Cash Flow: {max_cash_flow[0]}", fg="#edf6f9", bg="#006d77")
        max_cash_label.pack(pady=5)

        selected_projects_label = tk.Label(result_window, text="Selected Projects:", fg="#edf6f9", bg="#006d77")
        selected_projects_label.pack(pady=5)

        for project in selected_projects_final:
            project_label = tk.Label(result_window, text=f"- {project.name}", fg="#edf6f9", bg="#006d77")
            project_label.pack(pady=2)

if __name__ == "__main__":
    ProjectSelectionGUI()
