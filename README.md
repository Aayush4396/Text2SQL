***

# Text2SQL

**Text2SQL** is an advanced chatbot for business intelligence that lets users retrieve powerful insights from their data using plain English—**no SQL knowledge required**. Powered by Google’s Gemini Pro LLM and built with Python, LangChain, and Chainlit, this tool enables actionable analytics and democratizes database access for everyone.

***

## Key Features

- **Text-to-SQL Conversion:** Users ask questions in plain English; the chatbot translates queries into SQL and returns actionable business insights.
- **LLM-Powered:** Utilizes Gemini Pro for deep semantic understanding and robust query translation.
- **Modern Stack:** Built with LangChain (for agent/execution orchestration) and Chainlit (for an interactive, ChatGPT-style frontend).
- **Easy Extensibility:** Swap LLM or database connection with minimal changes.
- **Demo Ready:** Includes a sample business sales dataset (25 columns × 3000 rows).

***

## Project Structure

- `main.py`: Orchestrates user interactions and handles backend logic.
- `gemini_utils.py`: Integrates Gemini Pro for LLM-powered query generation and natural language understanding.
- `db_utils.py`: Utility functions for database operations and dynamic SQL execution.
- `data/`: Includes the sample business sales dataset.
- `requirements.txt`: All necessary dependencies for local/dev deployment.
- `chainlit.md`: Setup and Chainlit integration guide.
- `public/`: Static or demo assets (e.g., demo.mp4).

***

## Quick Start

1. **Clone the Repository:**

```bash
git clone https://github.com/Aayush4396/Text2SQL.git
cd Text2SQL
```

2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure API Keys:**
    - Obtain your Google Gemini Pro API Key, Literal API Key, and Chainlit Secret Key.
    - Create a `.env` file in the root directory:

```
GEMINI_API_KEY=your-gemini-key
LITERAL_API_KEY=your-literal-key
CHAINLIT_SECRET=your-chainlit-secret
```

4. **Launch the App:**

```bash
python main.py
```

    - The Chainlit frontend will open in your browser for instant interaction.
5. **Demo:**
    - View the workflow and interface demo video included as `public/Demo.mp4`.

***

## How It Works

1. **User Query:** User types a business question in English.
2. **LLM Translation:** Query is sent to Gemini Pro for parsing and SQL translation.
3. **Execution:** Translated SQL is executed on the business sales dataset.
4. **Insight Delivery:** Results and clear answers are presented conversationally in the UI.

***

## Frameworks \& Technologies

- **Chainlit:** Beautiful, live chat UI for LLM-powered apps.
- **LangChain:** Modular framework for LLM orchestration and agent design.
- **Google Gemini Pro 1.0:** Best-in-class LLM for accurate query understanding.
- **Python:** Backend orchestration and data processing.

***

## Requirements

- Python 3.8+
- Gemini Pro, Literal, and Chainlit API keys

***

## Why Use Text2SQL?

- Empowers non-technical users to leverage data for business growth.
- Streamlines analytics by bridging the gap between natural language and database querying.
- Extensible template—can adapt to any SQL database and any LLM.


***

<span style="display:none">[^1]</span>

[^1]: https://github.com/Aayush4396/Text2SQL
