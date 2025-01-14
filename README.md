# FlashcardApp

## Instructions
- Run "pip install -r requirements.txt" in terminal to install the required packages.
- Run "python scripts/populate_db.py" in terminal to populate the database with data.
- Run "python app.py" in terminal to start the application.

## Project Board

### To Do
- [ ] Create a web scraping module for vocabulary and example sentences.
- [ ] Write unit tests for core functionality.
- [ ] Integrate a library for generating audio (e.g., Google Text-to-Speech).
### In Progress

### Done
- [x] Design the database schema for Flashcards, Decks, and Review.
- [x] Design the Spaced Repetition System (SRS) algorithm.
- [x] Set up the Flask backend.
- [x] Choose a Frontend framework for the user interface.
- [x] Define user stories and personas.
- [x] Plan the architecture and class diagram.
- [x] Research web scraping libraries (e.g., BeautifulSoup, Scrapy).
- [x] Build a Flask route for adding flashcards.

## Requirement

As a user, I want to create new flashcards with a Chinese word, its pinyin, and its English translation so that I can study specific vocabulary.  
As a user, I want to edit existing flashcards so that I can correct or update any mistakes.  
As a user, I want to delete flashcards I no longer need so that I can keep my collection organised.  
As a user, I want to categorise my flashcards into decks (e.g., HSK levels or topics) so that I can focus on specific areas of study.  
As a user, I want to tag flashcards with multiple topics (e.g., "HSK 2" and "Food Vocabulary") so that I can search and filter them easily.  
As a user, I want to automatically generate flashcards from a list of words on a website so that I can quickly expand my vocabulary.  
As a user, I want the system to fetch example sentences from online dictionaries or learning resources so that I can see how words are used in context.  
As a user, I want the system to scrape audio files for pronunciation so that I can hear how words are spoken.  
As a user, I want to review flashcards based on an SRS algorithm so that I can focus on words I struggle with.  
As a user, I want to track my progress for each flashcard so that I know which ones I’ve mastered and which need more practice.  
As a user, I want the system to notify me when it’s time to review flashcards so that I don’t miss my study schedule.  
As a user, I want to mark flashcards as "easy," "medium," or "hard" during review sessions so that the SRS can adapt to my learning speed.  
As a user, I want to attach audio files to flashcards so that I can practice listening and pronunciation.  
As a user, I want to add images to flashcards so that I can associate words with visual representations.  
As a user, I want to play audio during review sessions so that I can listen to the correct pronunciation.  
As a user, I want to import flashcards from an external source (e.g., CSV or Anki) so that I can use existing materials.  
As a user, I want to export my flashcards to a file format like CSV so that I can share them or back them up.  
As a user, I want to see a dashboard showing my overall progress (e.g., mastered cards, cards due for review) so that I can monitor my learning.  
As a user, I want to view my review history (e.g., dates and scores) so that I can understand how I’ve improved over time.  
As a user, I want to customise the review session duration (e.g., 10, 20, or 30 minutes) so that I can fit study time into my schedule.  
As a user, I want to set reminders for study sessions so that I can stay consistent with my learning.  
As a user, I want to adjust the SRS difficulty settings so that the intervals match my learning pace.  
As a user, I want the app to be mobile-friendly so that I can study on the go.  
As a user, I want a dark mode option so that I can use the app comfortably at night.  

## Personas

### **1. Sophie – Sixth Form Student Preparing for University**

- **Age**: 17
- **Location**: Cambridge, UK
- **Highest Education Achieved**: GCSEs
- **Background**:
  - Sophie is in her second year of sixth form, studying Mandarin as part of her A-levels.
  - She plans to apply for university courses that include Mandarin or East Asian Studies.
- **Goals**:
  - Build a solid vocabulary foundation to excel in her A-level exams.
  - Develop pronunciation skills and improve recall of Chinese characters.
- **Pain Points**:
  - Finds it hard to manage her study schedule with multiple subjects.
  - Needs an easy way to review characters and pronunciation on her laptop.

---

### **2. James – University Freshman Taking a Language Elective**

- **Age**: 19
- **Location**: Manchester, UK
- **Highest Education Achieved**: A-levels
- **Background**:
  - James is a first-year engineering student who decided to take a Mandarin language elective to diversify his skills.
  - He has no prior experience with the language but is keen to learn.
- **Goals**:
  - Master basic conversational Mandarin and common vocabulary.
  - Use technology to aid his learning alongside his coursework.
- **Pain Points**:
  - Feels overwhelmed by the complexity of learning characters and tones.
  - Struggles to find resources that cater to absolute beginners.

---

### **3. Emily – Working Professional Enhancing Career Prospects**

- **Age**: 28
- **Location**: London, UK
- **Highest Education Achieved**: Bachelor’s Degree in Marketing
- **Background**:
  - Emily works as a marketing consultant for a global firm and has frequent interactions with Chinese clients.
  - She is self-teaching Mandarin to improve her communication and expand her career opportunities.
- **Goals**:
  - Improve her business vocabulary and understanding of cultural nuances.
  - Practice during her commute and in short bursts during the day.
- **Pain Points**:
  - Limited time for structured study due to a demanding work schedule.
  - Needs a tool that tracks her progress and suggests what to focus on next.

---

### **4. Daniel – Retiree Exploring a New Hobby**

- **Age**: 65
- **Location**: Bath, UK
- **Highest Education Achieved**: Bachelor’s Degree in History
- **Background**:
  - Daniel recently retired and decided to take up Mandarin as a way to keep his mind active and prepare for a planned trip to China.
  - He enjoys learning at his own pace and exploring new cultures.
- **Goals**:
  - Learn enough basic Mandarin to navigate as a tourist in China.
  - Use a simple tool that doesn’t require technical expertise.
- **Pain Points**:
  - Finds technology challenging and prefers a straightforward interface.
  - Wants to avoid feeling pressured by strict schedules or metrics.

---

### **5. Olivia – Sixth Form Language Teacher**

- **Age**: 35
- **Location**: Brighton, UK
- **Highest Education Achieved**: Master’s Degree in Education
- **Background**:
  - Olivia teaches French and Mandarin at a local sixth form college.
  - She often looks for tools to help her students practice independently.
- **Goals**:
  - Recommend a reliable flashcard tool to her students to improve their vocabulary retention.
  - Possibly integrate the tool into her lessons for classroom practice.
- **Pain Points**:
  - Struggles to find software that is affordable and effective for classroom use.
  - Needs a solution that works well on school-provided devices.

## Wireframe

### **1. Home Screen**

- **Header**: "Dashboard"
- **Sections**:
  - **Progress Summary**:
    - "Flashcards Mastered: [Count]"
    - "Reviews Due: [Count]"
  - **Quick Actions**:
    - [Review Now]
    - [Create Flashcard]
    - [Import Flashcards]
- **Navigation Bar**:
  - [Home], [Decks], [Review], [Settings] (Icons for each).

---

### **2. Decks Management Screen**

- **Header**: "My Decks"
- **Deck List**: Each deck is displayed as a card with:
  - Deck Name
  - Flashcard Count
  - [Review Deck] Button
  - [Edit Deck] Icon
  - [Delete Deck] Icon
- **Footer Action Button**: [Create New Deck]

---

### **3. Flashcard Viewer**

- **Header**: "Review Session"
- **Flashcard Display**:
  - Large **Chinese Word** at the top.
  - **Pinyin** and **English Translation** below (flippable card concept).
  - **Audio Icon** for pronunciation.
- **Buttons**:
  - [Easy], [Medium], [Hard] (Spaced Repetition Feedback).
- **Navigation**:
  - "Skip" and "End Review" buttons at the bottom.

---

### **4. Create Flashcard Screen**

- **Header**: "Add New Flashcard"
- **Fields**:
  - **Chinese Word** (Text Input)
  - **Pinyin** (Text Input)
  - **English Translation** (Text Input)
  - **Tags** (Optional Text Input)
  - **Audio Upload** (Optional)
- **Buttons**:
  - [Save]
  - [Cancel]

---

### **5. Web Scraping Screen**

- **Header**: "Import Words"
- **Fields**:
  - URL Input: "Paste URL here"
  - Options: Checkbox for "Include Example Sentences" and "Download Audio."
- **Buttons**:
  - [Scrape and Generate Flashcards]
  - [Cancel]

---

### **6. Progress Tracker Screen**

- **Header**: "Progress Overview"
- **Charts**:
  - Bar chart: Mastery of decks (e.g., % completed).
  - Line chart: Reviews over time.
- **Tables**:
  - List of flashcards with their current mastery levels.
- **Buttons**:
  - [Reset Progress]
  - [Export Data]
