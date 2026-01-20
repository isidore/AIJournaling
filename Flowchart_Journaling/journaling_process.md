# Journaling Process Flowchart

## Key
```mermaid
graph LR
    A[Tools]:::tools
    B[Intermediate Result]:::output
    C[Knowledge Document]:::processing
    D[Manual Process]:::manual
    
    classDef tools fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    classDef manual fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
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
    Say[say -f journal_2025_10_1.md]:::tools
    Review[Review document]:::manual
    Commit2[Git commit]:::tools
    Analyze[analyze]:::processing
    
    Start --> Whisper
    Whisper --> Vomit
    Vomit --> Commit
    Commit --> Cleanup
    People --> Cleanup
    Cleanup --> V1
    V1 --> Review
    Say --> Review
    Review --> Commit2
    Commit2 --> Analyze
    
    classDef tools fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    classDef manual fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
```
