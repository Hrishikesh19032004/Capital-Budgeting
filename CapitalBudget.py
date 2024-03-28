class Project:
    def __init__(self, name, initial_cost, cash_flows):
        self.name = name
        self.initial_cost = initial_cost
        self.cash_flows = cash_flows

def branch_and_bound(capital, projects, current_cash_flow, current_cost, idx, selected_projects):
    global max_cash_flow
    global selected_projects_final

    if current_cost > capital:
        return

    if idx == len(projects):
        if current_cash_flow > max_cash_flow:
            max_cash_flow = current_cash_flow
            selected_projects_final = selected_projects[:]
        return

    # Branch without selecting the project
    branch_and_bound(capital, projects, current_cash_flow, current_cost, idx + 1, selected_projects)

    # Branch by selecting the project
    project = projects[idx]
    selected_projects.append(project)
    branch_and_bound(capital, projects, current_cash_flow + sum(project.cash_flows), current_cost + project.initial_cost, idx + 1, selected_projects)
    selected_projects.pop()


if __name__ == "__main__":
    # Input from the user
    capital_budget = float(input("Enter the capital budget: "))
    num_projects = int(input("Enter the number of projects: "))

    projects = []

    # Input project details
    for i in range(num_projects):
        name = input(f"Enter the name of Project {i + 1}: ")
        initial_cost = float(input(f"Enter the initial cost of {name}: "))
        num_cash_flows = int(input(f"Enter the number of cash flows for {name}: "))
        cash_flows = []
        for j in range(num_cash_flows):
            cash_flow = float(input(f"Enter cash flow {j + 1} for {name}: "))
            cash_flows.append(cash_flow)
        projects.append(Project(name, initial_cost, cash_flows))

    max_cash_flow = 0
    selected_projects_final = []

    branch_and_bound(capital_budget, projects, 0, 0, 0, [])

    print("Maximum Cash Flow:", max_cash_flow)
    print("Selected Projects:")
    for project in selected_projects_final:
        print(f"- {project.name}")
