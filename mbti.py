import streamlit as st
import pandas as pd

# 1. 페이지 기본 설정
st.set_page_config(page_title="MBTI World Map", page_icon="🌍", layout="wide")

# 2. Semantic UI 및 커스텀 CSS 주입
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css">
    <style>
        /* Streamlit 기본 여백 조정 및 Semantic UI와의 조화 */
        .main { background-color: #F9FAFB; }
        .stApp { margin-top: -50px; }
        div.block-container { padding-top: 2rem; }
    </style>
""", unsafe_allow_html=True)

# 3. MBTI 기본 설명 데이터 (수정됨)
mbti_descriptions = {
    "ISTJ": {"title": "현실주의자", "desc": "책임감이 강하고 현실적이며, 매사에 철저하고 보수적입니다.", "icon": "building", "color": "blue"},
    "ISFJ": {"title": "수호자", "desc": "차분하고 헌신적이며, 성실하고 온화한 협조자입니다.", "icon": "shield alternate", "color": "teal"},
    "INFJ": {"title": "옹호자", "desc": "조용하고 신비로우며, 샘솟는 영감으로 지칠 줄 모르는 이상주의자입니다.", "icon": "leaf", "color": "green"},
    "INTJ": {"title": "전략가", "desc": "용의주도하고 독창적이며, 모든 일에 계획을 세우는 전략가입니다.", "icon": "chess", "color": "purple"},
    "ISTP": {"title": "장인", "desc": "과묵하고 분석적이며, 적응력이 강하고 도구를 잘 다루는 만능 재주꾼입니다.", "icon": "wrench", "color": "grey"},
    "ISFP": {"title": "모험가", "desc": "온화하고 겸손하며, 삶의 여유를 만끽하는 진정한 예술가입니다.", "icon": "paint brush", "color": "yellow"},
    "INFP": {"title": "중재자", "desc": "상냥하고 이타적이며, 낭만적인 이상을 꿈꾸는 시인입니다.", "icon": "heart", "color": "green"},
    "INTP": {"title": "논리술사", "desc": "지적 호기심이 높고 잠재력과 가능성을 탐구하는 사색가입니다.", "icon": "lightbulb", "color": "violet"},
    "ESTP": {"title": "사업가", "desc": "타협을 모르고, 위험을 즐기며, 모험을 즐기는 영리한 사업가입니다.", "icon": "chart line", "color": "red"},
    "ESFP": {"title": "연예인", "desc": "사교적이고 활동적이며, 수용적이고 낙천적인 만능 엔터테이너입니다.", "icon": "music", "color": "orange"},
    "ENFP": {"title": "활동가", "desc": "열정적이고 창의적이며, 긍정적인 에너지가 넘치는 재기발랄한 활동가입니다.", "icon": "smile", "color": "orange"},
    "ENTP": {"title": "변론가", "desc": "박학다식하고 독창적이며, 끊임없이 새로운 시도를 하는 논쟁을 즐기는 변론가입니다.", "icon": "comments", "color": "red"},
    "ESTJ": {"title": "경영자", "desc": "구체적이고 현실적이며, 사실적이고 활동을 조직화하는 지도자입니다.", "icon": "sitemap", "color": "blue"},
    "ESFJ": {"title": "집정관", "desc": "사교적이고 친절하며, 타인에 대한 관심과 배려가 넘치는 인기쟁이입니다.", "icon": "users", "color": "teal"},
    "ENFJ": {"title": "선도자", "desc": "카리스마와 충만한 열정을 지닌 타고난 리더입니다.", "icon": "sun", "color": "yellow"},
    "ENTJ": {"title": "통솔자", "desc": "대담하고 상상력이 풍부하며, 강력한 의지로 무리(조직)를 이끄는 지도자입니다.", "icon": "bullhorn", "color": "black"}
}

# 4. 데이터 로드 함수
@st.cache_data
def load_data():
    try:
        # 파일 경로 확인 필요 (같은 폴더에 있는지)
        df = pd.read_csv('countriesMBTI_16types.csv')
        return df
    except FileNotFoundError:
        return None

def main():
    # --- 헤더 영역 (Semantic UI Header) ---
    st.markdown("""
        <div class="ui center aligned icon header" style="margin-top: 20px;">
            <i class="circular globe icon teal"></i>
            Global MBTI Report
            <div class="sub header">데이터로 알아보는 당신의 성향이 가장 환영받는 국가</div>
        </div>
        <div class="ui divider"></div>
    """, unsafe_allow_html=True)

    # 데이터 불러오기
    df = load_data()
    if df is None:
        st.error("데이터 파일(countriesMBTI_16types.csv)을 찾을 수 없습니다.")
        return

    # MBTI 선택 (중앙 정렬을 위해 컬럼 사용)
    col_spacer_l, col_select, col_spacer_r = st.columns([1, 2, 1])
    with col_select:
        selected_mbti = st.selectbox(
            "나의 MBTI 유형 선택",
            options=list(mbti_descriptions.keys()),
            index=None,
            placeholder="👇 여기를 눌러 MBTI를 선택하세요"
        )

    # --- 선택 전/후 분기 처리 ---
    if selected_mbti is None:
        # 초기 화면: Semantic UI Info Message
        st.markdown("""
            <div class="ui container" style="margin-top: 30px;">
                <div class="ui icon message info">
                    <i class="hand point up outline icon"></i>
                    <div class="content">
                        <div class="header">
                            MBTI를 선택해주세요!
                        </div>
                        <p>상단 메뉴에서 유형을 선택하면, 전 세계 통계 정보를 분석하여 보여드립니다.</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    else:
        # 선택 후 화면
        info = mbti_descriptions[selected_mbti]
        
        # A. MBTI 설명 카드 (Semantic UI Segment & Header)
        st.markdown(f"""
            <div class="ui container" style="margin-top: 20px;">
                <div class="ui segment raised {info['color']}">
                    <h2 class="ui header">
                        <i class="{info['icon']} icon"></i>
                        <div class="content">
                            {selected_mbti} : {info['title']}
                            <div class="sub header">{info['desc']}</div>
                        </div>
                    </h2>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # 데이터 분석
        # 해당 MBTI 컬럼이 존재하는지 확인
        if selected_mbti in df.columns:
            sorted_df = df.sort_values(by=selected_mbti, ascending=False).head(10)
            top_country = sorted_df.iloc[0]['Country']
            top_value = sorted_df.iloc[0][selected_mbti] * 100
            
            # B. 통계 및 멘트 (Semantic UI Statistics & Message)
            col1, col2 = st.columns([1, 1.5])

            with col1:
                st.markdown(f"""
                    <div class="ui card fluid">
                        <div class="content">
                            <div class="header">🏆 Best Match Country</div>
                        </div>
                        <div class="content">
                            <div class="ui tiny statistic">
                                <div class="value">
                                    <i class="map marker alternate icon red"></i> {top_country}
                                </div>
                                <div class="label">
                                    가장 높은 비율
                                </div>
                            </div>
                            <div class="ui divider"></div>
                            <div class="ui huge statistic">
                                <div class="value">
                                    {top_value:.1f}%
                                </div>
                                <div class="label">
                                    인구 비율
                                </div>
                            </div>
                        </div>
                        <div class="extra content">
                            <div class="ui info message">
                                <p><b>"당신을 위한 추천 멘트"</b><br>
                                {top_country}의 거리는 당신과 같은 {selected_mbti}의 에너지로 가득 차 있습니다. 
                                이곳에서라면 마음이 통하는 소울메이트를 더 쉽게 만날 수 있을 거예요!</p>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                    <div class="ui top attached label teal">🌐 국가별 {selected_mbti} 비율 Top 10</div>
                """, unsafe_allow_html=True)
                
                chart_data = sorted_df.set_index('Country')[selected_mbti]
                st.bar_chart(chart_data, color="#00B5AD")
        else:
            st.error(f"데이터 파일에 '{selected_mbti}' 컬럼이 없습니다.")

if __name__ == "__main__":
    main()
