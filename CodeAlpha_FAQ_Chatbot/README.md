\# 💬 NLP FAQ Chatbot



> \*\*An intelligent, text-based FAQ assistant using Natural Language Processing.\*\*

> Developed as Task 2 for the CodeAlpha Artificial Intelligence Internship.



\## 📖 Overview

This project is an interactive, web-based chatbot built to handle user inquiries regarding the CodeAlpha Internship program rules, perks, and submission guidelines. By combining natural language tokenization and processing with mathematical intent matching, it identifies user queries and replies instantly via an elegant interface.



\## ✨ Features

\* \*\*NLP Preprocessing:\*\* Uses the NLTK library to tokenize input text, normalize casing, and remove irrelevant stop words and punctuation.

\* \*\*Vectorization \& Vector Semantics:\*\* Utilizes a TF-IDF (Term Frequency-Inverse Document Frequency) algorithm to transform sentences into analytical numerical vectors.

\* \*\*Intent Matching:\*\* Measures incoming user text against the database using Cosine Similarity to extract the single best matching answer accurately.

\* \*\*Smart UI Architecture:\*\* Features Streamlit's structural chat containers to model realistic conversations.



\## 🛠️ Technologies Used

\* \*\*Core Language:\*\* Python

\* \*\*Frontend Framework:\*\* Streamlit

\* \*\*Natural Language Processing:\*\* NLTK

\* \*\*Machine Learning Analysis:\*\* Scikit-Learn



\## 🚀 Getting Started



\### Prerequisites

\* \[Python 3.8+](https://www.python.org/downloads/)



\### Installation \& Execution



\*\*1. Clone the repository:\*\*

```bash

git clone \[https://github.com/YOUR\_USERNAME/CodeAlpha\_FAQ\_Chatbot.git](https://github.com/YOUR\_USERNAME/CodeAlpha\_FAQ\_Chatbot.git)

cd CodeAlpha\_FAQ\_Chatbot



2\. Create and activate a virtual environment (Recommended):



Bash

python -m venv venv

\# Windows execution policy activation

.\\venv\\Scripts\\activate

3\. Install the required dependencies:



Bash

pip install -r requirements.txt

4\. Run the application:



Bash

streamlit run app.py

Developed by \[Your Name] for the CodeAlpha AI Internship Program.





\---



\### 🚀 How to Run and Test This Code



1\. Put all 4 files inside your `CodeAlpha\_FAQ\_Chatbot` folder.

2\. Open PowerShell, navigate into the directory, and run your setup commands:

&#x20;  ```bash

&#x20;  python -m venv venv

&#x20;  .\\venv\\Scripts\\activate

&#x20;  pip install -r requirements.txt

&#x20;  python -m streamlit run app.py


