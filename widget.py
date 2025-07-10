import streamlit as st
import pandas as pd
import random
import datetime
df = pd.read_csv("movies.csv")

st.divider()
st.title('버튼예제')
st.divider()
#1. 데이터 조회
if st.button("데이터 조회"):
    st.dataframe(df)

#2. 랜덤 영화 추천
if st.button("랜덤 추천"):
    st.write(df.sample(1))

#3. 평균 평점 계산
if st.button("평균 평점 보기"):
    st.write(df["rating"].mean())

##4. 최고 평점 영화
if st.button("최고 평점 영화"):
    st.write(df.loc[df["rating"].idxmax()])

#5. 최저 평점 영화
if st.button("최저 평점 영화"):
    st.write(df.loc[df["rating"].idxmin()])

#6. 장르별 분포 보기
if st.button("장르별 분포 차트"):
    st.bar_chart(df["genre"].value_counts())

#7. 히스토그램 그리기
if st.button("평점 히스토그램"):
    #st.bar_chart(pd.cut(df["rating"], bins=5).value_counts())
    # 구간 나누기
    cut_series = pd.cut(df["rating"], bins=5)

    # 값 세기 + 인덱스를 문자열로 변환
    cut_counts = cut_series.value_counts().sort_index()
    cut_counts.index = cut_counts.index.astype(str)

    # 스트림릿 차트에 전달
    st.bar_chart(cut_counts)

#8. 포스터 이미지 보기
if st.button("Spirited Away 포스터"):
    st.image("assets/spirited_away.jpg")

#9. JSON 형태로 내보내기
if st.button("JSON 다운로드"):
    st.download_button("JSON으로 저장", df.to_json(), file_name="movies.json")

#10. 캐시 초기화
if st.button("캐시 삭제"):
    st.cache_data.clear()
    st.success("캐시가 초기화되었습니다.")

st.divider()
st.title('체크박스 예제')
st.divider()

#11. 통계 요약 토글
if st.checkbox("통계 요약 보기"):
    st.write(df.describe())

#12. 지도 레이어 토글
if st.checkbox("지도에 표시"):
    st.map(df[["lat","lon"]])

#13. RAW 데이터 토글
if st.checkbox("원본 데이터 보기"):
    st.dataframe(df)

#14. 포스터 갤러리 토글
if st.checkbox("포스터 갤러리"):
    for img in ["la_la_land.jpg","parasite.jpg"]:
        st.image(f"assets/{img}", width=100)

#15. 장르별 분포표 토글
if st.checkbox("장르 분포표"):
    st.table(df["genre"].value_counts())

#16. 평점 평균 토글
if st.checkbox("평균 평점 계산"):
    st.metric("평균 평점", f"{df['rating'].mean():.2f}")

##17. 연도별 추세선 토글
if st.checkbox("연도별 평점 추세"):
    st.line_chart(df.groupby("year")["rating"].mean())

#18. 포함 장르 필터 토글
if st.checkbox("Animation 포함만"):
    st.dataframe(df[df["genre"]=="Animation"])

#19. 파일 업로드 토글
if st.checkbox("새 CSV 업로드"):
    st.file_uploader("CSV 파일 선택", type="csv")

#20. 컬러 피커 토글
if st.checkbox("배경색 조절"):
    color = st.color_picker("색 선택", "#ffffff")
    st.write(f"선택된 색: {color}")

st.divider()
st.title('라디오버튼 예제')
st.divider()

#21. 차트 유형 선택
kind = st.radio("차트 유형", ["Line","Bar"])
if kind=="Line":
    st.line_chart(df.groupby("year")["rating"].mean())
else:
    st.bar_chart(df["genre"].value_counts())
 
#22 평점 기준 선택
crit = st.radio("기준 선택", ["평균","최댓값","최솟값"])
val = {"평균":df["rating"].mean(),"최댓값":df["rating"].max(),"최솟값":df["rating"].min()}[crit]
st.write(f"{crit} 평점: {val}")
 
#23. 언어 설정(한국어/영어)
lang = st.radio("언어 선택", ["한국어","English"])
st.write(lang=="한국어" and "안녕하세요" or "Hello")
 
#24. 지도 vs 차트
view = st.radio("뷰 선택", ["지도","차트"])
if view=="지도":
    st.map(df[["lat","lon"]]) 
else:
    st.line_chart(df.groupby("year")["rating"].mean())

#25. 포스터 사이즈 선택
size = st.radio("포스터 사이즈", ["작게","보통","크게"])
w = {"작게":100,"보통":200,"크게":300}[size]
st.image("assets/parasite.jpg", width=w)

#26. 파일 포맷 선택
fmt = st.radio("다운로드 포맷", ["CSV","JSON"])
data = fmt=="CSV" and df.to_csv() or df.to_json()
st.download_button(fmt, data, file_name=f"movies.{fmt.lower()}")

#27. 프로필 사진 테마
theme = st.radio("테마 선택", ["밝게","어둡게"])
st.write(theme=="밝게" and "☀️" or "🌑")

#28. 폴더 유무 확인
exists = st.radio("폴더 존재 여부", [True, False])
st.write(exists and "폴더가 있습니다." or "폴더가 없습니다.")

#29. 설정 저장 여부
save = st.radio("설정 저장", ["예","아니오"])
st.write(save=="예" and "저장 완료" or "저장 안 함")

#30. 로그 레벨 선택
lvl = st.radio("로그 레벨", ["INFO","DEBUG","ERROR"])
st.write(f"현재 로그 레벨: {lvl}")

st.divider()
st.title('목록상자 예제')
st.divider()

#31. 장르 선택
genre = st.selectbox("장르 선택", df["genre"].unique())
st.dataframe(df[df["genre"]==genre])

#32. 연도 선택
year = st.selectbox("연도 선택", sorted(df["year"].unique()))
st.table(df[df["year"]==year])

#33. 영화 제목 선택
title = st.selectbox("영화 선택", df["title"].tolist())
st.write(df[df["title"]==title])

#34. 히스토그램 bin 개수
bins = st.selectbox("Bin 개수", [5,10,20])
#st.bar_chart(pd.cut(df["rating"], bins=bins).value_counts())
# 구간 나누기
cut_series = pd.cut(df["rating"], bins=bins)

# 값 세기 + 인덱스를 문자열로 변환
cut_counts = cut_series.value_counts().sort_index()
cut_counts.index = cut_counts.index.astype(str)

# 스트림릿 차트에 전달
st.bar_chart(cut_counts)

#35. 정렬 기준 선택
order = st.selectbox("정렬 기준", ["rating","year","title"])
st.write(df.sort_values(order))

#36. 다국어 지원
lang = st.selectbox("언어", ["ko","en"])
st.write(lang=="ko" and "영화 목록" or "Movie List")

#37. 화면 모드 선택
mode = st.selectbox("모드", ["요약","상세"])
#st.write(mode=="요약" and df.head() or df)
if mode == "요약":
    st.write(df.head())
else:
    st.write(df)


#38. 차트 스타일 선택
style = st.selectbox("차트 스타일", ["default","dark","whitegrid"])
st.write(f"스타일: {style}")

#39. 문서 형식 선택
fmt = st.selectbox("문서 형식", ["PDF","PPTX","DOCX"])
st.write(f"{fmt} 형식으로 내보내기 준비 중...")

#40. 테마 컬러 선택
theme = st.selectbox("테마", ["light","dark"])
st.write(f"테마: {theme}")

st.divider()
st.title('멀티상자 예제')
st.divider()

#41. 여러 장르 선택
gens = st.multiselect("장르 선택", df["genre"].unique(), default=["Action"])
st.dataframe(df[df["genre"].isin(gens)])

#42. 여러 연도 선택
yrs = st.multiselect("연도 선택", df["year"].unique(), default=[2019,2001])
st.write(df[df["year"].isin(yrs)])

#43. 여러 영화 제목 선택
titles = st.multiselect("영화 선택", df["title"].tolist(), default=["Parasite"])
st.write(df[df["title"].isin(titles)])

#44. 여러 차트 한 번에 보기
plots = st.multiselect("차트 선택", ["line","bar","area"], default=["bar"])
for p in plots:
    getattr(st, f"{p}_chart")(df.groupby("year")["rating"].mean())

#45. 여러 파일 포맷
fmts = st.multiselect("포맷 선택", ["csv","json","excel"], default=["csv"])
for f in fmts:
    st.write(f, len(df))

#46. 여러 색상 선택
cols = st.multiselect("컬러 선택", ["#FF0000","#00FF00","#0000FF"], default=["#FF0000"])
st.write("선택된 색:", cols)

#47. 여러 날짜 범위 선택
dates = st.multiselect("날짜 선택", df["release_date"].unique())
st.write(df[df["release_date"].isin(dates)])

#48. 여러 지도 레이어
layers = st.multiselect("레이어", ["위치","장르"], default=["위치"])
if "위치" in layers: st.map(df[["lat","lon"]])
if "장르" in layers: st.write(df["genre"].value_counts())
 
#49. 여러 API 호출
apis = st.multiselect("API", ["OMDB","TMDB","Custom"], default=["OMDB"])
st.write("선택 API:", apis)
 
#50. 여러 필터 조합
filters = st.multiselect("필터", ["평점&=8","2000년 이후","Thriller"], default=["평점&=8"])
# 이후 로직으로 필터 적용
st.write("필터:", filters)


st.divider()
st.title('슬라이더 예제')
st.divider()

#51. 평점 범위 슬라이더
lo, hi = st.slider("평점 범위", 0.0, 10.0, (7.0,9.0))
#st.write(df[(df["rating"]&=lo)&(df["rating"]&=hi)])
st.write(df[(df["rating"] >= lo) & (df["rating"] <= hi)])

#52. 연도 범위 슬라이더
y1, y2 = st.slider("년도 범위", int(df["year"].min()), int(df["year"].max()), (2000,2020))
st.write(df[(df["year"] >= y1) & (df["year"] <= y2)])

#53. 영화 개수 조절
n = st.slider("표시할 영화 수", 1, len(df), 3)
st.write(df.head(n))

#54. 이미지 폭 조절
w = st.slider("포스터 폭", 50, 300, 150)
st.image("assets/parasite.jpg", width=w)

#55. 히스토그램 bin 수
bins = st.slider("히스토그램 bin", 1, 20, 5)
#st.bar_chart(pd.cut(df["rating"], bins=bins).value_counts())
# 구간 나누기
cut_series = pd.cut(df["rating"], bins=bins)

# 값 세기 + 인덱스를 문자열로 변환
cut_counts = cut_series.value_counts().sort_index()
cut_counts.index = cut_counts.index.astype(str)

# 스트림릿 차트에 전달
st.bar_chart(cut_counts)

#56. 투표 점수 설정
score = st.slider("내 평점", 0.0, 10.0, 8.5, step=0.1)
st.write(f"내가 준 평점: {score}")

#57. 반응 지연 시간
delay = st.slider("로딩 지연(ms)", 0, 2000, 500, step=100)
import time; time.sleep(delay/1000)
st.write("지연 후 표시 완료")

#58. 라디오 패널 슬라이더
val = st.slider("값 선택", 0, 100, 50)
st.write("선택값:", val)

#59. 색상 투명도 조절
alpha = st.slider("투명도", 0.0, 1.0, 0.5)
st.write(f"투명도: {alpha}")

#60. 시간대 선택 (int-&시간)
hour = st.slider("시간 선택", 0, 23, 12)
st.write(f"{hour}:00")

st.divider()
st.title('숫자입력상자 예제')
st.divider()

#61. 최소 평점 입력
th = st.number_input("최소 평점", 0.0, 10.0, 8.0)
st.write(df[df["rating"] >= th])

#62. 최대 연도 입력
y = st.number_input("최대 연도", 1970, 2025, 2019)
st.write(df[df["year"] <= y])

#63. 페이지 번호 입력
page = st.number_input("페이지 번호", 1, 10, 1)
st.write(df.iloc[(page-1)*2:page*2])

#64. 선택 슬라이더와 연동
n = st.number_input("영화 수", 1, len(df), 3)
st.write(df.head(n))

#65. 정수/실수 동시 사용
i = st.number_input("정수 입력", 0, 10, 5)
f = st.number_input("실수 입력", 0.0, 1.0, 0.5)
st.write(i, f)

#66. 가격 입력 폼
price = st.number_input("티켓 가격", min_value=0, max_value=20000, value=12000, step=1000)
st.write("가격:", price)

#67. 배우 수 입력
actors = st.number_input("출연 배우 수", 1, 10, 3)
st.write(f"{actors}명 출연")

#68. 컬럼 너비 조절
width = st.number_input("차트 너비(px)", 200, 1000, 400)
st.line_chart(df.groupby("year")["rating"].mean(), width=width)

#69. 시간 간격 입력
minutes = st.number_input("타이머 설정(분)", 1, 60, 5)
st.write(f"{minutes}분 타이머 시작")
 
#70. 투표 참여자 수 입력
voters = st.number_input("투표 인원", 1, 100, 10)
st.write(f"{voters}명이 투표 예정")


st.divider()
st.title('텍스트 입력')
st.divider()

#71. 영화 제목 검색
kw = st.text_input("검색어 입력")
if kw: st.write(df[df["title"].str.contains(kw)])

#72. 유저 이름 입력
name = st.text_input("이름")
if name: st.write(f"환영합니다, {name}님")

#73. 해시태그 입력
tags = st.text_input("해시태그 (콤마로 구분)")
st.write(tags.split(","))

#74. 비밀번호 입력
pwd = st.text_input("비밀번호", type="password")
st.write("*"*len(pwd))

#75. URL 입력
url = st.text_input("영상 URL")
if url: st.video(url)
 
#76. 이메일 입력 검증
email = st.text_input("이메일")
if email and "@" in email: st.success("유효한 이메일입니다.")
 
#77. 코드 입력
code = st.text_input("파이썬 코드")
if code: st.code(code, language="python")

#78. 문장 카운트
text = st.text_input("문장 입력")
st.write("문자 수:", len(text))
 
#79. 날짜 형식 입력
date_str = st.text_input("날짜 (YYYY-MM-DD)")
# 간단 파싱 예시
 
#80. 검색 엔진 쿼리
query = st.text_input("검색어")
st.write(f"검색 결과: {query}")


st.divider()
st.title('날짜 입력 예제')
st.divider()

df["release_date"] = pd.to_datetime(df["release_date"])
#81. 시작일/종료일 범위
start = st.date_input("시작일", df["release_date"].min())
end   = st.date_input("종료일", df["release_date"].max())
st.write(df[(df["release_date"] >= pd.to_datetime(start)) & (df["release_date"] <= pd.to_datetime(end))])

#82. 단일 개봉일 선택
d = st.date_input("개봉일 선택", df["release_date"].iloc[0])
st.write(df[df["release_date"]==pd.to_datetime(d)])

#83. 오늘 날짜 표시
today = st.date_input("오늘 날짜")
st.write("오늘:", today)

#84. 최대/최소 날짜 제한
#st.date_input("2000년 이후", df["release_date"].min(), min_value=pd.to_datetime("2000-01-01"))
release_min = df["release_date"].min()
min_date = pd.to_datetime("2000-01-01")

default_date = release_min if release_min >= min_date else min_date

st.date_input("2000년 이후", default_date, min_value=min_date)

 
#85. 예약 폼
with st.form("res_form"):
    date = st.date_input("예약일")
    submitted = st.form_submit_button("예약")
    if submitted: st.write("예약 완료:", date)

#86. 연도만 선택 (대체)
#year = st.date_input("연도 선택", value=pd.to_datetime("2001-01-01"), format="YYYY")
# 예: 1970년부터 현재 연도까지 선택 가능
years = list(range(1970, datetime.datetime.now().year + 1))
selected_year = st.selectbox("연도 선택", years, index=years.index(2001))

st.write(f"선택한 연도: {selected_year}")

#87. 위젯 레이블 커스터마이징
st.date_input("📅 개봉일 선택", df["release_date"].min())

#88. 빈도별 개봉일 표시
st.write(df["release_date"].dt.year.value_counts())

#89. 달력 스타일 변경 (테마)
# Streamlit 자체 지원은 없으나 custom CSS로 가능

#90. 시간 선택과 조합
date = st.date_input("날짜")
time = st.time_input("시간")
st.write(datetime.datetime.combine(date, time))


st.divider()
st.title('파일업로드 예제')
st.divider()

#91. CSV 업로드 후 DataFrame 보기
uploaded = st.file_uploader("CSV 업로드", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.dataframe(df)

#92. 이미지 파일 업로드 후 바로 보여주기
img = st.file_uploader("포스터 업로드", type=["png","jpg"])
if img:
    st.image(img, caption="업로드된 포스터")

#93. 다중 파일 업로드
files = st.file_uploader("여러 파일 업로드", accept_multiple_files=True)
for f in files:
    st.write(f.name)

#94. 업로드된 CSV 요약 통계
uploaded = st.file_uploader("영화 CSV 업로드", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    if st.button("통계 보기"):
        st.write(df.describe())

#95. 업로드된 JSON 읽기
json_file = st.file_uploader("JSON 업로드", type="json")
if json_file:
    data = pd.read_json(json_file)
    st.json(data)

#96. 업로드된 엑셀(.xlsx) 읽기
excel = st.file_uploader("Excel 업로드", type="xlsx")
if excel:
    st.write(pd.read_excel(excel))

#97. 업로드 시 파일 크기 표시
file = st.file_uploader("파일 업로드", type=["csv","json"])
if file:
    st.write("파일 크기:", file.size, "bytes")

#98. 업로드된 텍스트(.txt) 보기
txt = st.file_uploader("텍스트 업로드", type="txt")
if txt:
    st.text(txt.getvalue().decode("utf-8"))

#99. 커스텀 처리: 업로드 후 파일명만 리스트로 출력
my_files = st.file_uploader("파일 선택", accept_multiple_files=True)
st.write([f.name for f in my_files])

#100. 업로드된 이미지 썸네일 생성
imgs = st.file_uploader("여러 이미지 업로드", accept_multiple_files=True, type=["png","jpg"])
for img in imgs:
    st.image(img, width=80)



st.divider()
st.title('다운로드버튼 예제')
st.divider()

#101. CSV 다운로드
csv_data = df.to_csv(index=False)
st.download_button("CSV 다운로드", csv_data, file_name="movies.csv", mime="text/csv")

#102. JSON 다운로드
json_data = df.to_json()
st.download_button("JSON 다운로드", json_data, file_name="movies.json", mime="application/json")

#103. 텍스트 파일(.txt) 다운로드
text = "\n".join(df["title"].tolist())
st.download_button("텍스트 다운로드", text, file_name="titles.txt", mime="text/plain")

#104. 엑셀 파일 다운로드
xlsx = df.to_excel("movies.xlsx", index=False)
with open("movies.xlsx","rb") as f:
    st.download_button("Excel 다운로드", f, file_name="movies.xlsx", mime="application/vnd.ms-excel")

#105. 이미지 다운로드 (바이너리)
with open("assets/parasite.jpg","rb") as img:
    st.download_button("포스터 다운로드", img, file_name="parasite.jpg", mime="image/jpeg")

#106. 바이너리 데이터 다운로드
binary = b'\x00\xFF\x00\xFF'
st.download_button("바이너리 다운로드", binary, file_name="data.bin", mime="application/octet-stream")

#107. 링크 대신 버튼으로 웹 파일 다운로드
url = "https://example.com/sample.png"
st.download_button("웹 이미지 다운로드", url, file_name="sample.png", mime="image/png")

#108. DataFrame 일부분만 다운로드
small = df.head(3).to_csv(index=False)
st.download_button("상위 3개 다운로드", small, file_name="top3.csv")

#109. Markdown 파일 다운로드
md = "# 영화 목록\n" + "\n".join(f"- {t}" for t in df["title"])
st.download_button("Markdown 다운로드", md, file_name="movies.md", mime="text/markdown")

#110. ZIP 압축해서 다운로드
import io, zipfile
zip_buffer = io.BytesIO()
with zipfile.ZipFile(zip_buffer,"w") as zf:
    zf.writestr("movies.csv", df.to_csv(index=False))
st.download_button("ZIP 다운로드", zip_buffer.getvalue(), file_name="movies.zip", mime="application/zip")



st.divider()
st.title('멀티라인텍스트상자 예제')
st.divider()

#111. 자유 메모장
note = st.text_area("메모를 입력하세요")
st.write("입력한 내용:", note)

#112. 기본값 있는 텍스트 영역
default = """영화 리뷰를 작성하세요."""
review = st.text_area("리뷰", value=default, height=150)
st.write(review)

#113. 코드 편집기 느낌
code = st.text_area("파이썬 코드 입력", value="print('Hello')", height=100)
st.code(code, language="python")

#114. 줄 수 제한
ta = st.text_area("최대 3줄", max_chars=100)
st.write(len(ta.splitlines()), "줄 입력됨")

#115. 댓글 기능 흉내
comments = st.text_area("댓글 달기", placeholder="여기에 댓글을 입력하세요")
st.write("댓글:", comments)

#116. 실시간 글자 수 세기
text = st.text_area("글자 세기", "")
st.write("글자 수:", len(text))

#117. 리뷰 분석 (더미)
text = st.text_area("AI 리뷰 분석", "")
if st.button("분석"):
    st.write("긍정" if "좋다" in text else "중립/부정")

#118. JSON 편집기
json_text = st.text_area("JSON 입력", value=df.head().to_json(indent=2), height=200)
st.json(json_text)

#119. 다국어 입력 지원
lang = st.selectbox("언어", ["한국어","English"])
msg = st.text_area("문장 입력")
st.write(lang, ":", msg)

#120. Markdown 입력기로 활용
md = st.text_area("Markdown 입력", value="# 제목\n본문")
st.markdown(md)


st.divider()
st.title('카메라 예제')
st.divider()

#121. 사진 찍어 보여주기
img = st.camera_input("사진 찍기")
if img:
    st.image(img)

#122. 얼굴 인식 더미
img = st.camera_input("얼굴 촬영")
if img and st.button("분석"):
    st.write("얼굴을 찾았습니다!")  # 실제 모델 연동 예시

#123. 사진 필터 적용
img = st.camera_input("필터 사진")
if img:
    from PIL import Image, ImageFilter
    im = Image.open(img).convert("RGB").filter(ImageFilter.BLUR)
    st.image(im, caption="블러 처리된 이미지")

#124. QR 코드 스캔(더미)
img = st.camera_input("QR 스캔")
if img and st.button("스캔"):
    st.write("https://streamlit.io")  # 결과 예시

#125. 바코드 인식(더미)
img = st.camera_input("바코드 인식")
if img and st.button("인식"):
    st.write("0110001010")  # 더미 데이터

#126. 사진 크롭
img = st.camera_input("크롭")
if img:
    from PIL import Image
    im = Image.open(img)
    w,h = im.size
    st.image(im.crop((0,0,w//2,h//2)), caption="좌상단 크롭")

#127. 사진 저장
img = st.camera_input("사진 저장")
if img and st.button("저장"):
    with open("capture.jpg","wb") as f: f.write(img.getbuffer())
    st.success("저장 완료")

#128. 사진 리사이즈
img = st.camera_input("리사이즈")
if img:
    from PIL import Image
    im = Image.open(img)
    st.image(im.resize((100,100)))

#129. 실시간 스냅샷
img = st.camera_input("실시간 스냅샷")
if img:
    st.write("캡처 시간:", pd.Timestamp.now())

#130. OCR(더미)
img = st.camera_input("OCR")
if img and st.button("텍스트 추출"):
    st.write("텍스트 내용")  # 실제 OCR 연동 예시




st.divider()
st.title('시간입력 예제')
st.divider()

#131. 기본 시간 선택
t = st.time_input("시간 선택", datetime.time(12,0))
st.write("선택된 시간:", t)

#132. 알람 설정
alarm = st.time_input("알람 시간", datetime.time(7,30))
if st.button("알람 설정"):
    st.write(f"알람이 {alarm}로 설정되었습니다")

#133. 타이머 시작 (더미)
start = st.time_input("시작 시간", datetime.time(0,0))
if st.button("시작"):
    st.write("타이머 시작:", start)

#134. 시간대 표시
tz = st.time_input("현지 시간", datetime.datetime.now().time())
st.write("현재 시각:", tz)

#135. 작업 시간 입력
work = st.time_input("근무 시작", datetime.time(9,0))
off = st.time_input("퇴근 시간", datetime.time(18,0))
st.write(f"근무시간: {off.hour-work.hour}시간")

#136. 알람 간격 선택
interval = st.time_input("간격", datetime.time(0,5))
st.write(f"{interval.minute}분 간격")

#137. 시간 비교
t1 = st.time_input("시간1", datetime.time(8,0))
t2 = st.time_input("시간2", datetime.time(17,0))
st.write("차이:", datetime.datetime.combine(datetime.date.today(),t2)-datetime.datetime.combine(datetime.date.today(),t1))

#148. 타임 스탬프 출력
t = st.time_input("출력 시간")
st.write("타임스탬프:", pd.Timestamp.combine(pd.Timestamp.today(), t))

#149. 예약폼 내 시간
with st.form("time_form"):
    t = st.time_input("예약 시간", datetime.time(15,0))
    submitted = st.form_submit_button("예약")
    if submitted: st.write("예약됨:", t)

#150. 운영시간 제한
t = st.time_input("방문 시간", datetime.time(12,0))
if not(datetime.time(9,0) <= t <= datetime.time(18,0)):
    st.warning("영업시간 외입니다")


st.divider()
st.title('범위선택 슬라이더 예제')
st.divider()

#151. 지문 샘플: 영화 연도 선택
year = st.select_slider("개봉년도", options=sorted(df["year"].unique()))
st.write("선택년도:", year)

#152. 영화 제목별 선택
title = st.select_slider("영화 선택", options=df["title"].tolist())
st.write("선택:", title)

#153. 평점 구간 선택
rt = st.select_slider("평점", options=[i/10 for i in range(0,101)], value=0.8)
st.write("평점:", rt)

#154. 텍스트 옵션 슬라이더
opt = st.select_slider("옵션", options=["A","B","C"])
st.write("옵션:", opt)

#155. 다중 옵션 슬라이더 (range)
r = st.select_slider("평점 범위", options=[i/10 for i in range(0,101)], value=(0.6,0.9))
st.write("범위:", r)

#156. DATE 슬라이더 (date list)
dates = sorted(pd.to_datetime(df["release_date"]).dt.date.unique())
d = st.select_slider("개봉일 선택", options=dates)
st.write("개봉일:", d)

#157. TIME 슬라이더
times = [datetime.time(i,0) for i in range(0,24)]
t = st.select_slider("시간 선택", options=times)
st.write("시간:", t)

#158. COLOR 슬라이더 (색상 코드)
cols = ["#FF0000FF","#00FF00","#0000FF"]
c = st.select_slider("색상 선택", options=cols)
#st.markdown(f"&div style='background:{c};padding:5px;'&색상&/div&", unsafe_allow_html=True)
st.markdown(
    f"<div style='background:{c}; padding:10px; border-radius:5px; color:white;'>선택한 색상: {c}</div>",
    unsafe_allow_html=True
)

#159. LIST 슬라이더
items = ["영화","드라마","다큐","애니"]
it = st.select_slider("장르 유형", options=items)
st.write("유형:", it)

#160. RANGE 슬라이더 함수 연동
years = sorted(df["year"].unique())
default_start = years[0]
default_end = years[-1]
lo, hi = st.select_slider("연도 범위", options=years, value=(default_start, default_end))
st.write(df[(df["year"] >= lo) & (df["year"] <= hi)])