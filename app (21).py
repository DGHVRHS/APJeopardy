import streamlit as st

st.set_page_config(page_title="Jeopardy!", layout="wide")

# Game Data (5 Categories: 3 Calculus Applications + Vermont Ski Mountains + Alien Movies)
JEOPARDY_DATA = {
    "Related Rates & Linearization": [
        {
            "val": 200,
            "q": r"Find the linearization $L(x)$ of the function $f(x) = \sqrt{x + 12}$ at $a = 4$.",
            "a": r"$L(x) = 4 + \frac{1}{8}(x - 4)$  \n  *($f(4) = 4$ and $f'(4) = \frac{1}{2\sqrt{16}} = \frac{1}{8}$)*"
        },
        {
            "val": 400,
            "q": r"Use a linear approximation of $f(x) = x^4$ centered at $a = 2$ to estimate $(2.003)^4$.",
            "a": r"$16.096$  \n  *($L(2.003) = 2^4 + 4(2^3)(0.003) = 16 + 32(0.003) = 16.096$)*"
        },
        {
            "val": 600,
            "q": r"A spherical snowball melts so its volume decreases at $20\pi\text{ cm}^3/\text{min}$. How fast is the radius decreasing when the diameter is $10\text{ cm}$? ($V = \frac{4}{3}\pi r^3$)",
            "a": r"$0.2\text{ cm/min}$ ($\frac{dr}{dt} = -\frac{1}{5}\text{ cm/min}$)  \n  *(At $r = 5$, $-20\pi = 4\pi(5)^2 \frac{dr}{dt} \implies \frac{dr}{dt} = -\frac{20}{100}$)*"
        },
        {
            "val": 800,
            "q": r"A $13$-foot ladder leans against a vertical wall. If the bottom slides away at $3\text{ ft/s}$, how fast is the top sliding down when the bottom is $5\text{ ft}$ from the wall?",
            "a": r"$1.25\text{ ft/s}$ ($\frac{dy}{dt} = -\frac{5}{4}\text{ ft/s}$)  \n  *(When $x = 5$, $y = 12$; $5(3) + 12\frac{dy}{dt} = 0 \implies \frac{dy}{dt} = -\frac{15}{12}$)*"
        },
        {
            "val": 1000,
            "q": r"A conical tank (vertex down) has radius $3\text{ m}$ and height $9\text{ m}$. Water is pumped in at $2\pi\text{ m}^3/\text{min}$. How fast is the water level rising when the water is $6\text{ m}$ deep? ($V = \frac{1}{3}\pi r^2 h$)",
            "a": r"$0.5\text{ m/min}$ ($\frac{dh}{dt} = \frac{1}{2}\text{ m/min}$)  \n  *(Since $r = \frac{h}{3}$, $V = \frac{\pi}{27}h^3 \implies 2\pi = \frac{\pi}{9}(6)^2 \frac{dh}{dt}$)*"
        }
    ],
    "Extrema, MVT & Curve Sketching": [
        {
            "val": 200,
            "q": r"Find all critical numbers of $f(x) = x^{1/3}(x - 4)$.",
            "a": r"$x = 0$ and $x = 1$  \n  *($f'(x) = \frac{4(x - 1)}{3x^{2/3}}$, which equals $0$ at $x = 1$ and is undefined at $x = 0$)*"
        },
        {
            "val": 400,
            "q": r"Find the absolute maximum and absolute minimum values of $f(x) = x^3 - 6x^2 + 9x + 1$ on the closed interval $[0, 5]$.",
            "a": r"Absolute Max: $21$ (at $x = 5$); Absolute Min: $1$ (at $x = 0$ and $x = 3$)  \n  *(Critical numbers $x = 1, 3$: $f(0)=1, f(1)=5, f(3)=1, f(5)=21$)*"
        },
        {
            "val": 600,
            "q": r"Find all numbers $c$ in $(1, 4)$ that satisfy the conclusion of the Mean Value Theorem for $f(x) = \sqrt{x}$ on $[1, 4]$.",
            "a": r"$c = \frac{9}{4}$ ($2.25$)  \n  *($\frac{\sqrt{4} - \sqrt{1}}{4 - 1} = \frac{1}{3} = \frac{1}{2\sqrt{c}} \implies \sqrt{c} = \frac{3}{2}$)*"
        },
        {
            "val": 800,
            "q": r"Find the coordinates of the inflection point of $f(x) = x^3 - 6x^2 + 5x + 2$.",
            "a": r"$(2, -4)$  \n  *($f''(x) = 6x - 12 = 0 \implies x = 2$, where concavity changes from down to up; $f(2) = -4$)*"
        },
        {
            "val": 1000,
            "q": r"A twice-differentiable function $g$ satisfies $g'(3) = 0$ and $g''(3) = -5$. What does the Second Derivative Test conclude at $x = 3$, and what if $g''(3) = 0$ instead?",
            "a": r"Local maximum at $x = 3$ (since $g''(3) < 0$). If $g''(3) = 0$, the test is inconclusive and you must use the First Derivative Test."
        }
    ],
    "L'Hôpital's Rule & Optimization": [
        {
            "val": 200,
            "q": r"Evaluate the limit using L'Hôpital's Rule: $\lim_{x \to 2} \frac{\ln(x - 1)}{x^2 - 4}$",
            "a": r"$\frac{1}{4}$  \n  *($\frac{0}{0}$ form $\implies \lim_{x \to 2} \frac{\frac{1}{x - 1}}{2x} = \frac{1}{4}$)*"
        },
        {
            "val": 400,
            "q": r"Evaluate the limit using L'Hôpital's Rule: $\lim_{x \to 0} \frac{e^{3x} - 1 - 3x}{x^2}$",
            "a": r"$\frac{9}{2}$  \n  *(Apply L'Hôpital's Rule twice: $\lim_{x \to 0} \frac{3e^{3x} - 3}{2x} = \lim_{x \to 0} \frac{9e^{3x}}{2} = \frac{9}{2}$)*"
        },
        {
            "val": 600,
            "q": r"Find two positive numbers whose product is $100$ and whose sum is a minimum.",
            "a": r"$10$ and $10$  \n  *(Minimize $S(x) = x + \frac{100}{x} \implies S'(x) = 1 - \frac{100}{x^2} = 0 \implies x = 10, y = 10$)*"
        },
        {
            "val": 800,
            "q": r"A farmer has $400\text{ ft}$ of fencing to enclose a rectangular pasture along a straight river (no fence along the river) and divide it into $2$ equal pens with $1$ interior fence perpendicular to the river. Find the maximum total area.",
            "a": r"$\frac{40,000}{3}\text{ ft}^2$ ($\approx 13,333.3\text{ ft}^2$)  \n  *($3x + y = 400 \implies A(x) = x(400 - 3x) \implies x = \frac{200}{3}\text{ ft}, y = 200\text{ ft}$)*"
        },
        {
            "val": 1000,
            "q": r"A theater sells $400$ tickets when the price is $$20$. For every $$1$ price increase, $10$ fewer tickets sell. What ticket price maximizes revenue?",
            "a": r"$$30$ (Max revenue: $$9,000$)  \n  *($R(n) = (20 + n)(400 - 10n) = 8000 + 200n - 10n^2 \implies R'(n) = 200 - 20n = 0 \implies n = 10$)*"
        }
    ],
    "Shredding the Pow": [
        {
            "val": 200,
            "q": "Known as 'America's Family Resort,' this Jeffersonville mountain features three interconnected peaks—Madonna, Sterling, and Morse—just across the notch from Stowe.",
            "a": "Smugglers' Notch"
        },
        {
            "val": 400,
            "q": "Located in southern Vermont near West Dover, this resort installed the East's first high-speed six-passenger bubble chairlift ('Bluebird Express') and is famous for its Carinthia terrain parks.",
            "a": "Mount Snow"
        },
        {
            "val": 600,
            "q": "Situated in the Mad River Valley, this resort consists of two main mountain areas—Lincoln Peak and Mount Ellen—connected by the Slide Brook Express quad.",
            "a": "Sugarbush (Sugarbush Resort)"
        },
        {
            "val": 800,
            "q": "Located in Ludlow, Vermont, this resort is renowned for its snowmaking and grooming, and takes its name from a Native American phrase meaning 'all come home.'",
            "a": "Okemo (Okemo Mountain Resort)"
        },
        {
            "val": 1000,
            "q": "Located in Vermont's Northeast Kingdom near East Burke, this mountain is home to a famous ski academy that trained Olympic gold medalist Mikaela Shiffrin.",
            "a": "Burke Mountain"
        }
    ],
    "Phone Home": [
        {
            "val": 200,
            "q": "In this 1982 Steven Spielberg classic, a young boy named Elliott befriends a stranded extraterrestrial who loves Reese's Pieces and wants to 'phone home.'",
            "a": "E.T. the Extra-Terrestrial"
        },
        {
            "val": 400,
            "q": "In this 1979 Ridley Scott sci-fi horror film, the crew of the commercial space tug Nostromo is hunted by a deadly Xenomorph with the tagline 'In space no one can hear you scream.'",
            "a": "Alien"
        },
        {
            "val": 600,
            "q": "Starring Will Smith and Tommy Lee Jones, this 1997 sci-fi comedy follows a secret agency that monitors and polices extraterrestrials living disguised in New York City.",
            "a": "Men in Black"
        },
        {
            "val": 800,
            "q": "Directed by Denis Villeneuve and starring Amy Adams, this 2016 sci-fi drama follows a linguist recruited to decipher the language of twelve giant shell-shaped alien spacecraft.",
            "a": "Arrival"
        },
        {
            "val": 1000,
            "q": "In this 1996 summer blockbuster, massive alien saucers hover over major world cities and destroy the White House before humanity launches a counterattack on the Fourth of July.",
            "a": "Independence Day"
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
    # 5-Column Jeopardy Grid
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
