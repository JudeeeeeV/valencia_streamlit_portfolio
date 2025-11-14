import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Jude Mikael Valencia | Portfolio", layout="wide")


def load_css(file_name: str) -> str:

    css_path = Path(file_name)
    if not css_path.exists():
        return ""
    return css_path.read_text(encoding="utf-8")


css = load_css("style.css")
if css:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


st.title("Jude Mikael Valencia")
st.subheader("3rd Year BS Computer Science Student")
st.divider()

col_left, col_right = st.columns([2, 1], gap="large")

with col_left:
    st.markdown(
        """
        <div class="card intro-card">
            <h3>Hi, I’m Jude Mikael Valencia</h3>
            <p>
                I am a 3rd year BS Computer Science student passionate about building
                clean, maintainable software and delightful user experiences. I enjoy
                full-stack development, web apps, and exploring modern frontend tooling.
            </p>
            <p>
                I like working on student-focused products, educational tools, and
                small teams where I can learn fast and ship frequently.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_right:
    st.markdown(
        """
        <div class="card contact-card">
            <h4>Contact</h4>
            <ul class="contact-list">
                <li>🔗 <a href="https://www.linkedin.com/in/jude-mikael-valencia-a79b4a2a2/" target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
                <li>🐙 <a href="https://github.com/JudeeeeeV" target="_blank" rel="noopener noreferrer">GitHub</a></li>
                <li>✉️ <a href="mailto:valencia.judemikaell@gmail.com">Email</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br />", unsafe_allow_html=True)


st.subheader("Education")
st.markdown(
    """
    <div class="card">
        <h4>BS in Computer Science</h4>
        <p><strong>Cebu Institute of Technology - University</strong></p>
        <p>Expected Graduation: <em>School Year 2025–2026</em></p>
        <p>Duration: <em>2022–2026</em></p>
    </div>

    <div class="card">
        <h4>Senior High School</h4>
        <p><strong>University of Cebu – Pardo</strong></p>
        <p>Duration: <em>2020–2022</em></p>
    </div>

    <div class="card">
        <h4>Junior High School</h4>
        <p><strong>Abellana National School</strong></p>
        <p>Duration: <em>2016–2020</em></p>
    </div>

    <div class="card">
        <h4>Elementary</h4>
        <p><strong>Guadalupe Elementary School</strong></p>
        <p>Duration: <em>2010–2016</em></p>
    </div>
    """,
    unsafe_allow_html=True,
)


st.markdown("<br />", unsafe_allow_html=True)


st.subheader("Skills")
col_a, col_b, col_c = st.columns(3, gap="large")

with col_a:
    st.markdown(
        """
        <div class="card">
            <h4>Languages</h4>
            <ul class="skill-list">
                <li>Python</li>
                <li>Java</li>
                <li>JavaScript / TypeScript</li>
                <li>SQL</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_b:
    st.markdown(
        """
        <div class="card">
            <h4>Frameworks & Tools</h4>
            <ul class="skill-list">
                <li>React</li>
                <li>Streamlit</li>
                <li>Node.js</li>
                <li>Git / GitHub</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_c:
    st.markdown(
        """
        <div class="card">
            <h4>Concepts</h4>
            <ul class="skill-list">
                <li>Algorithms & Data Structures</li>
                <li>OOP & Design Patterns</li>
                <li>Databases & REST APIs</li>
                <li>Software Testing</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br />", unsafe_allow_html=True)


st.subheader("Projects")
proj_col_left, proj_col_right = st.columns(2, gap="large")

with proj_col_left:
    st.markdown(
        """
            <div class="project-card-content">
                <h4>Student Marketplace App</h4>
                <p class="muted">A marketplace for students to buy and sell second-hand items. Built with React and Firebase.</p>
                <div class="tag-row"><span class="tag">React</span><span class="tag">Firebase</span><span class="tag">UX</span></div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
            <div class="project-card-content">
                <h4>Quiz App (React + Streamlit backend)</h4>
                <p class="muted">Interactive online quiz used for classroom practice and assessments.</p>
                <div class="tag-row"><span class="tag">React</span><span class="tag">Python</span><span class="tag">Streamlit</span></div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

with proj_col_right:
    st.markdown(
        """
            <div class="project-card-content">
                <h4>Portfolio Site</h4>
                <p class="muted">A polished personal portfolio showcasing projects and skills.</p>
                <div class="tag-row"><span class="tag">HTML</span><span class="tag">CSS</span><span class="tag">Design</span></div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
            <div class="project-card-content">
                <h4>Notifications App</h4>
                <p class="muted">A notifications manager that groups user notifications and provides quick actions.</p>
                <div class="tag-row"><span class="tag">Vue</span><span class="tag">Tailwind</span><span class="tag">UX</span></div>
            </div>
        </a>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br />", unsafe_allow_html=True)


st.markdown(
    """
    <div class="footer">
        <p>Jude Mikael Valencia</p>
    </div>
    """,
    unsafe_allow_html=True,
)
