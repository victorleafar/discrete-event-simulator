class Event:
    def __init__(self, event_time):
        self.event_time = event_time

    def execute(self):
        raise NotImplementedError("Este método debe ser anulado por las subclases.")


class TaskArrival(Event):
    def __init__(self, event_time, task):
        super().__init__(event_time)
        self.task = task

    def execute(self):
        # Logic for handling task arrival
        print(f"Task {self.task} arrived at time {self.event_time}")


class TaskCompletion(Event):
    def __init__(self, event_time, task):
        super().__init__(event_time)
        self.task = task

    def execute(self):
        # Logic for handling task completion
        print(f"Task {self.task} completed at time {self.event_time}")