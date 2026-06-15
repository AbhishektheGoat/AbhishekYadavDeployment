import streamlit as st

st.set_page_config(
    page_title="Abhishek Yadav",
    page_icon="🚀",
    layout="wide"
)

# Header
st.title("👋 Abhishek Yadav")
st.subheader("Data Science Student | Python Developer | Telegram Bot Developer")

st.write("""
📍 Mumbai, India

📧 yadavabhishek1421@gmail.com

📱 +91 83695 83952

🔗 GitHub: https://github.com/AbhishektheGoat
""")

st.divider()

# About
st.header("🙋 About Me")

st.write("""
I am a Data Science undergraduate with strong foundations in Python,
Data Analysis, Machine Learning, and Automation.

I enjoy building practical solutions using Python, Streamlit, Telegram Bots,
and Machine Learning techniques. I am passionate about learning new technologies
and applying them to solve real-world problems.
""")

st.divider()

# Skills
st.header("🛠 Skills")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Programming
    - Python
    - SQL (Basic)
    - Git
    - GitHub
    """)

with col2:
    st.markdown("""
    ### Data Science
    - Data Cleaning
    - EDA
    - Statistical Analysis
    - Machine Learning
    """)

with col3:
    st.markdown("""
    ### Libraries & Tools
    - Pandas
    - NumPy
    - Matplotlib
    - Scikit-Learn
    - Streamlit
    - Excel
    """)

st.divider()

# Projects
st.header("📂 Projects")

st.subheader("📊 Student Performance Analysis")

st.write("""
• Performed Exploratory Data Analysis using Pandas

• Identified relationships between study habits, attendance, and academic performance

• Created visual insights using charts and statistical methods
""")

st.subheader("🏠 House Price Prediction")

st.write("""
• Built a regression model using Scikit-learn

• Applied data preprocessing and feature engineering

• Evaluated model performance using RMSE and R² metrics
""")

st.divider()

# Education
st.header("🎓 Education")

st.markdown("""
### BSc Data Science

**Semester 1 CGPA:** 9.18

**Semester 2 CGPA:** 9.45

**Semester 3 CGPA:** 8.82

**Semester 4:** Pursuing
""")

st.divider()

# Services
st.header("💼 Services")

st.markdown("""
### Software Development
- Python Applications
- Custom Automation Scripts
- Telegram Bot Development
- Streamlit Web Applications

### Data Science Services
- Data Analysis
- Data Cleaning
- Visualization Dashboards
- Machine Learning Projects

### Hosting & Deployment
- Streamlit Deployment
- GitHub Integration
- Basic Website Hosting Assistance
- Project Deployment Support
""")

st.divider()

# Availability
st.header("🚀 Open For")

st.success("""
✔ Data Science Internships

✔ Python Development Projects

✔ Freelance Software Development

✔ Telegram Bot Development

✔ Streamlit Application Development

✔ Hosting & Deployment Services

✔ Entry-Level Software Opportunities
""")

st.divider()

# Contact
st.header("📞 Contact")

st.write("""
📧 Email: yadavabhishek1421@gmail.com

📱 Mobile: +91 83695 83952

💻 GitHub: https://github.com/AbhishektheGoat
""")

st.divider()


