import streamlit as st

st.set_page_config(page_title="Jeopardy!", layout="wide")

# Game Data
JEOPARDY_DATA = {
    "Take Me Home Country Roads": [
        {"val": 200, "q": "This city serves as the capital of West Virginia.", "a": "Charleston"},
        {"val": 400, "q": "The state motto 'Montani Semper Liberi' translates to this in English.", "a": "Mountaineers Are Always Free"},
        {"val": 600, "q": "This famous bridge hosts an annual festival where extreme sports enthusiasts BASE jump off it.", "a": "New River Gorge Bridge"},
        {"val": 800, "q": "West Virginia officially split from Virginia and became a state in this year during the Civil War.", "a": "1863"},
        {"val": 1000, "q": "This native West Virginia apple variety was discovered in Clay County in 1905.", "a": "Golden Delicious"}
    ],
    "Yinzer Nation": [
        {"val": 200, "q": "This legendary Pirates outfielder was a 15-time All-Star and wore number 21.", "a": "Roberto Clemente"},
        {"val": 400, "q": "The Pirates have played their home games at this ballpark since 2001.", "a": "PNC Park"},
        {"val": 600, "q": "The Pirates last won the World Series in this year behind the 'We Are Family' team.", "a": "1979"},
        {"val": 800, "q": "This slugger won two MVP awards with Pittsburgh before leaving for San Francisco in 1993.", "a": "Barry Bonds"},
        {"val": 1000, "q": "This pitcher notoriously threw a no-hitter in 1970 while allegedly under the influence of LSD.", "a": "Dock Ellis"}
    ],
    "Limits": [
        {"val": 200, "q": r"Evaluate: $\lim_{x \to 2} (3x^2 - 5)$", "a": "7"},
        {"val": 400, "q": r"Evaluate: $\lim_{x \to 0} \frac{\sin(x)}{\cos(x)}$", "a": "0"},
        {"val": 600, "q": r"Evaluate: $\lim_{x \to \infty} \frac{4x^3 - 2}{2x^3 + 5}$", "a": "2"},
        {"val": 800, "q": r"Evaluate: $\lim_{x \to 3} \frac{x^2 - 9}{x - 3}$", "a": "6"},
        {"val": 1000, "q": r"Evaluate: $\lim_{x \to \infty} \left(1 + \frac{1}{x}\right)^x$", "a": "e"}
    ],
    "Believe": [
        {"val": 200, "q": "The fictional English soccer team that Ted Lasso is hired to coach.", "a": "AFC Richmond"},
        {"val": 400, "q": "Ted hangs a iconic yellow sign containing this single word above his office door.", "a": "BELIEVE"},
        {"val": 600, "q": "Ted often refers to this popular hot beverage as 'pigeon sweat' or 'garbage water'.", "a": "Tea"},
        {"val": 800, "q": "The owner of AFC Richmond who initially hired Ted hoping the team would fail.", "a": "Rebecca Welton"},
        {"val": 1000, "q": "Coach Beard's real first name, revealed in the series finale.", "a": "Willis"}
    ]
}

# Session State Initialization
if "scores" not in st.session_state:
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
if "used_questions" not in st.session_state:
    st.session_state.used_questions = set()
if "active_q" not in st.session_state:
    st.session_state.active_q = None

st.title("🏆 Jeopardy!")

# Scoreboard Sidebar
st.sidebar.header("Team Scores")
for team in st.session_state.scores:
    st.session_state.scores[team] = st.sidebar.number_input(
        f"{team}", value=st.session_state.scores[team], step=100
    )

if st.sidebar.button("Reset Game"):
    st.session_state.scores = {"Team 1": 0, "Team 2": 0, "Team 3": 0, "Team 4": 0}
    st.session_state.used_questions = set()
    st.session_state.active_q = None
    st.rerun()

# Active Question Modal Display
if st.session_state.active_q:
    q_data = st.session_state.active_q
    st.info(f"**Category:** {q_data['cat']} | **Value:** ${q_data['val']}")
    st.subheader(f"Question: {q_data['q']}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Show Answer"):
            st.success(f"**Answer:** {q_data['a']}")
    
    st.write("---")
    st.write("Award Points:")
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
    # Jeopardy Board Grid
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
