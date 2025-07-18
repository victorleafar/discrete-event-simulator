# Simulador de Eventos Discretos para Sistemas em Tempo Real

Este projeto é um **simulador de eventos discretos** que implementa algoritmos de escalonamento para sistemas de tarefas em um ou mais processadores. Ele possui uma interface simples para interação com o usuário.

---

## Estrutura do Projeto
├── src
│ ├── main.py # Ponto de entrada do simulador
│ ├── simulator # Contém a lógica principal da simulação
│ │ ├── init.py
│ │ ├── core.py # Lógica central do simulador
│ │ ├── scheduler.py # Implementa os algoritmos de escalonamento
│ │ └── events.py # Define as classes de eventos
│ ├── ui # Módulo de interface com o usuário
│ │ ├── init.py
│ │ └── simple_ui.py # Interface simples do simulador
│ └── tasks # Módulo do sistema de tarefas
│ ├── init.py
│ └── task_system.py # Representa um sistema de tarefas
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto


### Descrição dos Diretórios e Arquivos

- **README.md**  
  Documentação principal do projeto.

- **requirements.txt**  
  Lista de dependências necessárias para rodar o simulador (ex: Flask, numpy, pandas, matplotlib).

- **src/**  
  Diretório principal do código-fonte.

#### 1. `main.py`
Arquivo de entrada do simulador. Responsável por iniciar a interface com o usuário, receber as tarefas e acionar a simulação.

#### 2. `simulator/`
Contém a lógica central da simulação e os algoritmos de escalonamento.

- **core.py**  
  Implementa as classes principais do simulador, incluindo:
  - `Simulator`: Gerencia as tarefas, eventos e executa a simulação.
  - `EventQueue`: Fila de eventos.
  - Eventos como chegada e término de tarefas.

- **events.py**  
  Define as classes de eventos (ex: chegada e término de tarefas) que podem ser usados na simulação.

- **scheduler.py**  
  Implementa o algoritmo de escalonamento, como:
  - Rate Monotonic (RM)  
  Permite simulação.

- **__init__.py**  
  Arquivo para tornar o diretório um pacote Python.

#### 3. `tasks/`
Gerencia a representação das tarefas.

- **task_system.py**  
  Define as classes `Task` e `TaskSystem` para criar, armazenar e manipular tarefas.

- **__init__.py**  
  Arquivo para tornar o diretório um pacote Python.

#### 4. `ui/`
Responsável pela interface simples com o usuário.

- **simple_ui.py**  
  Implementa a interface de texto para entrada de tarefas e comandos do usuário.

- **__init__.py**  
  Arquivo para tornar o diretório um pacote Python.

---

## Como Utilizar

1. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt

2. **Execute o simulador:**
   ```sh
   python src/main.py

3. **Adicione tarefas no formato:**
   ```sh
   nome, chegada, execucao, periodo, deadline
   Tarefa1, 0, 5, 10, 10

4. **Finalize a entrada digitando exit:**
5. **Informe o número de processadores quando solicitado:**
6. **Veja o resultado do escalonamento (exemplo: Rate Monotonic):**
