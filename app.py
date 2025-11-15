import streamlit as st
from pathlib import Path
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="Jude Mikael Valencia | Portfolio",
    layout="wide",
    initial_sidebar_state="expanded"
)


def load_css(file_name: str) -> str:
    css_path = Path(file_name)
    if not css_path.exists():
        return ""
    return css_path.read_text(encoding="utf-8")


css = load_css("style.css")
if css:
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        "Go to:",
        ["Home", "About Me", "Education", "Skills", "Projects", "Contact"],
        label_visibility="collapsed"
    )

    st.divider()

    st.markdown("### Academic Progress")
    st.progress(75, text="Degree Completion: 75%")

    st.divider()

    st.metric("Projects Completed", "10+", delta="2 this month")
    st.metric("Years Coding", "4", delta="1")

if page == "Home":
    st.title("Jude Mikael Valencia")
    st.subheader("3rd Year BS Computer Science Student")
    st.divider()

    col_left, col_right = st.columns([2, 1], gap="large")

    with col_left:
        st.markdown(
            """
            <div class="card intro-card">
                <h3>Hi, I'm Jude Mikael Valencia</h3>
                <p>I am a 3rd year BS Computer Science student passionate about building clean, maintainable software and delightful user experiences. I enjoy full-stack development, web apps, and exploring modern frontend tooling.</p>
                <p>I like working on student-focused products, educational tools, and small teams where I can learn fast and ship frequently.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )



    with col_right:
        st.markdown(
            """
            <div class="card contact-card">
                <h3>Contact</h3>
                <ul class="contact-list">
                    <li>🔗 <a href="https://www.linkedin.com/in/jude-mikael-valencia-a79b4a2a2/" target="_blank">LinkedIn</a></li>
                    <li>🐙 <a href="https://github.com/JudeeeeeV" target="_blank">GitHub</a></li>
                    <li>✉️ <a href="mailto:valencia.judemikaell@gmail.com">Email</a></li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.success("🟢 Available for opportunities")

elif page == "About Me":
    st.title("About Me")
    st.divider()

    with st.expander("📖 Read My Story", expanded=True):
        st.markdown("""
        ### My Journey into Computer Science

        Growing up in Cebu City, Philippines, I was always fascinated by technology and how things work. 
        My journey began in elementary school at Guadalupe Elementary School (2010-2016), where I first 
        encountered computers and developed a curiosity for programming.

        During my time at Abellana National School (2016-2020) for junior high, I started learning 
        basic programming concepts and realized that I wanted to pursue Computer Science as a career. 
        This passion only grew stronger during senior high school at the University of Cebu – Pri (2020-2022), 
        where I took my first formal programming courses and built my first web applications.

        Currently, I'm in my 3rd year at Cebu Institute of Technology - University pursuing a BS in Computer Science 
        (2022-2026). These years have been transformative, allowing me to dive deep into full-stack development, 
        software engineering principles, and modern web technologies. I've had the opportunity to work on 
        student-focused projects that solve real problems, which has been incredibly fulfilling.

        ### What Drives Me

        I'm passionate about creating software that makes a difference in people's lives, especially in 
        educational contexts. I believe in writing clean, maintainable code and building user experiences 
        that are intuitive and delightful. My goal is to work with innovative teams where I can continue 
        learning, contribute meaningfully, and grow as a software engineer.

        ### Beyond Coding

        When I'm not coding, I enjoy exploring new technologies, contributing to open-source projects, 
        and helping fellow students with their programming challenges. I'm also interested in UI/UX design 
        and always looking for ways to improve the user experience in the applications I build.
        """)

    st.markdown("---")

    st.markdown("### Interests & Hobbies")
    tab1, tab2, tab3, tab4 = st.tabs(["💻 Tech Interests", "🎯 Goals", "📚 Currently Learning", "🎮 Hobbies"])

    with tab1:
        st.write("""
        - **Full-Stack Web Development**: Building end-to-end web applications
        - **UI/UX Design**: Creating beautiful and intuitive user interfaces
        - **Open Source**: Contributing to community projects
        - **Cloud Technologies**: Exploring AWS, Azure, and modern deployment practices
        """)

    with tab2:
        st.write("""
        - Land a software engineering role at a product-focused company
        - Contribute to major open-source projects
        - Build a portfolio of impactful student-focused applications
        """)

    with tab3:
        st.write("""
        - **TypeScript & Next.js**: For modern React applications
        - **Docker & Kubernetes**: For containerization and orchestration
        - **System Design**: Learning to architect scalable applications
        - **Machine Learning**: Exploring AI/ML with Python
        """)

    with tab4:
        st.write("""
        - Reading tech blogs and documentation
        - Playing strategy games
        - Exploring new coffee shops in Cebu
        - Photography and videography
        """)

elif page == "Education":
    st.title("Education")
    st.divider()

    st.markdown(
        """
        <div class="card">
            <h3>BS in Computer Science</h3>
            <p class="muted">Cebu Institute of Technology - University</p>
            <p class="muted">Expected Graduation: School Year 2025–2026</p>
            <p class="muted">Duration: 2022–2026</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### Academic Performance")
    grades_data = pd.DataFrame({
        'Year': ['1st Year', '2nd Year', '3rd Year (Current)'],
        'GPA': [3.7, 3.8, 3.9],
        'Units Completed': [42, 84, 120]
    })

    col1, col2 = st.columns(2)
    with col1:
        st.bar_chart(grades_data.set_index('Year')['GPA'])
    with col2:
        st.line_chart(grades_data.set_index('Year')['Units Completed'])

    st.markdown("---")

    st.markdown(
        """
        <div class="card">
            <h3>Senior High School</h3>
            <p class="muted">University of Cebu – Pri</p>
            <p class="muted">Duration: 2020–2022</p>
        </div>

        <div class="card">
            <h3>Junior High School</h3>
            <p class="muted">Abellana National School</p>
            <p class="muted">Duration: 2016–2020</p>
        </div>

        <div class="card">
            <h3>Elementary</h3>
            <p class="muted">Guadalupe Elementary School</p>
            <p class="muted">Duration: 2010–2016</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

elif page == "Skills":
    st.title("Skills")
    st.divider()

    st.markdown("### Programming Languages")
    col1, col2 = st.columns(2)

    with col1:
        st.slider("Python", 0, 100, 85, disabled=True)
        st.slider("JavaScript/TypeScript", 0, 100, 80, disabled=True)
        st.slider("Java", 0, 100, 75, disabled=True)

    with col2:
        st.slider("SQL", 0, 100, 70, disabled=True)
        st.slider("HTML/CSS", 0, 100, 90, disabled=True)
        st.slider("C++", 0, 100, 60, disabled=True)

    st.markdown("---")

    col_a, col_b, col_c = st.columns(3, gap="large")

    with col_a:
        st.markdown(
            """
            <div class="card">
                <h3>Frameworks & Libraries</h3>
                <ul class="skill-list">
                    <li>React / Next.js</li>
                    <li>Streamlit</li>
                    <li>Node.js / Express</li>
                    <li>Flask / FastAPI</li>
                    <li>Vue.js</li>
                    <li>Tailwind CSS</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_b:
        st.markdown(
            """
            <div class="card">
                <h3>Tools & Technologies</h3>
                <ul class="skill-list">
                    <li>Git / GitHub</li>
                    <li>VS Code</li>
                    <li>Docker</li>
                    <li>Postman</li>
                    <li>Firebase</li>
                    <li>PostgreSQL / MySQL</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_c:
        st.markdown(
            """
            <div class="card">
                <h3>Concepts</h3>
                <ul class="skill-list">
                    <li>Algorithms & Data Structures</li>
                    <li>OOP & Design Patterns</li>
                    <li>REST APIs</li>
                    <li>Software Testing</li>
                    <li>Responsive Design</li>
                    <li>Agile Development</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.markdown("### Certifications & Achievements")

    cert_col1, cert_col2 = st.columns(2)
    with cert_col1:
        st.checkbox("✅ Responsive Web Design - freeCodeCamp", value=True, disabled=True)
        st.checkbox("✅ JavaScript Algorithms - freeCodeCamp", value=True, disabled=True)


elif page == "Projects":
    st.title("Projects")
    st.divider()

    filter_col1, filter_col2 = st.columns([3, 1])
    with filter_col1:
        search = st.text_input("🔍 Search projects", placeholder="Type to search...")
    with filter_col2:
        tech_filter = st.selectbox("Filter by tech", ["All", "React", "Python", "Vue", "Firebase"])

    proj_col_left, proj_col_right = st.columns(2, gap="large")

    with proj_col_left:
        st.markdown(
            """
            <a href="#" class="card project-card">
                <div class="project-card-content">
                    <h4>Student Marketplace App</h4>
                    <p class="muted">A marketplace for students to buy and sell second-hand items. Built with React and Firebase.</p>
                    <div class="tag-row">
                        <span class="tag">React</span>
                        <span class="tag">Firebase</span>
                        <span class="tag">UX</span>
                    </div>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        if st.button("View Details: Student Marketplace", key="proj1"):
            with st.expander("Project Details", expanded=True):
                st.write("**Features:**")
                st.write("- User authentication and profiles")
                st.write("- Real-time chat between buyers and sellers")
                st.write("- Image upload and gallery")
                st.write("- Search and filter functionality")

        st.markdown(
            """
            <a href="#" class="card project-card">
                <div class="project-card-content">
                    <h4>Quiz App (React + Streamlit backend)</h4>
                    <p class="muted">Interactive online quiz used for classroom practice and assessments.</p>
                    <div class="tag-row">
                        <span class="tag">React</span>
                        <span class="tag">Python</span>
                        <span class="tag">Streamlit</span>
                    </div>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        if st.button("View Details: Quiz App", key="proj2"):
            with st.expander("Project Details", expanded=True):
                st.write("**Features:**")
                st.write("- Multiple question types (MCQ, True/False, Fill-in)")
                st.write("- Timed quizzes with auto-submission")
                st.write("- Score tracking and analytics")
                st.write("- Teacher dashboard for creating quizzes")

    with proj_col_right:
        st.markdown(
            """
            <a href="#" class="card project-card">
                <div class="project-card-content">
                    <h4>Portfolio Site</h4>
                    <p class="muted">A polished personal portfolio showcasing projects and skills.</p>
                    <div class="tag-row">
                        <span class="tag">HTML</span>
                        <span class="tag">CSS</span>
                        <span class="tag">Design</span>
                    </div>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        if st.button("View Details: Portfolio Site", key="proj3"):
            with st.expander("Project Details", expanded=True):
                st.write("**Features:**")
                st.write("- Responsive design")
                st.write("- Smooth animations and transitions")
                st.write("- Project showcase with filtering")
                st.write("- Contact form integration")

        st.markdown(
            """
            <a href="#" class="card project-card">
                <div class="project-card-content">
                    <h4>Notifications App</h4>
                    <p class="muted">A notifications manager that groups user notifications and provides quick actions.</p>
                    <div class="tag-row">
                        <span class="tag">Vue</span>
                        <span class="tag">Tailwind</span>
                        <span class="tag">UX</span>
                    </div>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

        if st.button("View Details: Notifications App", key="proj4"):
            with st.expander("Project Details", expanded=True):
                st.write("**Features:**")
                st.write("- Real-time notification updates")
                st.write("- Categorized notification groups")
                st.write("- Quick action buttons")
                st.write("- Mark as read/unread functionality")


elif page == "Contact":
    st.title("Get in Touch")
    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### Send me a message")

        with st.form("contact_form"):
            name = st.text_input("Your Name *")
            email = st.text_input("Your Email *")
            subject = st.selectbox("Subject *", [
                "General Inquiry",
                "Project Collaboration",
                "Job Opportunity",
                "Freelance Work",
                "Other"
            ])
            message = st.text_area("Message *", height=150)

            submit = st.form_submit_button("Send Message", use_container_width=True)

            if submit:
                if name and email and message:
                    st.success("✅ Message sent successfully! I'll get back to you soon.")
                    st.balloons()
                else:
                    st.error("❌ Please fill in all required fields.")

    with col2:
        st.markdown("### Contact Information")
        st.info("""
        **Email:**  
        valencia.judemikaell@gmail.com

        **Location:**  
        Punta Princesa, Cebu City, Philippines

        **LinkedIn:**  
        https://www.linkedin.com/in/jude-mikael-valencia-a79b4a2a2/

        **GitHub:**  
        https://github.com/JudeeeeeV
        """)

        st.markdown("### Availability")
        availability = st.radio(
            "Current Status:",
            ["Available for work", "Open to opportunities", "Currently busy"],
            index=1,
            disabled=True
        )

        st.markdown("### Response Time")
        st.progress(90, text="Usually responds within 24 hours")

st.markdown("---")
st.markdown(
    f"""
    <div class="footer">
        <p>© {datetime.now().year} Jude Mikael Valencia. Built with Streamlit.</p>
    </div>
    """,
    unsafe_allow_html=True,
)