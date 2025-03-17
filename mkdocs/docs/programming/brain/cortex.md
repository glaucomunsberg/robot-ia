## Cortex

The `Cortex` is the brain of the system, responsible for managing all system activities, from reading sensors, controlling actuators, image processing, executing commands, to communicating with other systems.


## States

The `Cortex` is responsible for managing the system's state, prioritizing tasks, and executing them according to the system's state. The system has four states:

- **Alert**: The system is in alert mode, waiting for a critical activity to occur.
- **Action**: The system is in action mode, executing tasks.
- **Rest**: The system is in rest mode, waiting for activities to occur.
- **Dormant**: The system is in dormant mode, waiting for the battery to be charged or the system to be restarted.

```mermaid
stateDiagram
  direction TB
  [*] --> Rest
  Rest --> [*]
  Rest --> Dormant
  Rest --> Action
  Rest --> Alert
  Action --> Rest
  Action --> Alert
  Action --> Dormant
  Dormant --> Rest
  Dormant --> Action
  Dormant --> Alert
  Alert --> Action

```

### Alert

- **Enter** when any critical activity is inserted in cortex task queue
- **During** suspend all sensor readings (TODO)
- **Exit** when all critical activities are executed

### Action
- **Enter** when the system receives a command to execute an action and any critical activity is in the cortex task queue
- **During** execute all tasks in the cortex task queue
- **Exit** when all tasks in the cortex task queue are executed

### Rest

- **Enter** without activities for x seconds
- **During** does not read certain sensors
- **Exit** with the addition of some activity

### Dormant 

- **Enter** General Dane or battery at critical level
- **During** does not read certain sensors (TODO)
- **Exit** system restarted or battery not at critical level

## Transition

Each state has a set of rules that define when the system `enters`, `during`, and `exits` the state.

### Enter

The system enters the state when a specific activity occurs.

### During

The system remains in the state/rules while a specific activity occurs.

### Exit

The system exits the state when a specific activity occurs.


```mermaid
sequenceDiagram
    participant Enter
    participant During
    participant Exit

    Enter->>During: Any action like 'critical'
    loop actions
        During->>During: Suspende no critical tasks
        During->>During: Remove moviment tasks form enqueu 
        During->>During: Execute next critical task
    end
    During->>Exit: None 'critical' activity is enqueued
```
    
## Task Enqueue

Todas as trefas são enviadas para serem processada com a classificação:

- <small style='background-color: rgb(198,21,32);color: white; border-radius: 6px; padding: 1px 6px;'>**CRITICAL**</small>: Execução imediatamente na fila. Cenário: Cancelar todos os comandos de movimento pq foi detectada uma barreira a 10cm.
- <small style='background-color: rgb(246,130,32);color: white; border-radius: 6px; padding: 1px 6px;'>**HIGH PRIORITY**</small>: Execução com prioridade alta se não houver atividades críticas. Cenário: Leitura do sensor de distância enquanto o carro está em movimento.
- <small style='background-color: rgb(243,199,4);color: white; border-radius: 6px; padding: 1px 6px;'>NORMAL</small>: Execução em prioridade normal, caso não haja atividades de alta prioridade. Cenário: realizar o movimento do carro, leitura de outros sensores ou execução de demostrativo na tela.
- <small style='background-color: rgb(0,126,64);color: white; border-radius: 6px; padding: 1px 6px;'>LOW</small>: atividades de baixa prioridade, caso não haja nenhuma atividade: Cenário: leitura de sensores secundários como de tempoeratura, sincronização de de dados e etc.
- <small style='background-color: rgb(5,172,237);color: white; border-radius: 6px; padding: 1px 6px;'>EVENTUALY</small>: Atividades que não exigem priorização e poderão não ser executadas. Cenário: sincronização do relógio interno.


Below is a sequence diagram that shows how the tasks are enqueued and processed by the `Cortex`.

```mermaid
sequenceDiagram
  participant AddTask as AddTask
  participant RunTask as RunTask

  autonumber
  rect rgba(243,199,4,0.7)
    AddTask ->> RunTask: add 'NORMAL' task
  end
  rect rgba(0,126,64,0.7)
    AddTask ->> RunTask: add 'LOW' level
  end
  rect rgba(246,130,32,0.7)
    AddTask ->> RunTask: add 'HIGH_PRIORITY' level
  end
  rect rgba(198,21,32,0.7)
    AddTask ->> RunTask: add 'CRITICAL' level
  end
  rect rgba(5,172,237,0.7)
    AddTask ->> RunTask: add 'EVENTUALY' level
  end
  loop CortexRunner
    RunTask ->> RunTask: Order by priority<br>Get the next task<br>Run the task command
    RunTask --) AddTask: Eventualy enqueue a secundary event
  end
```
## Worflow

The system has a workflow that defines how the system behaves in each state. The workflow is defined by a state diagram that shows the system's behavior in each state.

```mermaid
stateDiagram
  direction TB
  state RestChoise <<choice>>
  state s1 <<join>>
  state s5 <<choice>>
  state s9 <<choice>>
  state s11 <<choice>>
  state s15 <<join>>
  state s16 <<join>>
  Alert --> s1
  s1 --> RestChoise
  [*] --> RestChoise:system start
  s2 --> s1
  s3 --> s1
  RestChoise --> s5:Tasks list is not empty
  s5 --> s6
  s9 --> Alert:A <b>CRITICAL</b> task in list
  s6 --> s9
  s11 --> [*]:is shutdown command
  s9 --> s11:no <b>CRITICAL</b> task in list
  s11 --> s15:os not shutdown command
  s15 --> s3:motor actions
  s16 --> s2:last tast is in x secounds
  RestChoise --> s16:Task list is empty
  s16 --> s7:last task in x secounds and not moviment
  s7 --> s1
  s2:Rest
  s3:Action
  s6:tasks
s6:get_next_list
  s7:Dorment
```