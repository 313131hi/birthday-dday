import streamlit as st
from datetime import datetime, date

st.set_page_config(page_title="생일 D-day 계산기", page_icon="🎂", layout="centered")

st.title("🎂 생일 D-day 계산기")
st.caption("다가오는 생일까지 남은 날짜와 나의 나이를 계산해보세요!")

today = date.today()

# 달력 대신 직관적인 연/월/일 입력 양식으로 변경
with st.form("birthday_form"):
    name = st.text_input("이름을 입력하세요", value="홍길동")
    
    st.write("생년월일을 선택하세요")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # 1900년부터 올해 연도까지 무제한 선택 가능
        year = st.number_input("연도(년)", min_value=1900, max_value=today.year, value=2000, step=1)
    with col2:
        month = st.number_input("월", min_value=1, max_value=12, value=1, step=1)
    with col3:
        day = st.number_input("일", min_value=1, max_value=31, value=1, step=1)
        
    submitted = st.form_submit_button("D-day 계산하기")

if submitted:
    try:
        # 1. 입력받은 연, 월, 일로 날짜 생성
        birth_date = date(year, month, day)
        
        # 2. 미래 날짜 예외 처리
        if birth_date > today:
            st.error("미래의 날짜는 생일로 입력할 수 없습니다!")
        else:
            # 3. 윤년(2월 29일) 예외 처리 및 올해 생일 계산
            try:
                this_year_bday = date(today.year, birth_date.month, birth_date.day)
            except ValueError:
                # 2월 29일 출생자인데, 올해가 평년(28일까지 있는 해)일 경우 2월 28일로 대체
                this_year_bday = date(today.year, 2, 28)
            
            # 4. 올해 생일이 이미 지났다면 내년 생일로 설정
            if this_year_bday < today:
                try:
                    next_bday = date(today.year + 1, birth_date.month, birth_date.day)
                except ValueError:
                    # 내년이 평년일 경우 2월 28일로 대체
                    next_bday = date(today.year + 1, 2, 28)
            else:
                next_bday = this_year_bday
                
            # 5. D-day 및 나이 연산
            days_left = (next_bday - today).days
            age = today.year - birth_date.year
            
            st.markdown("---")
            
            # 6. 결과 출력
            if days_left == 0:
                st.balloons()
                st.success(f"🎉 **축하합니다! 오늘은 {name}님의 생일입니다!** 🥳")
            else:
                st.metric(label=f"🎁 {name}님의 다음 생일까지", value=f"D-{days_left}일")
                st.info(f"다음 생일: **{next_bday.strftime('%Y년 %m월 %d일')}**")
            
            # 7. 나이 정보 (2열 레이아웃)
            res_col1, res_col2 = st.columns(2)
            with res_col1:
                st.metric("만 나이", f"{age}세")
            with res_col2:
                st.metric("태어난 지", f"{(today - birth_date).days:,}일째")
                
    except ValueError:
        # 사용자가 2월 30일, 4월 31일 등 존재하지 않는 날짜를 입력했을 때 에러 방지
        st.error("❌ 유효하지 않은 날짜입니다. (예: 2월 30일 등 달력을 확인해 주세요)")
