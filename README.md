# MCQ Generator with LangChain and OpenAI

A Streamlit web app that generates multiple-choice questions (MCQs) from a PDF or text file using LangChain and OpenAI's GPT-3.5. Upload a document, choose the number of questions, subject, and difficulty, and the app returns a quiz table with the correct answers plus an AI review of how suitable the quiz is for students.

---

## Features

- Upload a **PDF or TXT** file as the source material
- Choose the **number of MCQs** (3 to 50), the **subject**, and the **complexity level**
- Quiz generated in a fixed **JSON format** and shown as a table (question, choices, correct answer)
- A second AI step **reviews the quiz** for complexity and suggests changes if it doesn't suit the students
- Shows token usage and API cost in the console for each request
- Logs every run to a timestamped file in the `logs/` folder

---

## How It Works

```
Uploaded file (PDF/TXT)
        │
        ▼
  read_file()  ──►  plain text
        │
        ▼
  Quiz chain (LLMChain)  ──►  MCQs in JSON  (prompt + Response.json template)
        │
        ▼
  Review chain (LLMChain) ──►  complexity analysis (max 50 words)
        │
        ▼
  SequentialChain output  ──►  get_table_data()  ──►  Streamlit table + review box
```

Two LangChain `LLMChain`s run one after the other inside a `SequentialChain`. The first writes the quiz, and the second reviews it as an English-language expert.

---

## Tech Stack

| Purpose | Technology |
|---------|------------|
| Language | Python |
| LLM framework | LangChain |
| Model | OpenAI GPT-3.5-Turbo (temperature 0.3) |
| UI | Streamlit |
| File reading | PyPDF2 |
| Data handling | pandas |
| Config | python-dotenv |

---

## Project Structure

```
mcqgen/
├── src/
│   └── mcqgenrator/
│       ├── __init__.py
│       ├── MCQGenrator.py      # LLM, prompts, and the sequential chain
│       ├── utils.py            # read_file() and get_table_data()
│       └── logger.py           # logging setup
├── StreamlitApp.py             # Streamlit user interface
├── Response.json               # JSON format template given to the model
├── experiments.ipynb           # Notebook used to build and test the chain
├── .env.example                # Template for your API key
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Create a virtual environment

```bash
python -m venv env
source env/bin/activate        # Windows: env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Copy `.env.example` to `.env` in the project root and add your key:

```env
OPENAI_API_KEY=your_api_key_here
```

Never commit this file. It is listed in `.gitignore`.

### 5. Run the app

```bash
streamlit run StreamlitApp.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`).

---

## Usage

1. Upload a PDF or TXT file.
2. Enter the number of MCQs, the subject, and the complexity level (for example, "Simple" or "Medium").
3. Click **Create MCQs**.
4. Read the generated quiz table and the review below it.

---

## Example Output

| MCQ | Choices | Correct |
|-----|---------|---------|
| Question text | a-> option \|\| b-> option \|\| c-> option \|\| d-> option | b |

---

## Limitations

- Question quality depends on the quality and length of the uploaded text. Very long documents may exceed the model's context limit.
- Scanned PDFs (images) are not supported, because the app extracts text only.
- The model sometimes returns invalid JSON, in which case the app shows an error and you need to try again.
- This project uses an older LangChain API, so install the version listed in `requirements.txt` if you see import errors.

---

## Future Improvements

- Download the quiz as PDF, CSV, or Excel
- Show answer explanations
- Support more file types (DOCX) and larger documents by splitting text into chunks
- Let users choose the model and the number of options per question
- Add a quiz-taking mode with scoring

---

## Author

**Vaibhav**
GitHub: [@Vaibhave52](https://github.com/Vaibhave52/AI_MCQ_GENERATOR)
