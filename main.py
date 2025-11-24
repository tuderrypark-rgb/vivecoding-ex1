import streamlit as st

# 1. 페이지 설정 및 제목
st.set_page_config(
    page_title="헬로 월드 앱",
    layout="centered"
)

# 2. 배경에 고양이 이미지를 적용하는 CSS
# base64 인코딩된 이미지 대신, 웹 접근 가능한 이미지 URL을 사용합니다.
# 실제 서비스에서는 안정적인 이미지 호스팅이 필요합니다.
CAT_IMAGE_URL = "https://cdn.pixabay.com/photo/2017/11/06/13/45/cat-2923265_1280.jpg"

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({CAT_IMAGE_URL});
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-position: center;
        opacity: 0.9; /* 배경 이미지 투명도 조절 */
    }}
    /* 입력 위젯과 메시지 텍스트가 잘 보이도록 배경색을 추가 */
    .stTextInput > div, .stButton > button, .stMarkdown, .stAlert {{
        background-color: rgba(255, 255, 255, 0.85); /* 흰색 배경, 높은 투명도 */
        padding: 10px;
        border-radius: 10px;
    }}
    .stTextInput > label {{
        background-color: transparent; /* 라벨 배경 제거 */
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("😸 헬로 월드 인사 앱")

# 3. 사용자 이름 입력 필드
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 4. "입력" 버튼
if st.button("입력"):
    # 5. 버튼 클릭 시 메시지 출력
    if user_name:
        # st.balloons() # 메시지 출력 시 풍선 효과 (선택 사항)
        st.success(f"짠~ **{user_name}**님, 헬로 월드!")
        st.write("Streamlit 웹앱에 오신 것을 환영합니다!")
    else:
        st.warning("이름을 먼저 입력해주세요.")
