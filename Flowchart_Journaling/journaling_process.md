# Journaling Process Flowchart

## Key
```mermaid
graph LR
    A[Tools]:::tools
    B[Intermediate Result]:::output
    C[Knowledge Document]:::processing
    
    classDef tools fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
```

## Process Flow
```mermaid
graph TD
    Start[Create empty markdown file]:::tools
    Whisper[Open SuperWhisper and talk]:::tools
    Vomit[Get vomit version of journal]:::output
    Commit[Git commit to check in]:::tools
    Cleanup[Run cleanup process]:::processing
    People[people.md]:::processing
    V1[Version 1 of document]:::output
    
    Start --> Whisper
    Whisper --> Vomit
    Vomit --> Commit
    Commit --> Cleanup
    People --> Cleanup
    Cleanup --> V1
    
    classDef tools fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
```
