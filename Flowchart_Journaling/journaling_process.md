# Journaling Process Flowchart

## Key
```mermaid
graph LR
    A[File Operations]:::fileOps
    B[Voice Input]:::voiceInput
    C[Output/Result]:::output
    D[Version Control]:::versionControl
    E[Processing]:::processing
    
    classDef fileOps fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef voiceInput fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef versionControl fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
```

## Process Flow
```mermaid
graph TD
    Start[Create empty markdown file]:::fileOps
    Whisper[Open SuperWhisper and talk]:::voiceInput
    Vomit[Get vomit version of journal]:::output
    Commit[Git commit to check in]:::versionControl
    Cleanup[Run cleanup process<br/>includes people.md]:::processing
    
    Start --> Whisper
    Whisper --> Vomit
    Vomit --> Commit
    Commit --> Cleanup
    
    classDef fileOps fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef voiceInput fill:#fff9c4,stroke:#f57f17,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef versionControl fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
```
