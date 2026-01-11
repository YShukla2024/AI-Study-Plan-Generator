import os
from groq import Groq

# -------------------------------
# Configure Groq API
# -------------------------------
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("GROQ_API_KEY not loaded")

client = Groq(api_key=API_KEY)


def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an AI education assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.6,
        max_tokens=400,
    )
    return response.choices[0].message.content


def study_agent(class_level, subjects, weak_subjects, daily_hours, exam_days):
    """
    Agentic AI for Personalized Study Planning
    """

    # -------- Agent reasoning --------
    weak_weight = 0.6
    normal_weight = 0.4

    weak_time = round(daily_hours * weak_weight, 1)
    normal_time = round(daily_hours * normal_weight, 1)

    structured_plan = []

    if weak_subjects:
        for s in weak_subjects:
            structured_plan.append(f"{s}: {weak_time} hours (focus on weak areas)")

    for s in subjects:
        if s not in weak_subjects:
            structured_plan.append(
                f"{s}: {round(normal_time / max(1, len(subjects)), 1)} hours"
            )

    prompt = f"""
Student details:
Class level: {class_level}
Subjects: {subjects}
Weak subjects: {weak_subjects}
Daily study hours: {daily_hours}
Exam in {exam_days} days

Initial plan created by agent:
{structured_plan}

Tasks:
1. Improve the study plan
2. Add a revision strategy
3. Give short motivational advice
4. Keep it concise and practical
"""

    return call_llm(prompt)


if __name__ == "__main__":
    result = study_agent(
        class_level="Class 10",
        subjects=["Maths", "Science", "English"],
        weak_subjects=["Maths"],
        daily_hours=3,
        exam_days=20
    )

    print("\nAI GENERATED STUDY PLAN\n")
    print(result)
