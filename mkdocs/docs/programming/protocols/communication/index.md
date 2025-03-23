
# Communication

## Description

Communication is the process of exchanging information between two or more entities. It is a fundamental concept in programming, as it is the basis for all interactions between Server through the [Intention](../intention/index.md) and a Robot Cortex through the [Brain](../../brain/index.md).


```mermaid
flowchart LR
    subgraph server API
        A[Request]
    end
    subgraph Microprocessor
        B[Executation]
    end
    
    A-- **COMMUNICATION PROTOCOL** --> B
    B-- **COMMUNICATION PROTOCOL** --> A

```

## Diagram

Below is a sequence diagram that shows the communication between the server intention and the actions of the robot cortex.

```mermaid
sequenceDiagram
  actor server as Request HTTP

  participant main as Main.py
  participant reader as Comunication:Reader
  participant decoder as Brain:Neocortex:Decoder
  participant cortex as Brain:Cortex

  server ->>+ main: request(idea:text/json)

  loop asyncioThreads
    par asyncioTaks
        loop task_listener()
            main ->>reader:reader()
            opt new_request
                reader ->>+ decoder: decode_from_text(idea:text)
                decoder ->> decoder: decode(idea:list)
                decoder ->> cortex: add_task(func, type)
            end
        end
    and
        loop cortex_runner()
            main ->> cortex:run()
            alt task list not empty
                cortex ->> cortex:pop_from_list
            end
        end
    end
  end
  main ->> server: response(response:text)

```