class Task:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = None
        self.completion_time = None

class TaskSystem:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, arrival_time, burst_time):
        task = Task(name, arrival_time, burst_time)
        self.tasks.append(task)

    def get_tasks(self):
        return self.tasks

    def get_task_info(self):
        return [(task.name, task.arrival_time, task.burst_time, task.completion_time) for task in self.tasks]