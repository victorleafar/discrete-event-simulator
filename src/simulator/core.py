class Event:
    def __init__(self, time):
        self.time = time

    def execute(self):
        raise NotImplementedError("This method should be overridden by subclasses")


class TaskArrival(Event):
    def __init__(self, time, task):
        super().__init__(time)
        self.task = task

    def execute(self):
        print(f"Task {self.task} arrived at time {self.time}")


class TaskCompletion(Event):
    def __init__(self, time, task):
        super().__init__(time)
        self.task = task

    def execute(self):
        print(f"Task {self.task} completed at time {self.time}")


class EventQueue:
    def __init__(self):
        self.events = []

    def add_event(self, event):
        self.events.append(event)
        self.events.sort(key=lambda e: e.time)

    def get_next_event(self):
        return self.events.pop(0) if self.events else None


class Simulator:
    def __init__(self):
        self.event_queue = EventQueue()
        self.tasks = []

    def add_task(self, task_str):
        # Espera input: nome, chegada, execucao, periodo, deadline
        try:
            nome, chegada, execucao, periodo, deadline = [x.strip() for x in task_str.split(',')]
            task = {
                "nome": nome,
                "chegada": int(chegada),
                "execucao": int(execucao),
                "periodo": int(periodo),
                "deadline": int(deadline)
            }
            self.tasks.append(task)
            print(f"Tarefa adicionada: {task}")
        except Exception as e:
            print("Formato inválido. Use: nome, chegada, execucao, periodo, deadline")

    def schedule_event(self, event):
        self.event_queue.add_event(event)

    def run(self):
        print("Simulação iniciada com as tarefas:")
        for task in self.tasks:
            print(task)
        from simulator.scheduler import Scheduler  # Add this import or adjust the path as needed
        scheduler = Scheduler()
        for task in self.tasks:
            scheduler.add_task(task)
        timeline = scheduler.rate_monotonic(simulation_time=20, num_processors=1)
        print("\nEscalonamento Rate Monotonic:")
        for time, running in timeline:
            print(f"Tempo {time}: Executando {', '.join(running)}")