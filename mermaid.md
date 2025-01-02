```mermaid
classDiagram
    class Flashcard {
        +int id
        +str front
        +str back
        +str pinyin
        +str audio_path
        +str tags
        +get_display_text() str
    }

    class Deck {
        +int id
        +str name
        +List~Flashcard~ flashcards
        +add_flashcard(flashcard: Flashcard)
        +remove_flashcard(flashcard_id: int)
        +get_flashcards() List~Flashcard~
    }

    class User {
        +int id
        +str username
        +str email
        +str password
        +List~Deck~ decks
        +register(username: str, email: str, password: str)
        +login(email: str, password: str)
        +get_decks() List~Deck~
    }

    class SpacedRepetition {
        +dict review_schedule
        +schedule_review(flashcard: Flashcard, performance: str)
        +get_next_review_date(flashcard: Flashcard) datetime
    }

    class WebScraper {
        +scrape_flashcards(url: str) List~Flashcard~
        +scrape_audio(word: str) str
    }

    class ProgressTracker {
        +dict flashcard_progress
        +update_progress(flashcard_id: int, score: int)
        +get_progress(flashcard_id: int) int
    }

    User "1" --> "*" Deck
    Deck "1" --> "*" Flashcard
    Flashcard "1" --> "0..1" SpacedRepetition
    Flashcard "1" --> "0..1" ProgressTracker
    WebScraper ..> Flashcard : generates
    SpacedRepetition --> Flashcard : schedules
    ProgressTracker --> Flashcard : tracks
