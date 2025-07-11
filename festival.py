import streamlit as st
from datetime import date, time
import pandas as pd
import os

DATA_PATH = "Submissions.csv"

st.sidebar.title("메뉴 이동")
page = st.sidebar.selectbox("📋페이지 선택", ["설문 페이지", "분석 페이지"])

def append_response(result: dict):
    df = pd.DataFrame([result])

    if not os.path.isfile(DATA_PATH):
        df.to_csv(DATA_PATH, index=False, encoding="utf-8-sig")
    else:
        df.to_csv(DATA_PATH, mode='a', header=False, index=False, encoding="utf-8-sig")

if page == "설문 페이지":

    st.title("🎉 축제 아이디어 설문")
    st.write("부스와 공연에 대한 여러분의 창의적인 아이디어를 부탁드립니다.")
    st.divider()

    name = st.text_input("• 이름")
    grade = st.selectbox("• 학년", ["1학년", "2학년", "3학년"])
    agree = st.checkbox("• 개인정보 수집 동의")
    st.divider()
    booth_types = ["먹거리", "놀이/게임", "전시", "체험", "기타"]
    booth = st.selectbox("• 부스 종류", booth_types)
    if booth == "기타":
        booth = st.text_input(" -기타 부스 아이디어")
    booth_desc = st.text_area("• 부스 상세 설명", height=100)
    budget = st.slider("• 예상 예산 (만원)", 0, 100, (10, 30))
    color = st.color_picker("• 대표 색상 선택", "#FFD700")
    st.divider()
    perf_genres = ["댄스", "밴드/음악", "마술", "퍼포먼스 아트", "기타"]
    genres = st.multiselect("• 공연 장르", perf_genres)
    if "기타" in genres:
        other = st.text_input(" -기타 공연 장르")
        genres = [g for g in genres if g != "기타"] + [other]
    perf_title = st.text_input("• 공연 제목 제안")
    perf_date = st.date_input("• 공연 희망 날짜", min_value=date.today())
    perf_time = st.time_input("• 공연 희망 시간", value=time(18, 0))
    participants = st.number_input("• 예상 참여 인원", 1, 50, 5)
    st.divider()

    if st.button("✅ 제출하기"):
        if not name or not agree:
            st.error("이름과 동의 여부를 확인해주세요.")
        else:

            result = {
                "이름": name,
                "학년": grade,
                "부스 종류": booth,
                "부스 설명": booth_desc,
                "예산_min": budget[0],
                "예산_max": budget[1],
                "디자인 색상": color,
                "공연 장르": ";".join(genres),
                "공연 제목": perf_title,
                "공연 일시": f"{perf_date} {perf_time}",
                "참여 인원": participants,
            }
            append_response(result)
            st.success("제출되었습니다! 감사합니다.")

elif page == "분석 페이지":
    st.title("📊 설문 데이터 분석")
    if not os.path.isfile(DATA_PATH):
        st.warning("아직 제출된 데이터가 없습니다.")
    else:
        df = pd.read_csv(DATA_PATH)

        df['공연 장르'] = df['공연 장르'].str.split(';')

        st.subheader("📝 원본 데이터 확인")
        st.dataframe(df)
        
        st.subheader("📈 부스 종류 분포")
        st.bar_chart(df['부스 종류'].value_counts())

        st.subheader("🎓 학년별 분포")
        st.bar_chart(df['학년'].value_counts())

        st.subheader("🎭 공연 장르 분포")
        genre_counts = df.explode('공연 장르')['공연 장르'].value_counts()
        st.bar_chart(genre_counts)

        st.subheader("💰 예산 범위 추세")
        st.line_chart(df[['예산_min', '예산_max']])

        st.subheader("👥 참여 인원 분포")
        st.bar_chart(df['참여 인원'])

        st.download_button("CSV 다운로드",
                           df.to_csv(index=False).encnode('utf-8-sig'),
                           file_name="survey_analysis.csv",
                           mime="text/csv")
        