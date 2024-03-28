import tkinter as tk

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
        self.root = tk.Tk()
        self.root.title("Project Selection")
        self.root.geometry("500x500")
        self.root.configure(bg="#006d77")

        self.label = tk.Label(self.root, text="Project Selection", font=("Book Antiqua", 20), fg="#edf6f9", bg="#006d77")
        self.label.pack(pady=10)

        self.capital_label = tk.Label(self.root, text="Enter the capital budget:", fg="#edf6f9", bg="#006d77")
        self.capital_label.pack(pady=5)
        self.capital_entry = tk.Entry(self.root)
        self.capital_entry.pack(pady=5)

        self.projects_label = tk.Label(self.root, text="Enter the number of projects:", fg="#edf6f9", bg="#006d77")
        self.projects_label.pack(pady=5)
        self.projects_entry = tk.Entry(self.root)
        self.projects_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.get_project_details)
        self.submit_button.pack(pady=10)

        self.root.mainloop()

    def get_project_details(self):
        capital_budget = float(self.capital_entry.get())
        num_projects = int(self.projects_entry.get())

        projects = []

        project_window = tk.Toplevel(self.root)
        project_window.title("Project Details")
        project_window.geometry("500x500")
        project_window.configure(bg="#006d77")

        for i in range(num_projects):
            name_label = tk.Label(project_window, text=f"Name of Project {i + 1}:", fg="#edf6f9", bg="#006d77")
            name_label.pack(pady=5)
            name_entry = tk.Entry(project_window)
            name_entry.pack(pady=5)

            initial_cost_label = tk.Label(project_window, text=f"Initial cost of Project {i + 1}:", fg="#edf6f9", bg="#006d77")
            initial_cost_label.pack(pady=5)
            initial_cost_entry = tk.Entry(project_window)
            initial_cost_entry.pack(pady=5)

            cash_flows_label = tk.Label(project_window, text=f"Enter cash flows for Project {i + 1} (separated by comma):", fg="#edf6f9", bg="#006d77")
            cash_flows_label.pack(pady=5)
            cash_flows_entry = tk.Entry(project_window)
            cash_flows_entry.pack(pady=5)

            projects.append((name_entry, initial_cost_entry, cash_flows_entry))

        submit_button = tk.Button(project_window, text="Submit", command=lambda: self.calculate_schedule(capital_budget, projects))
        submit_button.pack(pady=10)

    def calculate_schedule(self, capital_budget, projects):
        project_objects = []
        for project in projects:
            name = project[0].get()
            initial_cost = float(project[1].get())
            cash_flows = [float(x.strip()) for x in project[2].get().split(",")]
            project_objects.append(Project(name, initial_cost, cash_flows))

        max_cash_flow = [0]
        selected_projects_final = []

        branch_and_bound(capital_budget, project_objects, 0, 0, 0, [], max_cash_flow, selected_projects_final)

        result_window = tk.Toplevel(self.root)
        result_window.title("Results")
        result_window.geometry("500x500")
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
