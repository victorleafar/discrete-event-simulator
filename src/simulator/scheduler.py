class Scheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def rate_monotonic(self, simulation_time=20, num_processors=1):
        """
        Escalonamento Rate Monotonic para tarefas periódicas.
        Cada tarefa deve ser um dicionário com: 'nome', 'chegada', 'execucao', 'periodo', 'deadline'
        """
        import copy
        timeline = []
        active_tasks = []
        tasks = copy.deepcopy(self.tasks)
        for t in tasks:
            t['next_release'] = t['chegada']
            t['remaining_time'] = 0

        for time in range(simulation_time):
            # Libera novas instâncias das tarefas
            for t in tasks:
                if time == t['next_release']:
                    t['remaining_time'] = t['execucao']
                    t['release_time'] = time
                    t['next_release'] += t['periodo']
                    active_tasks.append(t.copy())

            # Remove tarefas concluídas ou que perderam deadline
            for t in active_tasks[:]:
                if t['remaining_time'] <= 0 or (time - t['release_time'] >= t['deadline']):
                    active_tasks.remove(t)

            # Ordena por período (prioridade RM)
            active_tasks.sort(key=lambda x: x['periodo'])
            running = []
            for i in range(min(num_processors, len(active_tasks))):
                active_tasks[i]['remaining_time'] -= 1
                running.append(active_tasks[i]['nome'])

            timeline.append((time, running if running else ['Idle']))

        return timeline