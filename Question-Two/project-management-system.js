
class Task {
	constructor(name, assignedTo, deadline, dependencies = []) {
	  this.name = name;
this.assignedTo = assignedTo;
this.deadline = deadline;
this.status = "NOT_STARTED";
this.dependencies = dependencies;
}
}

class Project {
constructor(name) {
this.name = name;
this.tasks = [];
}

addTask(task) {
this.tasks.push(task);
}

report() {
console.log(`Report for project: ${this.name}`);
this.tasks.forEach(task => {
  console.log(`- ${task.name} [${task.status}] (Assigned to: ${task.assignedTo}, Deadline: ${task.deadline})`);
});
}
}


const p = new Project("Mama Mboga case study");
const task1 = new Task("Research", "Lwam", "2025-07-06");
const task2 = new Task("Literature review", "Hewan", "2025-07-01", ["Research"]);
p.addTask(task1);
p.addTask(task2);
p.report();
