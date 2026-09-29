
import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
import difflib


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# PROFESSIONAL UI
# =========================================================

st.markdown("""
<style>

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(99, 102, 241, 0.12),
            transparent 25%
        ),
        radial-gradient(
            circle at 95% 10%,
            rgba(14, 165, 233, 0.12),
            transparent 28%
        ),
        radial-gradient(
            circle at 50% 100%,
            rgba(139, 92, 246, 0.08),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #f8fbff,
            #eef5ff,
            #faf8ff
        );

    color: #172033;
}


.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}


h1, h2, h3 {
    color: #172033 !important;
}

h1 {
    font-weight: 850 !important;
    letter-spacing: -1px;
}

h2 {
    font-weight: 750 !important;
}

h3 {
    font-weight: 700 !important;
}


p, label {
    color: #475569;
}


/* =========================================================
   HERO
========================================================= */

.hero {
    background:
        linear-gradient(
            135deg,
            rgba(79, 70, 229, 0.97),
            rgba(37, 99, 235, 0.94),
            rgba(6, 182, 212, 0.90)
        );

    border-radius: 26px;
    padding: 38px;
    margin-bottom: 28px;
    color: white;

    box-shadow:
        0 18px 45px rgba(37, 99, 235, 0.20);
}

.hero h1 {
    color: white !important;
    font-size: 38px;
    margin-bottom: 8px;
}

.hero p {
    color: rgba(255,255,255,0.88);
    font-size: 16px;
}


/* =========================================================
   FEATURE CARDS
========================================================= */

.feature-card {
    background: rgba(255,255,255,0.82);

    border: 1px solid #e2e8f0;

    border-radius: 18px;

    padding: 20px;

    min-height: 130px;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.05);

    transition: 0.2s ease;
}

.feature-card:hover {
    transform: translateY(-3px);

    box-shadow:
        0 14px 32px rgba(15,23,42,0.09);
}

.feature-icon {
    font-size: 30px;
    margin-bottom: 8px;
}

.feature-title {
    font-size: 17px;
    font-weight: 750;
    color: #172033;
}

.feature-text {
    font-size: 13px;
    color: #64748b;
    margin-top: 5px;
}


/* =========================================================
   SECTION CARD
========================================================= */

.section-card {
    background: rgba(255,255,255,0.82);

    border: 1px solid #e2e8f0;

    border-radius: 20px;

    padding: 24px;

    margin: 16px 0;

    box-shadow:
        0 8px 28px rgba(15,23,42,0.045);
}


/* =========================================================
   INPUT FIELDS
========================================================= */

div[data-baseweb="input"],
div[data-baseweb="textarea"] {

    background: white !important;

    border: 1px solid #dbe3f0 !important;

    border-radius: 12px !important;
}


div[data-baseweb="input"]:focus-within,
div[data-baseweb="textarea"]:focus-within {

    border-color: #6366f1 !important;

    box-shadow:
        0 0 0 3px rgba(99,102,241,0.10);
}


input,
textarea {
    color: #172033 !important;
}


/* =========================================================
   FILE UPLOADER
========================================================= */

section[data-testid="stFileUploader"] {

    background: rgba(255,255,255,0.88);

    border: 1px dashed #a5b4fc;

    border-radius: 16px;

    padding: 14px;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.05);
}


/* =========================================================
   BUTTON
========================================================= */

.stButton > button {

    width: 100%;

    min-height: 52px;

    border: none;

    border-radius: 13px;

    color: white;

    font-size: 16px;

    font-weight: 750;

    background:
        linear-gradient(
            90deg,
            #4f46e5,
            #2563eb
        );

    box-shadow:
        0 10px 25px rgba(79,70,229,0.22);

    transition: 0.25s ease;
}


.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 15px 32px rgba(79,70,229,0.30);
}


/* =========================================================
   METRIC
========================================================= */

div[data-testid="stMetric"] {

    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 18px;

    padding: 20px;

    box-shadow:
        0 10px 28px rgba(15,23,42,0.06);
}


div[data-testid="stMetricLabel"] {
    color: #64748b !important;
}


div[data-testid="stMetricValue"] {
    color: #4f46e5 !important;
    font-weight: 850 !important;
}


/* =========================================================
   SKILL CARDS
========================================================= */

.skill-card {

    background: white;

    border: 1px solid #e2e8f0;

    border-radius: 14px;

    padding: 14px 18px;

    margin: 8px 0;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.04);
}


/* =========================================================
   ROADMAP CARD
========================================================= */

.roadmap-card {

    background:
        linear-gradient(
            135deg,
            white,
            #f5f7ff
        );

    border-left: 4px solid #6366f1;

    border-radius: 15px;

    padding: 18px;

    margin: 12px 0;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.05);
}


/* =========================================================
   INFO CARD
========================================================= */

.info-card {

    background:
        linear-gradient(
            135deg,
            #eef2ff,
            #ecfeff
        );

    border: 1px solid #c7d2fe;

    border-radius: 18px;

    padding: 20px;

    margin: 15px 0;
}


/* =========================================================
   FOOTER
========================================================= */

.footer {
    text-align: center;

    color: #64748b;

    font-size: 13px;

    padding: 25px 10px;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

    .hero {
        padding: 25px;
    }

    .hero h1 {
        font-size: 28px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <h1>🎯 AI Skill Gap Analyzer</h1>

    <p>
        AI-powered Career & Skill Analysis for Students
    </p>

    <p>
        Discover your current skills, identify missing skills,
        and get a personalized learning roadmap for your future career.
    </p>

</div>
""", unsafe_allow_html=True)


# =========================================================
# FEATURE CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📄</div>
        <div class="feature-title">Resume Analysis</div>
        <div class="feature-text">
            Detect skills from your resume.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <div class="feature-title">Skill Matching</div>
        <div class="feature-text">
            Compare your skills with career requirements.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">📊</div>
        <div class="feature-title">Gap Detection</div>
        <div class="feature-text">
            Identify skills you need to improve.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-icon">🗺️</div>
        <div class="feature-title">Learning Roadmap</div>
        <div class="feature-text">
            Get a step-by-step learning plan.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.write("")


# =========================================================
# LOAD JOB DATABASE
# =========================================================

try:

    jobs_df = pd.read_csv("jobs.csv")

except Exception:

    jobs_df = pd.DataFrame(
        columns=["job", "skills"]
    )


job_skills = {}


for _, row in jobs_df.iterrows():

    job_name = str(
        row.get("job", "")
    ).strip().lower()

    skills_text = str(
        row.get("skills", "")
    )

    skills_list = [

        skill.strip().lower()

        for skill in skills_text.split(",")

        if skill.strip()

    ]

    if job_name:

        job_skills[job_name] = skills_list


# =========================================================
# GENERAL CAREER SKILL DATABASE
# =========================================================

career_skill_templates = {

    # =====================================================
    # TECHNOLOGY / IT
    # =====================================================

    "python developer": [
        "python", "sql", "git", "django",
        "rest api", "html", "css"
    ],

    "software engineer": [
        "programming", "python", "java",
        "data structures", "algorithms",
        "git", "sql", "problem solving"
    ],

    "software developer": [
        "programming", "python", "java",
        "sql", "git", "data structures",
        "problem solving"
    ],

    "web developer": [
        "html", "css", "javascript",
        "react", "git", "rest api"
    ],

    "frontend developer": [
        "html", "css", "javascript",
        "react", "git"
    ],

    "backend developer": [
        "python", "sql", "git",
        "rest api", "fastapi", "django"
    ],

    "full stack developer": [
        "html", "css", "javascript",
        "react", "python", "sql",
        "git", "rest api"
    ],

    "data scientist": [
        "python", "sql", "pandas",
        "numpy", "statistics",
        "machine learning",
        "scikit-learn"
    ],

    "data analyst": [
        "excel", "sql", "python",
        "pandas", "statistics",
        "power bi", "tableau"
    ],

    "ai engineer": [
        "python", "machine learning",
        "deep learning", "tensorflow",
        "pytorch", "llms",
        "generative ai"
    ],

    "machine learning engineer": [
        "python", "machine learning",
        "scikit-learn", "deep learning",
        "tensorflow", "pytorch", "mlops"
    ],

    "data engineer": [
        "python", "sql", "spark",
        "linux", "docker", "aws"
    ],

    "cloud engineer": [
        "linux", "docker", "kubernetes",
        "aws", "azure", "git"
    ],

    "devops engineer": [
        "linux", "docker", "kubernetes",
        "git", "ci/cd", "aws"
    ],

    "cyber security analyst": [
        "networking", "linux",
        "cyber security", "ethical hacking",
        "cryptography", "risk assessment"
    ],


    # =====================================================
    # MEDICAL / HEALTHCARE
    # =====================================================

    "doctor": [
        "biology", "anatomy", "physiology",
        "clinical skills", "diagnosis",
        "patient care", "communication",
        "medical ethics", "decision making"
    ],

    "medical doctor": [
        "biology", "anatomy", "physiology",
        "clinical skills", "diagnosis",
        "patient care", "medical ethics",
        "communication"
    ],

    "mbbs doctor": [
        "biology", "anatomy", "physiology",
        "pharmacology", "pathology",
        "diagnosis", "patient care",
        "medical ethics"
    ],

    "nurse": [
        "anatomy", "physiology",
        "patient care", "first aid",
        "clinical skills", "communication",
        "medical ethics", "emergency care"
    ],

    "pharmacist": [
        "pharmacology", "chemistry",
        "biology", "drug knowledge",
        "patient counseling",
        "medical ethics", "communication"
    ],

    "dentist": [
        "biology", "anatomy",
        "oral health", "dental procedures",
        "patient care", "clinical skills",
        "communication"
    ],

    "physiotherapist": [
        "anatomy", "physiology",
        "exercise therapy", "rehabilitation",
        "patient assessment",
        "communication", "patient care"
    ],

    "lab technician": [
        "biology", "chemistry",
        "laboratory techniques",
        "sample collection",
        "microscopy", "safety procedures",
        "record keeping"
    ],


    # =====================================================
    # ENGINEERING
    # =====================================================

    "engineer": [
        "mathematics", "physics",
        "problem solving", "technical skills",
        "design", "communication",
        "project management"
    ],

    "civil engineer": [
        "engineering mathematics",
        "structural engineering",
        "construction", "autocad",
        "surveying", "project management",
        "site management"
    ],

    "mechanical engineer": [
        "engineering mathematics",
        "mechanics", "thermodynamics",
        "cad", "manufacturing",
        "machine design", "problem solving"
    ],

    "electrical engineer": [
        "mathematics", "electrical circuits",
        "electronics", "power systems",
        "control systems", "autocad",
        "problem solving"
    ],

    "electronics engineer": [
        "electronics", "digital electronics",
        "analog electronics",
        "microcontrollers",
        "embedded systems",
        "c programming", "circuit design"
    ],

    "chemical engineer": [
        "chemistry", "mathematics",
        "thermodynamics", "chemical processes",
        "process control", "laboratory skills",
        "safety"
    ],

    "aerospace engineer": [
        "physics", "mathematics",
        "aerodynamics", "flight mechanics",
        "aircraft design", "engineering software",
        "problem solving"
    ],


    # =====================================================
    # POLICE / DEFENCE / GOVERNMENT
    # =====================================================

    "police officer": [
        "physical fitness", "discipline",
        "communication", "law knowledge",
        "investigation", "decision making",
        "situational awareness", "leadership"
    ],

    "police": [
        "physical fitness", "discipline",
        "law knowledge", "investigation",
        "communication", "leadership",
        "decision making"
    ],

    "ips officer": [
        "law knowledge", "leadership",
        "public administration",
        "decision making", "communication",
        "current affairs", "discipline",
        "physical fitness"
    ],

    "ias officer": [
        "public administration",
        "current affairs", "communication",
        "leadership", "decision making",
        "policy knowledge", "problem solving"
    ],

    "government officer": [
        "general knowledge",
        "current affairs", "communication",
        "computer skills", "problem solving",
        "decision making", "administrative skills"
    ],

    "army officer": [
        "physical fitness", "discipline",
        "leadership", "teamwork",
        "strategic thinking",
        "decision making",
        "mental resilience"
    ],

    "navy officer": [
        "physical fitness", "discipline",
        "leadership", "navigation",
        "teamwork", "technical skills",
        "decision making"
    ],

    "air force officer": [
        "physical fitness", "discipline",
        "aviation knowledge", "leadership",
        "decision making", "technical skills",
        "situational awareness"
    ],

    "defence officer": [
        "physical fitness", "discipline",
        "leadership", "teamwork",
        "strategic thinking", "decision making"
    ],


    # =====================================================
    # EDUCATION
    # =====================================================

    "teacher": [
        "communication", "subject knowledge",
        "lesson planning", "classroom management",
        "teaching methods", "patience",
        "assessment", "technology skills"
    ],

    "school teacher": [
        "subject knowledge", "communication",
        "lesson planning", "classroom management",
        "teaching methods", "assessment",
        "patience"
    ],

    "college lecturer": [
        "subject knowledge", "communication",
        "teaching", "research",
        "presentation", "classroom management",
        "technology skills"
    ],

    "professor": [
        "subject knowledge", "research",
        "teaching", "communication",
        "academic writing", "presentation",
        "critical thinking"
    ],


    # =====================================================
    # AGRICULTURE
    # =====================================================

    "agriculture": [
        "soil science", "crop management",
        "irrigation", "agricultural technology",
        "pest management", "farm management",
        "plant biology", "weather knowledge"
    ],

    "agriculture officer": [
        "agriculture", "soil science",
        "crop management", "pest management",
        "irrigation", "farmer communication",
        "government schemes"
    ],

    "agricultural engineer": [
        "agricultural machinery",
        "soil science", "irrigation",
        "engineering", "farm management",
        "automation", "problem solving"
    ],

    "farmer": [
        "crop management", "soil science",
        "irrigation", "pest management",
        "weather knowledge", "farm management",
        "agricultural technology"
    ],


    # =====================================================
    # SCIENCE / RESEARCH
    # =====================================================

    "scientist": [
        "research", "scientific method",
        "data analysis", "critical thinking",
        "laboratory skills", "problem solving",
        "scientific writing", "experimentation"
    ],

    "research scientist": [
        "research", "scientific method",
        "data analysis", "experimentation",
        "laboratory skills", "scientific writing",
        "critical thinking"
    ],

    "biologist": [
        "biology", "cell biology",
        "genetics", "laboratory skills",
        "research", "data analysis",
        "scientific writing"
    ],

    "chemist": [
        "chemistry", "laboratory skills",
        "chemical analysis", "research",
        "safety procedures", "data analysis"
    ],

    "physicist": [
        "physics", "mathematics",
        "research", "data analysis",
        "experimentation", "problem solving"
    ],

    "mathematician": [
        "mathematics", "statistics",
        "problem solving", "logical reasoning",
        "research", "data analysis"
    ],

    "environmental scientist": [
        "environmental science", "ecology",
        "data analysis", "research",
        "climate science", "field work",
        "scientific writing"
    ],


    # =====================================================
    # BUSINESS / MANAGEMENT
    # =====================================================

    "business analyst": [
        "business analysis", "excel",
        "sql", "data analysis",
        "communication", "problem solving",
        "business knowledge"
    ],

    "business manager": [
        "leadership", "communication",
        "business strategy", "financial management",
        "team management", "decision making",
        "problem solving"
    ],

    "marketing manager": [
        "digital marketing", "communication",
        "market research", "social media",
        "branding", "analytics", "content creation"
    ],

    "hr manager": [
        "communication", "recruitment",
        "employee management", "labour laws",
        "conflict resolution", "leadership",
        "organizational skills"
    ],

    "entrepreneur": [
        "business planning", "leadership",
        "communication", "marketing",
        "financial management", "problem solving",
        "decision making"
    ],


    # =====================================================
    # FINANCE / ACCOUNTING
    # =====================================================

    "accountant": [
        "accounting", "excel", "taxation",
        "financial reporting", "bookkeeping",
        "tally", "attention to detail"
    ],

    "chartered accountant": [
        "accounting", "auditing", "taxation",
        "financial reporting", "corporate law",
        "financial analysis", "excel"
    ],

    "banker": [
        "banking", "finance", "accounting",
        "communication", "customer service",
        "financial analysis", "computer skills"
    ],

    "bank manager": [
        "banking", "finance", "leadership",
        "customer service", "financial management",
        "communication", "decision making"
    ],


    # =====================================================
    # LAW
    # =====================================================

    "lawyer": [
        "law", "legal research",
        "communication", "argumentation",
        "legal writing", "critical thinking",
        "negotiation"
    ],

    "advocate": [
        "law", "legal research",
        "legal writing", "communication",
        "argumentation", "negotiation",
        "critical thinking"
    ],

    "judge": [
        "law", "legal analysis",
        "decision making", "judicial reasoning",
        "communication", "ethics",
        "critical thinking"
    ],


    # =====================================================
    # MEDIA / CREATIVE
    # =====================================================

    "journalist": [
        "writing", "communication",
        "research", "interviewing",
        "current affairs", "fact checking",
        "storytelling"
    ],

    "content creator": [
        "content creation", "communication",
        "video editing", "social media",
        "writing", "creativity", "marketing"
    ],

    "graphic designer": [
        "graphic design", "photoshop",
        "illustrator", "creativity",
        "typography", "visual communication"
    ],

    "video editor": [
        "video editing", "storytelling",
        "visual effects", "audio editing",
        "creativity", "content creation"
    ],

    "photographer": [
        "photography", "camera skills",
        "lighting", "photo editing",
        "composition", "creativity"
    ],


    # =====================================================
    # TRAVEL / HOSPITALITY
    # =====================================================

    "hotel manager": [
        "hospitality", "customer service",
        "communication", "leadership",
        "hotel operations", "team management"
    ],

    "chef": [
        "cooking", "food safety",
        "kitchen management", "creativity",
        "menu planning", "time management"
    ],

    "pilot": [
        "aviation", "navigation",
        "communication", "aircraft knowledge",
        "decision making", "situational awareness",
        "discipline"
    ],

    "travel manager": [
        "travel planning", "communication",
        "customer service", "geography",
        "booking systems", "problem solving"
    ]
}


# =========================================================
# ADD BUILT-IN CAREERS TO JOB DATABASE
# =========================================================

for career, skills_list in career_skill_templates.items():

    if career not in job_skills:

        job_skills[career] = skills_list


# =========================================================
# ALL SKILL KEYWORDS
# =========================================================

skill_keywords = sorted(
    set(
        skill
        for skills_list in job_skills.values()
        for skill in skills_list
    )
)


# =========================================================
# SKILL DETECTION FUNCTION
# =========================================================

def detect_skills(text):

    text = text.lower()

    detected = []

    for skill in skill_keywords:

        if skill in text:

            detected.append(skill)

    return detected


# =========================================================
# LEARNING ROADMAP
# =========================================================

roadmaps = {

    # Technology

    "python":
        "Learn Python basics, functions, OOP, modules and advanced Python.",

    "programming":
        "Learn programming fundamentals, variables, conditions, loops, functions and problem solving.",

    "sql":
        "Learn SQL queries, joins, subqueries, databases and optimization.",

    "java":
        "Learn Java fundamentals, OOP, collections and application development.",

    "data structures":
        "Learn arrays, linked lists, stacks, queues, trees, graphs and hashing.",

    "algorithms":
        "Learn searching, sorting, recursion, greedy algorithms and algorithmic problem solving.",

    "html":
        "Learn HTML structure, forms, tables and semantic elements.",

    "css":
        "Learn CSS styling, layouts, Flexbox, Grid and responsive design.",

    "javascript":
        "Learn JavaScript fundamentals, DOM, ES6 and asynchronous programming.",

    "react":
        "Learn React components, hooks, state management and frontend development.",

    "git":
        "Learn Git, GitHub, repositories, branches, commits and version control.",

    "rest api":
        "Learn REST APIs, HTTP methods, JSON and API integration.",

    "django":
        "Learn Django framework, models, views, templates and web applications.",

    "pandas":
        "Learn Pandas for data cleaning, manipulation and analysis.",

    "numpy":
        "Learn NumPy arrays, mathematical operations and numerical computing.",

    "machine learning":
        "Learn supervised learning, unsupervised learning, algorithms and model evaluation.",

    "deep learning":
        "Learn neural networks, CNNs, RNNs and deep learning concepts.",

    "tensorflow":
        "Learn TensorFlow and build deep learning models.",

    "pytorch":
        "Learn PyTorch and build neural network models.",

    "aws":
        "Learn AWS cloud fundamentals, compute, storage and application deployment.",

    "azure":
        "Learn Azure cloud fundamentals, services and cloud deployment.",

    "docker":
        "Learn Docker containers, images and deployment basics.",

    "kubernetes":
        "Learn Kubernetes pods, deployments and container orchestration.",

    "linux":
        "Learn Linux commands, file systems, permissions and server administration.",


    # Medical

    "biology":
        "Learn basic biology, human biology, cells, genetics and biological processes.",

    "anatomy":
        "Learn human body structure, organs, tissues and major body systems.",

    "physiology":
        "Learn how organs and body systems function and interact.",

    "clinical skills":
        "Develop clinical examination, patient assessment and basic healthcare skills.",

    "diagnosis":
        "Learn clinical reasoning, symptoms analysis and basic diagnostic methods.",

    "patient care":
        "Learn patient communication, safety, basic care procedures and healthcare practices.",

    "medical ethics":
        "Learn professional ethics, patient confidentiality and responsible healthcare practices.",

    "pharmacology":
        "Learn medicines, drug actions, dosage concepts and safe medication practices.",

    "pathology":
        "Learn diseases, causes, diagnosis and laboratory-based disease analysis.",

    "first aid":
        "Learn basic first aid, emergency response and safety procedures.",

    "emergency care":
        "Learn emergency assessment, first response and basic emergency care principles.",

    "chemistry":
        "Learn chemical reactions, organic and inorganic chemistry and laboratory techniques.",


    # Engineering

    "mathematics":
        "Strengthen mathematics, logical reasoning and quantitative problem solving.",

    "physics":
        "Learn mechanics, electricity, waves, thermodynamics and practical physics.",

    "engineering mathematics":
        "Learn calculus, algebra, differential equations and engineering mathematics.",

    "structural engineering":
        "Learn structural design, materials, loads and structural analysis.",

    "construction":
        "Learn construction methods, materials, safety and project execution.",

    "autocad":
        "Learn AutoCAD drawing, 2D drafting, dimensions and technical design.",

    "surveying":
        "Learn land measurement, surveying instruments and site surveying.",

    "mechanics":
        "Learn force, motion, mechanics, materials and engineering applications.",

    "thermodynamics":
        "Learn heat, energy, thermodynamic laws and engineering applications.",

    "cad":
        "Learn computer-aided design and create technical engineering drawings.",

    "manufacturing":
        "Learn manufacturing processes, production systems and quality control.",

    "machine design":
        "Learn machine components, design principles and engineering calculations.",

    "electrical circuits":
        "Learn voltage, current, resistance, circuit analysis and electrical components.",

    "electronics":
        "Learn electronic components, circuits and practical electronics.",

    "digital electronics":
        "Learn logic gates, digital circuits, flip-flops and digital systems.",

    "microcontrollers":
        "Learn microcontroller programming, sensors and embedded applications.",

    "embedded systems":
        "Learn embedded programming, microcontrollers and hardware-software integration.",

    "c programming":
        "Learn C programming, pointers, functions, arrays and memory management.",


    # Police / Defence

    "physical fitness":
        "Improve strength, endurance, flexibility and overall physical fitness.",

    "discipline":
        "Build discipline, time management, consistency and professional responsibility.",

    "law knowledge":
        "Learn basic laws, legal procedures, rights, responsibilities and regulations.",

    "investigation":
        "Learn observation, evidence collection, questioning and investigation techniques.",

    "situational awareness":
        "Develop observation, alertness, risk identification and quick response skills.",

    "leadership":
        "Develop leadership, team management, decision making and responsibility.",

    "decision making":
        "Practice logical decision making, problem solving and situation analysis.",

    "current affairs":
        "Develop awareness of national, international, economic and social current events.",

    "public administration":
        "Learn government administration, public services, governance and administrative processes.",

    "teamwork":
        "Develop collaboration, communication, coordination and team problem solving.",

    "strategic thinking":
        "Develop planning, long-term thinking, risk analysis and strategic decision making.",


    # Education

    "communication":
        "Improve verbal communication, professional communication and interpersonal skills.",

    "subject knowledge":
        "Build strong knowledge in the subject you plan to teach.",

    "lesson planning":
        "Learn how to create lesson plans, learning objectives and classroom activities.",

    "classroom management":
        "Learn techniques for managing classrooms, student behavior and engagement.",

    "teaching methods":
        "Learn different teaching methods and student-centered learning strategies.",

    "patience":
        "Develop patience, active listening and positive interaction with learners.",

    "assessment":
        "Learn student assessment, tests, feedback and performance evaluation.",

    "teaching":
        "Learn teaching strategies, instructional design and effective classroom practices.",

    "research":
        "Learn research methodology, literature review, experimentation and documentation.",

    "academic writing":
        "Learn academic writing, research papers, citations and formal documentation.",


    # Agriculture

    "soil science":
        "Learn soil types, nutrients, soil fertility and soil management.",

    "crop management":
        "Learn crop selection, planting, growth management, harvesting and storage.",

    "irrigation":
        "Learn irrigation methods, water management and efficient agricultural practices.",

    "agricultural technology":
        "Learn modern agricultural technologies, smart farming and technology-based crop management.",

    "pest management":
        "Learn pest identification, prevention and integrated pest management.",

    "farm management":
        "Learn farm planning, resource management, budgeting and agricultural operations.",

    "plant biology":
        "Learn plant structure, growth, reproduction and plant health.",

    "weather knowledge":
        "Learn weather patterns, climate effects and weather-based agricultural planning.",

    "agricultural machinery":
        "Learn farm machinery, equipment operation and agricultural automation.",

    "government schemes":
        "Learn major agricultural schemes, farmer support programs and government services.",


    # Science

    "scientific method":
        "Learn observation, hypothesis formation, experimentation, analysis and conclusions.",

    "data analysis":
        "Learn data collection, cleaning, analysis and interpretation.",

    "critical thinking":
        "Develop analytical thinking, evidence evaluation and logical reasoning.",

    "laboratory skills":
        "Learn laboratory safety, equipment handling, sample preparation and experimentation.",

    "scientific writing":
        "Learn research papers, reports, citations and scientific documentation.",

    "experimentation":
        "Learn experimental design, data collection, testing and result analysis.",

    "logical reasoning":
        "Practice logical thinking, pattern recognition and structured problem solving.",

    "genetics":
        "Learn genes, DNA, inheritance and basic genetic principles.",

    "cell biology":
        "Learn cell structure, functions, cell division and cellular processes.",

    "environmental science":
        "Learn ecosystems, pollution, natural resources and environmental protection.",

    "ecology":
        "Learn ecosystems, biodiversity, food chains and environmental relationships.",

    "climate science":
        "Learn climate systems, climate change and environmental impacts.",

    "field work":
        "Develop field observation, data collection, documentation and safety skills.",


    # Business

    "business analysis":
        "Learn business requirements, process analysis, data interpretation and decision support.",

    "business strategy":
        "Learn strategic planning, market analysis, competitive positioning and business decisions.",

    "financial management":
        "Learn budgeting, financial planning, investment basics and financial decision making.",

    "team management":
        "Learn delegation, team coordination, performance management and leadership.",

    "digital marketing":
        "Learn SEO, social media marketing, online advertising and digital campaigns.",

    "market research":
        "Learn customer research, market trends, surveys and competitor analysis.",

    "social media":
        "Learn social media strategy, content planning, audience engagement and analytics.",

    "branding":
        "Learn brand identity, positioning, communication and brand strategy.",

    "content creation":
        "Learn content planning, writing, visual creation and social media publishing.",

    "recruitment":
        "Learn hiring processes, interview techniques, candidate evaluation and recruitment planning.",

    "employee management":
        "Learn employee engagement, performance management and workplace communication.",

    "conflict resolution":
        "Learn negotiation, active listening and techniques for resolving workplace conflicts.",

    "business planning":
        "Learn business models, market research, budgeting and business strategy.",


    # Finance

    "accounting":
        "Learn bookkeeping, journal entries, financial statements and accounting principles.",

    "excel":
        "Learn formulas, functions, pivot tables, charts and data analysis in Excel.",

    "taxation":
        "Learn taxation concepts, tax calculations, compliance and tax regulations.",

    "financial reporting":
        "Learn financial statements, reporting standards and financial analysis.",

    "bookkeeping":
        "Learn recording transactions, ledgers, journals and financial records.",

    "tally":
        "Learn Tally basics, accounting entries, GST and financial reports.",

    "banking":
        "Learn banking operations, financial products, customer service and banking procedures.",

    "finance":
        "Learn financial concepts, budgeting, investments and financial analysis.",

    "customer service":
        "Learn professional communication, customer handling and problem solving.",


    # Law

    "law":
        "Learn legal principles, laws, rights, duties and legal procedures.",

    "legal research":
        "Learn how to find, analyze and interpret laws, cases and legal documents.",

    "legal writing":
        "Learn professional legal drafting, documentation and structured legal writing.",

    "argumentation":
        "Develop logical arguments, evidence-based reasoning and persuasive communication.",

    "negotiation":
        "Develop negotiation, persuasion, communication and conflict-resolution skills.",

    "legal analysis":
        "Learn to analyze legal issues, evidence, laws and case information.",

    "judicial reasoning":
        "Develop structured legal reasoning and evidence-based decision making.",

    "ethics":
        "Learn professional ethics, responsibility and ethical decision making.",


    # Media / Creative

    "writing":
        "Improve grammar, professional writing, storytelling and clear written communication.",

    "interviewing":
        "Learn interview preparation, questioning, listening and information gathering.",

    "fact checking":
        "Learn source verification, evidence checking and accurate information reporting.",

    "storytelling":
        "Develop storytelling structure, creativity and audience-focused communication.",

    "graphic design":
        "Learn design principles, layouts, typography and visual communication.",

    "photoshop":
        "Learn image editing, retouching, layers, masks and graphic design workflows.",

    "illustrator":
        "Learn vector graphics, illustrations, logos and professional design workflows.",

    "creativity":
        "Develop creative thinking, idea generation and innovative problem solving.",

    "video editing":
        "Learn video cutting, transitions, audio, effects and professional editing workflows.",

    "photography":
        "Learn composition, exposure, lighting, camera settings and photography techniques.",

    "camera skills":
        "Learn camera settings, exposure, focus, lenses and photography techniques.",

    "lighting":
        "Learn natural and artificial lighting techniques for photography and video.",


    # Hospitality / Travel

    "hospitality":
        "Learn hotel operations, guest service, hospitality standards and professional behavior.",

    "hotel operations":
        "Learn front office, housekeeping, guest management and hotel operations.",

    "cooking":
        "Learn cooking techniques, food preparation, kitchen safety and menu planning.",

    "food safety":
        "Learn food hygiene, safe storage, contamination prevention and kitchen safety.",

    "kitchen management":
        "Learn kitchen organization, inventory, staff coordination and food safety.",

    "aviation":
        "Learn aviation fundamentals, aircraft systems, safety procedures and aviation regulations.",

    "navigation":
        "Learn navigation principles, maps, coordinates and route planning.",

    "aircraft knowledge":
        "Learn aircraft systems, components, basic aerodynamics and aviation safety.",

    "travel planning":
        "Learn itinerary planning, travel research, booking and customer assistance.",

    "geography":
        "Learn physical and human geography, locations, maps and geographical concepts."
}


# =========================================================
# ADDITIONAL ROADMAPS AUTOMATICALLY
# =========================================================

# Any skill without a detailed roadmap gets a useful generic roadmap.
for career_skills in job_skills.values():

    for skill in career_skills:

        if skill not in roadmaps:

            roadmaps[skill] = (
                f"Learn the fundamentals of {skill.title()}, "
                f"practice through real-world examples and build "
                f"practical knowledge in this area."
            )


# =========================================================
# STUDENT DETAILS
# =========================================================

st.header("👩‍🎓 Student Details")


# =========================================================
# RESUME UPLOAD
# =========================================================

st.subheader("📄 Upload Your Resume")

uploaded_resume = st.file_uploader(
    "Upload your resume PDF",
    type=["pdf"],
    help="Upload a PDF resume to automatically detect skills."
)


# =========================================================
# RESUME PROCESSING
# =========================================================

resume_text = ""

detected_skills = []


if uploaded_resume:

    try:

        reader = PdfReader(uploaded_resume)

        for page in reader.pages:

            text = page.extract_text()

            if text:

                resume_text += text


        detected_skills = detect_skills(
            resume_text
        )


        st.success(
            "✅ Resume uploaded and analyzed successfully!"
        )


        if detected_skills:

            st.subheader(
                "🤖 Skills Detected From Resume"
            )

            for skill in detected_skills:

                st.markdown(
                    f"""
                    <div class="skill-card">
                        🟢 <b>{skill.title()}</b>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No supported skills were detected automatically."
            )


    except Exception as error:

        st.error(
            f"❌ Unable to read the resume: {error}"
        )

else:

    st.info(
        "📄 Upload your resume to automatically detect your skills."
    )


# =========================================================
# INPUT DETAILS
# =========================================================

st.subheader("✍️ Enter Your Details")


name = st.text_input(
    "Enter your name",
    placeholder="Example: M. Meghana"
)


course = st.text_input(
    "Enter your course",
    placeholder="Example: BSc Data Science"
)


skills = st.text_input(
    "Enter your current skills",
    placeholder="Example: Python, Communication, Biology"
)


target_job = st.text_input(
    "🎯 What do you want to become in future?",
    placeholder="Example: Doctor, Police Officer, Teacher, Scientist"
)


st.caption(
    "💡 You can type any career or future goal. "
    "Examples: Doctor, Police Officer, Teacher, Engineer, "
    "Scientist, Agriculture Officer, Lawyer, etc."
)


st.divider()


# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🔍 Analyze My Skill Gap"
):


    # =====================================================
    # VALIDATION
    # =====================================================

    if (
        not name.strip()
        or not course.strip()
        or not skills.strip()
        or not target_job.strip()
    ):

        st.warning(
            "⚠️ Please fill in Name, Course, Current Skills and Future Career."
        )


    else:

        # =================================================
        # STUDENT SKILLS
        # =================================================

        student_skills = []


        # -------------------------------------------------
        # RESUME SKILLS
        # -------------------------------------------------

        if detected_skills:

            student_skills.extend(
                detected_skills
            )


        # -------------------------------------------------
        # MANUAL SKILLS
        # -------------------------------------------------

        manual_skills = [

            skill.strip().lower()

            for skill in skills.split(",")

            if skill.strip()

        ]


        for skill in manual_skills:

            if skill not in student_skills:

                student_skills.append(skill)


        # =================================================
        # TARGET CAREER
        # =================================================

        selected_job = (
            target_job
            .strip()
            .lower()
        )


        # =================================================
        # DIRECT CAREER MATCH
        # =================================================

        required_skills = job_skills.get(
            selected_job,
            []
        )


        matched_job_name = selected_job


        # =================================================
        # CAREER NAME ALIASES
        # =================================================

        career_aliases = {

            "doctor": "doctor",

            "medical doctor": "medical doctor",

            "police officer": "police officer",

            "police": "police",

            "teacher": "teacher",

            "professor": "professor",

            "scientist": "scientist",

            "engineer": "engineer",

            "agriculture": "agriculture",

            "farmer": "farmer",

            "lawyer": "lawyer",

            "advocate": "advocate",

            "nurse": "nurse",

            "pilot": "pilot",

            "chef": "chef",

            "accountant": "accountant",

            "banker": "banker",

            "photographer": "photographer",

            "journalist": "journalist"

        }


        if selected_job in career_aliases:

            alias_job = career_aliases[selected_job]

            if alias_job in job_skills:

                matched_job_name = alias_job

                required_skills = job_skills[alias_job]


        # =================================================
        # FUZZY CAREER MATCH
        # =================================================

        if not required_skills and job_skills:

            possible_matches = difflib.get_close_matches(

                selected_job,

                list(job_skills.keys()),

                n=1,

                cutoff=0.55

            )


            if possible_matches:

                matched_job_name = possible_matches[0]

                required_skills = job_skills[
                    matched_job_name
                ]


        # =================================================
        # PARTIAL CAREER MATCH
        # =================================================

        if not required_skills:

            for career_name in job_skills.keys():

                if (
                    selected_job in career_name
                    or career_name in selected_job
                ):

                    matched_job_name = career_name

                    required_skills = job_skills[
                        career_name
                    ]

                    break


        # =================================================
        # JOB NOT FOUND
        # =================================================

        if not required_skills:

            st.error(
                f"❌ We don't have a skill profile for '{target_job}' yet."
            )

            st.info(
                "💡 Try careers such as Doctor, Police Officer, "
                "Teacher, Engineer, Scientist, Agriculture Officer, "
                "Lawyer, Nurse, Python Developer, Data Scientist, etc."
            )


        else:

            # =================================================
            # NORMALIZE SKILLS
            # =================================================

            required_skills = list(
                dict.fromkeys(
                    skill.lower().strip()
                    for skill in required_skills
                )
            )


            student_skills = list(
                dict.fromkeys(
                    skill.lower().strip()
                    for skill in student_skills
                )
            )


            # =================================================
            # MATCHING SKILLS
            # =================================================

            matching_skills = [

                skill

                for skill in required_skills

                if skill in student_skills

            ]


            # =================================================
            # MISSING SKILLS
            # =================================================

            missing_skills = [

                skill

                for skill in required_skills

                if skill not in student_skills

            ]


            # =================================================
            # MATCH PERCENTAGE
            # =================================================

            if len(required_skills) > 0:

                skill_match_percentage = (

                    len(matching_skills)

                    / len(required_skills)

                ) * 100

            else:

                skill_match_percentage = 0


            # =================================================
            # RESULT HEADER
            # =================================================

            st.success(
                "🎉 Skill Gap Analysis Completed!"
            )


            if matched_job_name != selected_job:

                st.info(
                    f"💡 We matched your career with: "
                    f"**{matched_job_name.title()}**"
                )


            st.divider()


            # =================================================
            # STUDENT PROFILE
            # =================================================

            st.subheader(
                "👤 Student Profile"
            )


            col1, col2, col3 = st.columns(3)


            with col1:

                st.markdown(
                    f"""
                    <div class="section-card">

                        <b>👤 Name</b>

                        <br><br>

                        {name}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col2:

                st.markdown(
                    f"""
                    <div class="section-card">

                        <b>🎓 Course</b>

                        <br><br>

                        {course}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            with col3:

                st.markdown(
                    f"""
                    <div class="section-card">

                        <b>💼 Target Career</b>

                        <br><br>

                        {target_job}

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            st.divider()


            # =================================================
            # SKILL MATCH
            # =================================================

            st.subheader(
                "📊 Your Skill Match"
            )


            metric_col1, metric_col2, metric_col3 = st.columns(3)


            with metric_col1:

                st.metric(
                    "Skill Match",
                    f"{skill_match_percentage:.1f}%"
                )


            with metric_col2:

                st.metric(
                    "Skills You Have",
                    len(matching_skills)
                )


            with metric_col3:

                st.metric(
                    "Skills to Learn",
                    len(missing_skills)
                )


            st.progress(
                min(
                    int(skill_match_percentage),
                    100
                )
            )


            st.divider()


            # =================================================
            # SKILLS YOU HAVE
            # =================================================

            st.subheader(
                "✅ Skills You Already Have"
            )


            if matching_skills:

                for skill in matching_skills:

                    st.markdown(
                        f"""
                        <div class="skill-card">

                            🟢 <b>{skill.title()}</b>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.info(
                    "No required skills matched yet."
                )


            st.divider()


            # =================================================
            # SKILLS TO LEARN
            # =================================================

            st.subheader(
                "❌ Skills You Need to Learn"
            )


            if missing_skills:

                for skill in missing_skills:

                    st.markdown(
                        f"""
                        <div class="skill-card">

                            🔴 <b>{skill.title()}</b>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:

                st.success(
                    "🎉 Amazing! You already have all the required skills."
                )


            st.divider()


            # =================================================
            # PERSONALIZED LEARNING ROADMAP
            # =================================================

            st.subheader(
                "🗺️ Personalized Learning Roadmap"
            )


            if missing_skills:

                for number, skill in enumerate(

                    missing_skills,

                    start=1

                ):

                    explanation = roadmaps.get(

                        skill,

                        f"Learn the fundamentals of "
                        f"{skill.title()} and practice "
                        f"through real-world examples."

                    )


                    st.markdown(
                        f"""
                        <div class="roadmap-card">

                            <h3>
                                Step {number}: {skill.title()}
                            </h3>

                            <p>
                                {explanation}
                            </p>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )


            else:

                st.success(
                    "🚀 You already have all the required skills for this career."
                )


            # =================================================
            # CAREER STATUS
            # =================================================

            st.divider()

            st.subheader(
                "💡 Career Readiness"
            )


            if skill_match_percentage >= 80:

                message = (

                    "Excellent! Your current skills are strongly "
                    "aligned with your selected career. Continue "
                    "building practical experience and projects."

                )

            elif skill_match_percentage >= 50:

                message = (

                    "Good progress! You have a strong foundation, "
                    "but some additional skills can improve your "
                    "career readiness."

                )

            else:

                message = (

                    "You are at the beginning of your journey. "
                    "Follow the personalized roadmap step by step "
                    "and continue developing practical skills."

                )


            st.markdown(
                f"""
                <div class="info-card">

                    <h3>
                        🚀 Your Career Status
                    </h3>

                    <p>
                        {message}
                    </p>

                    <p>
                        Keep learning, practice through projects,
                        gain practical experience and build a
                        strong portfolio.
                    </p>

                </div>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()


st.markdown(
    """
    <div class="footer">

        🎯 <b>AI Skill Gap Analyzer</b>

        <br>

        AI-powered Career Guidance for Students

        <br><br>

        <span>
            Learn • Improve • Build • Grow 🚀
        </span>

    </div>
    """,
    unsafe_allow_html=True
)

  