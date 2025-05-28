from datetime import datetime


class Task:
    def __init__(self, name, assigned_to, deadline, dependencies=None):
        self.name = name
        self.assigned_to = assigned_to
        self.deadline = deadline
        self.status = "NOT_STARTED"
        self.dependencies = dependencies if dependencies else []
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []
    def add_task(self, task):
        self.tasks.append(task)
    def report(self):
        print(f"Report for project: {self.name}")
        for task in self.tasks:
            print(f"{task.name} [{task.status}] (Assigned to: {task.assigned_to}, Deadline: {task.deadline})")


p = Project("Website Redesign")
t1 = Task("Design mockup", "Lwam", "2025-06-01")
t2 = Task("Frontend dev", "Kisanet", "2025-06-10", dependencies=["Design mockup"])
p.add_task(t1)
p.add_task(t2)
p.report()