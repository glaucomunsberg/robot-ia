
The abstract processor worflow is the **brain** in the robot-ia.

It's [structured](structure.md) by [cortex](cortex.md) and substructures like [reptilian](reptilian.md), [limbic](limbic.md) and [neocortex](neocortex.md) to execute actions, decisions and manage the robot's [behavior](behavior.md). Each executation in brain use the [protocols](../protocols/index.md) to communicate, translate commands and return responses.

```mermaid
flowchart

    subgraph brain[Robot Brain]
        cortex[Cortext]

        subgraph modules[substructures]
            neocortex[Neocortex]
            limic[Limbic]
            reptilian[Reptilian]
        end
    end

    subgraph body[Robot Body]
        sensors[Sensores]
    end

    neocortex --  commands  --> cortex
    limic --  commands --> cortex
    reptilian --  commands --> cortex

    cortex -- command --> sensors
    sensors -- response --> cortex
```

## Brain Workflow Runner

The brain execute the intentions in cortex translating the commands to the sensors and actuators. Bellow an exemple to read ultrassonic sensor and move the robot forward.

```mermaid
flowchart TB
    CORTEX([Cortext]) --> INTENTIONS[["`Intentions List`"]]
    INTENTIONS -- run idea **go to forward** --> IDEA[idea]
    IDEA --> CMD1{{command 1}}
    IDEA --> CMD2{{command 2}}
    IDEA --> CMD3{{command 3}}
    IDEA --> CMD4{{command 4}}
    CMD2 --> C_RULES1[/rule 1\]
    CMD2 --> C_RULES2[/rule 2\]
    CMD3 --> C_RULES3[/rule 1\]
```