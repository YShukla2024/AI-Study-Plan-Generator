# AI-Study-Plan-Generator

Below is a **complete, end-to-end README.md** you can copy-paste directly into your GitHub repository.
It is written in a **professional, academic + industry style**, suitable for **capstone submission, evaluation, and resume review**.

---

# AI Study Plan Generator (Agentic AI)

## 📌 Project Overview

The **AI Study Plan Generator** is an end-to-end **Agentic AI application** that creates personalized study plans for students based on their academic level, subjects, weak areas, daily study hours, and exam timeline.

The system combines **rule-based decision logic** with **Large Language Model (LLM)** intelligence to deliver structured, practical, and motivational study guidance. The application is deployed as a **live web service** using Streamlit and Render.

🔗 **Live Demo:**
[https://ai-study-plan-generator.onrender.com](https://ai-study-plan-generator.onrender.com)

---

## 🎯 Problem Statement

Students often struggle to plan their studies effectively due to:

* Lack of personalized guidance
* Poor time management
* Inability to prioritize weak subjects
* Generic study schedules that do not adapt to individual needs

This project addresses these challenges by providing an **AI-driven personalized study planner**.

---

## 💡 Solution Approach

The system uses an **Agentic AI architecture**, where:

1. The AI agent first performs **rule-based reasoning** to allocate study time.
2. The agent then invokes an **LLM (LLaMA 3.1 via Groq API)** to refine the plan with:

   * Improved structure
   * Revision strategies
   * Motivational guidance

This separation of **reasoning** and **generation** makes the solution robust, explainable, and scalable.

---

## 🧠 What is Agentic AI in This Project?

This project qualifies as **Agentic AI** because the system:

* Operates autonomously toward a goal (study planning)
* Applies internal decision logic before calling the LLM
* Produces adaptive outputs without manual intervention
* Combines deterministic logic with generative intelligence

---

## 🌍 SDG Alignment

**UN Sustainable Development Goal 4 – Quality Education**

The project promotes:

* Inclusive learning support
* Personalized education
* Better academic planning and outcomes

---

## 🏗️ System Architecture

```
User Input (UI)
      ↓
Rule-Based Agent Logic
      ↓
LLM Enhancement (Groq – LLaMA 3.1)
      ↓
Personalized Study Plan Output
```

---

## 🛠️ Technologies Used

* **Python**
* **Streamlit** (Frontend)
* **Groq API**
* **LLaMA 3.1 – 8B Instant**
* **Render** (Deployment)
* **GitHub** (Version Control)

---

## 📂 Project Structure

```
AI-Study-Plan-Generator/
│── app.py            # Agentic AI backend logic
│── ui.py             # Streamlit frontend
│── requirements.txt  # Project dependencies
│── start.sh          # Render startup script
│── README.md         # Documentation
│── .gitignore
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/AI-Study-Plan-Generator.git
cd AI-Study-Plan-Generator
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Environment Variable

**Windows (PowerShell):**

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

**Linux / macOS:**

```bash
export GROQ_API_KEY="your_api_key_here"
```

### 4️⃣ Run Locally

```bash
streamlit run ui.py
```

---

## ☁️ Deployment (Render)

The application is deployed as a **Python Web Service** on Render.

### Deployment Highlights

* Streamlit launched using a custom startup script
* Secure API key management via environment variables
* GitHub-connected CI/CD deployment

### Render Start Command

```bash
bash start.sh
```

### Environment Variable

| Key          | Description                 |
| ------------ | --------------------------- |
| GROQ_API_KEY | Groq API key for LLM access |

---

## 🔐 Security & Responsible AI

* No API keys stored in source code
* No personal data persistence
* Educational use only
* Transparent rule-based decision logic
* No automated grading or high-stakes decisions

---

## 📊 Sample Output

The system generates:

* Subject-wise time allocation
* Clear revision strategies
* Practical motivation tips
* Human-readable, concise responses

---

## 🎓 Academic & Practical Impact

* Helps students plan studies efficiently
* Reduces exam stress
* Demonstrates real-world Agentic AI usage
* Suitable for educational institutions and learning platforms

---

## 🧪 Future Enhancements

* PDF download of study plan
* User history and progress tracking
* Calendar-based scheduling
* Multi-language support
* Authentication for students

---

## 📌 Resume Description (Optional)

> Built and deployed an Agentic AI-powered personalized study planning system using Python, Streamlit, and LLaMA 3.1 via Groq API, integrating rule-based reasoning with generative AI and deploying the solution on Render.

---

## ✅ Live Application

🔗 **[https://ai-study-plan-generator.onrender.com](https://ai-study-plan-generator.onrender.com)**

---

## 📜 License

This project is developed for educational and academic purposes.

---

### 🎉 Final Note

This project demonstrates a **complete AI lifecycle**:

* Idea → Design → Development → Deployment

