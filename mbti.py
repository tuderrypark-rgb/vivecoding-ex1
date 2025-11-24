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
    "ESTP": {"title": "사업가", "desc": "타협을 모르고, 위험을 즐기며, 모험을 즐기는 영리한 사업가입니다.", "icon": "chart line", "color
