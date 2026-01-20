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
    Start[Create journal.md]:::tools
    Whisper[SuperWhisper]:::tools
    Talk[Talk]:::manual
    Vomit[Vomit version]:::output
    Commit[git commit]:::tools
    Cleanup[Cleanup]:::processing
    People[people.md]:::processing
    V1[V1]:::output
    Say[say -f journal_2025_10_1.md]:::tools
    Review[Review]:::manual
    Commit2[git commit]:::tools
    Analyze[analyze]:::processing
    
    subgraph Interview
        Read[Read today's journal +<br/>previous journals +<br/>previous analysis]:::processing
        Ask[Ask questions]:::manual
        PushBack[Push back]:::manual
        CreateAnalysis[journal.analysis.md]:::processing
        
        Read --> Ask
        Ask --> PushBack
        PushBack --> CreateAnalysis
    end
    
    SayAnalysis[say -f journal.analysis.md]:::tools
    ReviewAnalysis[Final review]:::manual
    
    Start --> Whisper
    Whisper --> Talk
    Talk --> Vomit
    Vomit --> Commit
    Commit --> Cleanup
    People --> Cleanup
    Cleanup --> V1
    V1 --> Review
    Say --> Review
    Review --> Commit2
    Commit2 --> Analyze
    Analyze --> Read
    CreateAnalysis --> ReviewAnalysis
    SayAnalysis --> ReviewAnalysis
    
    classDef tools fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    classDef output fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef processing fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    classDef manual fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px
```
