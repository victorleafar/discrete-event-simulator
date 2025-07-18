class SimpleUI:
    def __init__(self):
        self.tasks = []

    def display_menu(self):
        print("Discrete Event Simulator")
        print("1. Add Task")
        print("2. Run Simulation")
        print("3. Exit")

    def display_welcome_message(self):
        print("Bem-vindo ao Simulador de Eventos Discretos para Sistemas em Tempo Real!")
        print("Digite as tarefas ou 'exit' para sair.")

    def display_goodbye_message(self):
        print("Obrigado por usar o simulador. Até logo!")

    def get_user_input(self):
        return input("Digite uma tarefa (ou 'exit'): ")

    def add_task(self):
        task_name = input("Enter task name: ")
        arrival_time = int(input("Enter arrival time: "))
        duration = int(input("Enter duration: "))
        self.tasks.append((task_name, arrival_time, duration))
        print(f"Task '{task_name}' added.")

    def run_simulation(self):
        if not self.tasks:
            print("No tasks to simulate.")
            return
        # Here you would call the simulation logic
        print("Running simulation with the following tasks:")
        for task in self.tasks:
            print(f"Task Name: {task[0]}, Arrival Time: {task[1]}, Duration: {task[2]}")

    def start(self):
        self.display_welcome_message()
        while True:
            self.display_menu()
            choice = self.get_user_input()
            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.run_simulation()
            elif choice == '3':
                print("Exiting the simulator.")
                self.display_goodbye_message()
                break
            else:
                print("Invalid choice. Please try again.")