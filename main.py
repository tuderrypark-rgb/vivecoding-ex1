import streamlit as st
import random
import time

# 1. 페이지 설정 및 제목
st.set_page_config(
    page_title="헬로 월드 앱",
    layout="centered"
)

# 배경 이미지 CSS 제거
# st.markdown 스타일 블록을 주석 처리하거나 제거합니다.

st.title("😸 헬로 월드 인사 앱")

# 3. 사용자 이름 입력 필드
user_name = st.text_input("당신의 이름은 무엇인가요?", placeholder="여기에 이름을 입력하세요.")

# 4. "입력" 버튼
if st.button("입력"):
    # 5. 버튼 클릭 시 메시지 출력
    if user_name:
        st.success(f"짠~ **{user_name}**님, 헬로 월드!")
        st.write("Streamlit 웹앱에 오신 것을 환영합니다!")

        # 고양이 이모지 여러 마리 출력
        st.subheader("🎉 고양이 파티! 🎉")
        
        # 고양이 이모지를 담을 컨테이너 생성
        cat_container = st.empty()
        
        # 화면에 뿌릴 고양이 개수와 이모지 리스트
        num_cats = 30 # 원하는 고양이 개수
        cat_emojis = ["🐱", "🐈", "🐾", "😻", "😽"]
        
        cat_display = []
        for i in range(num_cats):
            # 랜덤한 위치에 고양이 이모지 추가
            # Streamlit은 직접적인 절대 위치 제어를 제공하지 않으므로,
            # 여러 개의 컬럼을 사용하여 "랜덤"처럼 보이게 하거나,
            # 단순히 여러 줄에 걸쳐 출력하는 방식으로 구현합니다.
            
            # 여기서는 간단히 한 줄에 여러 개, 여러 줄에 걸쳐 출력하는 방식으로 구현합니다.
            # 실제 완벽한 "랜덤 위치"는 CSS 또는 JavaScript가 더 적합하지만,
            # Streamlit의 한계 내에서 최선을 다합니다.
            
            # 한 줄에 여러 개의 고양이를 출력하기 위해 문자열을 조합합니다.
            # 각 고양이 사이에 공백을 넣어줍니다.
            if i % 5 == 0 and i != 0: # 5마리마다 줄 바꿈
                cat_display.append("<br>") # HTML 줄바꿈 태그 사용
            cat_display.append(random.choice(cat_emojis))
            
            with cat_container:
                st.markdown(f"<p style='font-size: 24px;'>{' '.join(cat_display)}</p>", unsafe_allow_html=True)
            time.sleep(0.1) # 0.1초 간격으로 고양이 등장
            
        st.balloons() # 고양이 등장 후 풍선 효과 추가

    else:
        st.warning("이름을 먼저 입력해주세요.")
