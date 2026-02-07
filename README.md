# AI Assessment: Agent-Based, UI-Driven

This project is a small educational app built with Python and Streamlit. It uses two simple AI-style agents to generate and review learning content for a given grade and topic.

---

## What the project does

- **Generator Agent**
  - Implemented in `generator_agent.py`.
  - Takes structured input: `{ grade, topic }`.
  - Returns structured output:
    ```json
    {
      "explanation": "...",
      "mcqs": [
        {
          "question": "...",
          "options": ["A", "B", "C", "D"],
          "answer": "B"
        }
      ]
    }
    ```
  - For example, for the topic **"Types of angles"** (Grade 4), it generates:
    - A short, age‑appropriate explanation.
    - A set of MCQs with fixed options and correct answers.

- **Reviewer Agent**
  - Implemented in `reviewer_agent.py`.
  - Takes the Generator’s JSON output + the grade.
  - Returns:
    ```json
    {
      "status": "pass" | "fail",
      "feedback": ["..."]
    }
    ```
  - Applies simple rules, such as:
    - Checking sentence length for age appropriateness.
    - Making sure key concepts like “angle”, “right angle”, “acute angle”, and “obtuse angle” are mentioned.
    - Ensuring each MCQ has exactly 4 options and that the answer is one of them.

- **Pipeline**
  - Implemented in `pipeline.py`.
  - Provides a `run_pipeline(grade, topic)` function that:
    1. Calls the Generator Agent once.
    2. Sends the result to the Reviewer Agent.
    3. If the reviewer returns `fail`, calls the Generator Agent again with the feedback to produce a **refined** output.
    4. Limits this to **one** refinement pass.

- **Streamlit UI**
  - Implemented in `app.py`.
  - Shows:
    - An **Input** section (grade and topic).
    - A **Run Agent Pipeline** button that triggers `run_pipeline`.
    - A **Generator Output** section (explanation + MCQs).
    - A **Reviewer Feedback** section (PASS/FAIL and feedback messages).
    - A **Refined Output (if any)** section that displays refined explanation and MCQs when the first attempt fails.
  - For Grade 4, the first explanation is intentionally a bit long so the Reviewer flags it as too complex. The refined explanation then uses shorter, simpler sentences, showing the refinement logic working.

---

## How to run

1. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
2. Install dependencies:
   ```bash
   pip install streamlit
3. Start the app:
   ```bash
   streamlit run app.py
   

