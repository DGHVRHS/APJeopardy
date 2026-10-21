import streamlit as st

st.set_page_config(page_title="Jeopardy!", layout="wide")

# Game Data (3 Categories)
JEOPARDY_DATA = {
    "Power & Chain Rules": [
        {
            "val": 200,
            "q": r"Differentiate: $F(y) = \frac{7}{y^2} + \sqrt{2y} - 5y^3$",
            "a": r"$F'(y) = -\frac{14}{y^3} + \frac{1}{\sqrt{2y}} - 15y^2$"
        },
        {
            "val": 400,
            "q": r"Differentiate: $y = \sqrt{2x^2 - 10x + 7}$",
            "a": r"$y' = \frac{2x - 5}{\sqrt{2x^2 - 10x + 7}}$"
        },
        {
            "val": 600,
            "q": r"Differentiate: $h(x) = (3x^4 - 5)^7$",
            "a": r"$h'(x) = 84x^3(3x^4 - 5)^6$"
        },
        {
            "val": 800,
            "q": r"Differentiate: $f(x) = \frac{1}{\sqrt{4x^3 + 1}}$",
            "a": r"$f'(x) = -\frac{6x^2}{(4x^3 + 1)^{3/2}}$"
        },
        {
            "val": 1000,
            "q": r"Differentiate: $g(x) = (2x^2 - 5x)^{2/3}$",
            "a": r"$g'(x) = \frac{2(4x - 5)}{3\sqrt[3]{2x^2 - 5x}}$"
        }
    ],
    "Product, Quotient & Trig": [
        {
            "val": 200,
            "q": r"Differentiate: $y = 4x^3 \sin(x)$",
            "a": r"$y' = 12x^2 \sin(x) + 4x^3 \cos(x)$"
        },
        {
            "val": 400,
            "q": r"Differentiate: $g(t) = 10t^3 \tan(t) + 6 \sin(t)$",
            "a": r"$g'(t) = 30t^2 \tan(t) + 10t^3 \sec^2(t) + 6 \cos(t)$"
        },
        {
            "val": 600,
            "q": r"Differentiate: $y = \frac{\sec(2x)}{3 - 4x^3}$",
            "a": r"$y' = \frac{2\sec(2x)\tan(2x)(3 - 4x^3) + 12x^2\sec(2x)}{(3 - 4x^3)^2}$"
        },
        {
            "val": 800,
            "q": r"Differentiate: $f(x) = \frac{\cos(x)}{2x^2 + 1}$",
            "a": r"$f'(x) = \frac{-(2x^2 + 1)\sin(x) - 4x\cos(x)}{(2x^2 + 1)^2}$"
        },
        {
            "val": 1000,
            "q": r"Differentiate: $h(t) = t^2 \sec(3t)$",
            "a": r"$h'(t) = 2t\sec(3t) + 3t^2\sec(3t)\tan(3t)$"
        }
    ],
    "Philosophers & Mathematicians": [
        {
            "val": 200,
            "q": "This 17th-century French mathematician created a famous wager on the existence of God and popularized a triangular array of binomial coefficients.",
            "a": "Blaise Pascal"
        },
        {
            "val": 400,
            "q": "This French polymath is famous for his work in celestial mechanics and an integral transform that converts differential equations into algebraic ones.",
            "a": "Pierre-Simon Laplace"
        },
        {
            "val": 600,
            "q": "This French-Algerian philosopher and Nobel laureate formulated Absurdism in works like 'The Stranger' and 'The Myth of Sisyphus'.",
            "a": "Albert Camus"
        },
        {
            "val": 800,
            "q": "This French philosopher and mathematician coined 'Cogito, ergo sum' and developed the Cartesian coordinate system.",
            "a": "René Descartes"
        },
        {
            "val": 1000,
            "q": "This German polymath independent of Isaac Newton co-invented calculus and developed modern binary notation.",
            "a": "Gottfried Wilhelm Leibniz"
        }
    ]
}

# Session State Setup for 4 Teams
if "scores" not in st.session_state:
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
if "used_questions" not in st.session_state:
    st.session_state.used_questions = set()
if "active_q" not in st.session_state:
    st.session_state.active_q = None

st.title("🏆 Classroom Jeopardy!")

# Scoreboard Sidebar
st.sidebar.header("Scoreboard")
for team in st.session_state.scores:
    st.session_state.scores[team] = st.sidebar.number_input(
        f"{team}", value=st.session_state.scores[team], step=100
    )

if st.sidebar.button("Reset Game"):
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
    st.session_state.used_questions = set()
    st.session_state.active_q = None
    st.rerun()

# Active Question Screen
if st.session_state.active_q:
    q_data = st.session_state.active_q
    st.info(f"**Category:** {q_data['cat']} | **Value:** ${q_data['val']}")
    
    st.markdown(f"### {q_data['q']}")
    st.write("---")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Answer"):
            st.success(f"**Answer:** {q_data['a']}")
    
    st.write("### Award Points:")
    score_cols = st.columns(4)
    for idx, team in enumerate(st.session_state.scores):
        if score_cols[idx].button(f"+${q_data['val']} to {team}"):
            st.session_state.scores[team] += q_data['val']
            st.session_state.active_q = None
            st.rerun()
            
    if st.button("Close Question without Points"):
        st.session_state.active_q = None
        st.rerun()

else:
    # 3-Column Jeopardy Grid
    categories = list(JEOPARDY_DATA.keys())
    cols = st.columns(len(categories))

    for cat_idx, cat in enumerate(categories):
        with cols[cat_idx]:
            st.markdown(f"### {cat}")
            for q_idx, item in enumerate(JEOPARDY_DATA[cat]):
                q_id = f"{cat}_{q_idx}"
                if q_id in st.session_state.used_questions:
                    st.button(f"---", key=q_id, disabled=True, use_container_width=True)
                else:
                    if st.button(f"${item['val']}", key=q_id, use_container_width=True):
                        st.session_state.used_questions.add(q_id)
                        st.session_state.active_q = {**item, "cat": cat}
                        st.rerun()
