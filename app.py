import streamlit as st
from datetime import datetime, date
import math

st.set_page_config(page_title="생일 D-day 계산기", page_icon="🎂", layout="centered")

st.title("🎂 생일 D-day 계산기")
st.caption("다가오는 생일까지 남은 날짜와 나의 나이를 계산해보세요!")

# 입력 양식
with st.form("birthday_form"):
    name = st.text_input("이름을 입력하세요", value="홍길동")
    birth_date = st.date_input(
        "생년월일을 선택하세요",
        min_value=date(1900, 1, 1),
        max_value=date.today(),
        value=date(2000, 1, 1)
    )
    submitted = st.form_submit_button("D-day 계산하기")

if submitted:
    today = date.today()
    
    # 올해 생일 날짜
    this_year_bday = date(today.year, birth_date.month, birth_date.day)
    
    # 올해 생일이 이미 지났다면 내년 생일로 설정
    if this_year_bday < today:
        next_bday = date(today.year + 1, birth_date.month, birth_date.day)
    else:
        next_bday = this_year_bday
        
    days_left = (next_bday - today).days
    age = today.year - birth_date.year
    
    st.markdown("---")
    
    # 결과 출력
    if days_left == 0:
        st.balloons()
        st.success(f"🎉 **축하합니다! 오늘은 {name}님의 생일입니다!** 🥳")
    else:
        st.metric(label=f"🎁 {name}님의 다음 생일까지", value=f"D-{days_left}일")
        st.info(f"다음 생일: **{next_bday.strftime('%Y년 %m월 %d일')}**")
    
    # 나이 정보
    col1, col2 = st.columns(2)
    with col1:
        st.metric("만 나이", f"{age}세")
    with col2:
        st.metric("태어난 지", f"{(today - birth_date).days:,}일째")
