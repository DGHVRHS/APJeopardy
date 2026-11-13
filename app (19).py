import streamlit as st

st.set_page_config(page_title="Jeopardy!", layout="wide")

# Game Data (2 Categories: Related Rates Worksheet + Vermont Ski Mountains)
JEOPARDY_DATA = {
    "Related Rates": [
        {
            "val": 200,
            "q": r"Each side of a square is increasing at a rate of $6\text{ cm/s}$. At what rate is the area of the square increasing when the area of the square is $16\text{ cm}^2$?",
            "a": r"$48\text{ cm}^2/\text{s}$  \n  *(Since $A = s^2 = 16 \implies s = 4\text{ cm}$, $\frac{dA}{dt} = 2s\frac{ds}{dt} = 2(4)(6) = 48$)*"
        },
        {
            "val": 400,
            "q": r"A cylindrical tank with radius $5\text{ m}$ is being filled with water at a rate of $3\text{ m}^3/\text{min}$. How fast is the height of the water increasing? ($V = \pi r^2 h$)",
            "a": r"$\frac{3}{25\pi}\text{ m/min}$ ($\approx 0.038\text{ m/min}$)  \n  *(Since $V = 25\pi h \implies \frac{dV}{dt} = 25\pi\frac{dh}{dt} \implies 3 = 25\pi\frac{dh}{dt}$)*"
        },
        {
            "val": 600,
            "q": r"The radius of a sphere is increasing at a rate of $4\text{ mm/s}$. How fast is the volume increasing when the diameter is $30\text{ mm}$? ($V = \frac{4}{3}\pi r^3$)",
            "a": r"$3600\pi\text{ mm}^3/\text{s}$ ($\approx 11,309.7\text{ mm}^3/\text{s}$)  \n  *(When diameter $= 30\text{ mm}$, $r = 15\text{ mm}$; $\frac{dV}{dt} = 4\pi r^2 \frac{dr}{dt} = 4\pi(15)^2(4)$)*"
        },
        {
            "val": 800,
            "q": r"A particle is moving along a hyperbola $xy = 8$. As it reaches the point $(4, 2)$, the $y$-coordinate is decreasing at a rate of $3\text{ cm/s}$. How fast is the $x$-coordinate of the point changing at that instant?",
            "a": r"Increasing at $6\text{ cm/s}$ ($\frac{dx}{dt} = 6\text{ cm/s}$)  \n  *($x\frac{dy}{dt} + y\frac{dx}{dt} = 0 \implies 4(-3) + 2\frac{dx}{dt} = 0$)*"
        },
        {
            "val": 1000,
            "q": r"A plane flying horizontally at an altitude of $1\text{ mi}$ and a speed of $500\text{ mi/h}$ passes directly over a radar station. Find the rate at which the distance from the plane to the station is increasing when it is $2\text{ mi}$ away from the station.",
            "a": r"$250\sqrt{3}\text{ mi/h}$ ($\approx 433.01\text{ mi/h}$)  \n  *($x^2 + 1^2 = s^2 \implies x = \sqrt{3}\text{ mi}$ when $s = 2\text{ mi}$; $2x\frac{dx}{dt} = 2s\frac{ds}{dt} \implies \sqrt{3}(500) = 2\frac{ds}{dt}$)*"
        }
    ],
    "Anything but Calculus...Please": [
        {
            "val": 200,
            "q": "Nicknamed 'The Beast of the East,' this is the largest ski resort in Vermont and the eastern United States.",
            "a": "Killington (Killington Resort)"
        },
        {
            "val": 400,
            "q": "Famous for its 'Front Four' expert trails, this resort sits on Vermont's highest peak, Mount Mansfield.",
            "a": "Stowe (Stowe Mountain Resort)"
        },
        {
            "val": 600,
            "q": "Known for the motto 'Ski It If You Can,' this Waitsfield-area mountain famously operates a single-chair lift and does not allow snowboards.",
            "a": "Mad River Glen"
        },
        {
            "val": 800,
            "q": "Located near the Canadian border in northern Vermont, this resort gets the highest average annual snowfall in eastern North America—a phenomenon locals call the 'Jay Cloud.'",
            "a": "Jay Peak"
        },
        {
            "val": 1000,
            "q": "Located in southern Vermont, this resort is known as the birthplace of modern snowboarding and hosted the U.S. Open Snowboarding Championships for 30 years.",
            "a": "Stratton Mountain"
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
    # 2-Column Jeopardy Grid
    categories = list(JEOPARDY_DATA.keys())
    cols = st.columns(len(categories))

    for cat_idx, cat in enumerate(categories):
        with cols[cat_idx]:
            st.markdown(f"### {cat}")
            for q_idx, item in enumerate(JEOPARDY_DATA[cat]):
                q_id = f"{cat}_{q_idx}"
                if q_id in st.session_state.used_questions:
                    st.button("---", key=q_id, disabled=True, use_container_width=True)
                else:
                    if st.button(f"${item['val']}", key=q_id, use_container_width=True):
                        st.session_state.used_questions.add(q_id)
                        st.session_state.active_q = {**item, "cat": cat}
                        st.rerun()
