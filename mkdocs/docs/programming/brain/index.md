The brain is **[STRUCTURED](structure.md)** by **[CORTEX](cortex.md)** that run all **[INTENTIONS](../protocols/intention/index.md)** with your **[COMMANDS](../protocols/intention/command.md)**. All data to send/used in each idea use the **[PROTOCOL](../protocols/index.md)**. 

The workflow of the idea running in the robot Cortex is represented in the flowchart below.

```mermaid
flowchart TB
    CORTEX[Cortext] --> IDEAS[["`Ideias`"]]
    IDEAS -- run idea **go to forward** --> IDEA[walk forward]
    IDEA --> CMD1[read ultrassonic]
    IDEA --> CMD2[forward the weels]
    IDEA --> CMD3[fa:fa-car stop weels]
    CMD2 --> C_RULES2{rules}
    C_RULES2 --> CR1_2[ultrassonic > 5 cm]
    CMD3 --> C_RULES3{rules}
    C_RULES3 --> CR1_3[ultrassonic < 5 cm]
```