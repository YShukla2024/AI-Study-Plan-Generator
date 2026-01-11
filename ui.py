import streamlit as st
from app import study_agent

# Page configuration
st.set_page_config(
    page_title="AI Study Plan Generator",
    page_icon="📘",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for enhanced UI
st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 0.75rem 1.5rem;
        font-size: 1.1rem;
        font-weight: 600;
        border: none;
        border-radius: 10px;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(102, 126, 234, 0.3);
    }
    .info-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    .stat-box {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        text-align: center;
        margin: 0.5rem;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #667eea;
    }
    .stat-label {
        color: #666;
        font-size: 0.9rem;
        margin-top: 0.5rem;
    }
    .study-plan-output {
        background: #f8f9fa;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #667eea;
        margin-top: 1.5rem;
    }
    .sdg-badge {
        display: inline-block;
        background: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.5rem;
    }
    h1 {
        color: #2c3e50;
        font-weight: 700;
    }
    h3 {
        color: #667eea;
        margin-top: 1.5rem;
    }
    .stMultiSelect {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header with gradient card
st.markdown("""
    <div class="info-card">
        <h1 style="color: white; margin: 0;">📘 AI Personalized Study Plan</h1>
        <p style="font-size: 1.1rem; margin-top: 0.5rem; opacity: 0.95;">
            Smart Learning Powered by Agentic AI
        </p>
        <span class="sdg-badge">🎯 SDG 4 – Quality Education</span>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 👤 Tell us about yourself")

# Two-column layout for basic info
col1, col2 = st.columns(2)

with col1:
    class_level = st.text_input(
        "📚 Class / Education Level",
        "Class 10",
        help="Enter your current education level"
    )

with col2:
    exam_days = st.number_input(
        "📅 Days Until Exam",
        min_value=1,
        max_value=365,
        value=20,
        help="How many days do you have to prepare?"
    )

# Subject selection
st.markdown("### 📖 Subject Selection")

subjects = st.multiselect(
    "Select Your Subjects",
    ["Maths", "Science", "English", "History", "Geography", "Physics", "Chemistry", "Biology", "Computer Science"],
    default=["Maths", "Science", "English"],
    help="Choose all subjects you're studying"
)

if subjects:
    weak_subjects = st.multiselect(
        "🎯 Subjects Needing Extra Focus",
        subjects,
        default=["Maths"] if "Maths" in subjects else [],
        help="Select subjects where you need more help"
    )
else:
    weak_subjects = []

# Study time configuration
st.markdown("### ⏰ Study Schedule")

daily_hours = st.slider(
    "Daily Study Hours Available",
    min_value=1,
    max_value=8,
    value=3,
    help="How many hours can you dedicate to studying each day?"
)

# Show calculated stats
if subjects:
    col1, col2, col3 = st.columns(3)
    
    total_hours = daily_hours * exam_days
    hours_per_subject = total_hours / len(subjects) if subjects else 0
    
    with col1:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{total_hours}</div>
                <div class="stat-label">Total Study Hours</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{len(subjects)}</div>
                <div class="stat-label">Subjects Selected</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="stat-box">
                <div class="stat-number">{hours_per_subject:.1f}</div>
                <div class="stat-label">Hours per Subject</div>
            </div>
        """, unsafe_allow_html=True)

# Generate button
st.markdown("---")

if st.button("🎯 Generate My Personalized Study Plan"):
    if not subjects:
        st.warning("⚠️ Please select at least one subject to continue.")
    else:
        with st.spinner("🤖 AI agent is analyzing your needs and creating your personalized study plan..."):
            output = study_agent(
                class_level=class_level,
                subjects=subjects,
                weak_subjects=weak_subjects,
                daily_hours=daily_hours,
                exam_days=exam_days
            )

        st.success("✅ Your personalized study plan is ready!")
        
        st.markdown("""
            <div class="study-plan-output">
                <h3 style="margin-top: 0;">📋 Your Personalized Study Plan</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(output)
        
        # Download button
        st.download_button(
            label="📥 Download Study Plan",
            data=output,
            file_name=f"study_plan_{class_level.replace(' ', '_')}.txt",
            mime="text/plain"
        )

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; padding: 2rem 0 1rem 0;">
        <p style="color: #666; font-size: 0.9rem;">
            Built with ❤️ using Agentic AI • LLaMA 3.1 via Groq
        </p>
        <p style="color: #999; font-size: 0.85rem; margin-top: 0.5rem;">
            Empowering learners worldwide • Supporting SDG 4 – Quality Education
        </p>
    </div>
""", unsafe_allow_html=True)