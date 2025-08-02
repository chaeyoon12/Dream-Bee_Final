
import streamlit as st
from career_result_messages import get_result_message
from career_counseling_texts import get_counseling_intro, get_counseling_result, get_counseling_closing

st.set_page_config(page_title="드림비", page_icon="🐝")

st.markdown(
    """
    <style>
    @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');

    * {
        font-family: 'Pretendard', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "step" not in st.session_state:
    st.session_state["step"] = "test"
if "scores" not in st.session_state:
    st.session_state["scores"] = {"인문사회": 0, "자연과학": 0, "공학": 0, "예체능": 0, "의학": 0}

step = st.session_state["step"]

if step == "test":
    st.title("🐝 드림비 성향 검사")
    st.markdown("너의 진로 성향을 간단하게 알아보자! 각 문항에 솔직하게 체크해줘.")

    questions = {
        "인문사회": ["다른 사람과 대화하는 걸 좋아한다.", "글을 읽거나 쓰는 것이 재미있다.", "사람들의 심리를 관찰하는 걸 좋아한다."],
        "자연과학": ["자연의 원리를 이해하는 게 흥미롭다.", "수학이나 과학 과목이 재미있다.", "실험이나 탐구 활동이 즐겁다."],
        "공학": ["기계나 로봇에 관심이 많다.", "문제를 해결하는 과정을 좋아한다.", "무언가를 만들거나 조립하는 게 좋다."],
        "예체능": ["그림, 음악, 춤 등 표현하는 걸 좋아한다.", "몸을 움직이는 활동을 즐긴다.", "창의적인 아이디어를 내는 걸 좋아한다."],
        "의학": ["사람들을 도와주는 일을 하고 싶다.", "생명과학에 흥미가 있다.", "꼼꼼하고 정확한 편이다."]
    }

    for field, qs in questions.items():
        for q in qs:
            response = st.radio(q, ["그렇다", "보통이다", "아니다"], key=q)
            if response == "그렇다":
                st.session_state["scores"][field] += 2
            elif response == "보통이다":
                st.session_state["scores"][field] += 1

    if st.button("검사 완료"):
        st.session_state["step"] = "result"
        st.rerun()

elif step == "result":
    st.title("🔍 검사 결과")
    scores = st.session_state["scores"]
    top_field = max(scores, key=scores.get)
    st.subheader(f"당신의 추천 계열은 👉 **{top_field}** 계열이에요!")
    st.markdown(get_result_message(top_field))

    if st.button("진로 상담 시작하기"):
        st.session_state["step"] = "counseling"
        st.rerun()

elif step == "counseling":
    st.title("🗣️ 진로 상담")
    top_field = max(st.session_state["scores"], key=st.session_state["scores"].get)

    st.markdown(get_counseling_intro(top_field))
    st.markdown(get_counseling_result(top_field))
    st.markdown(get_counseling_closing())
