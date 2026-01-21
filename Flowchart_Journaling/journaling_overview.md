# Journaling Process Overview

## Three-Phase Process

```mermaid
graph LR
    Start[Create Journal]
    
    subgraph Phase1[Phase 1: Capture]
        Talk[Talk/Vomit]
        Commit1[Commit: Raw]
    end
    
    subgraph Phase2[Phase 2: Refine]
        Cleanup[Cleanup & Review]
        Commit2[Commit: V1]
    end
    
    subgraph Phase3[Phase 3: Analyze]
        Interview[Interview Process]
        Final[Final Analysis]
    end
    
    Start --> Talk
    Talk --> Commit1
    Commit1 --> Cleanup
    Cleanup --> Commit2
    Commit2 --> Interview
    Interview --> Final
    
    classDef phase1 fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef phase2 fill:#ffe0b2,stroke:#e65100,stroke-width:2px
    classDef phase3 fill:#e1f5ff,stroke:#01579b,stroke-width:2px
    
    class Talk,Commit1 phase1
    class Cleanup,Commit2 phase2
    class Interview,Final phase3
```

## Phase Details

- **Phase 1 (Capture)**: Raw brain dump using voice → Initial commit
- **Phase 2 (Refine)**: Clean up text, review for clarity → V1 commit
- **Phase 3 (Analyze)**: AI-driven interview, questions, push back → Final analysis
