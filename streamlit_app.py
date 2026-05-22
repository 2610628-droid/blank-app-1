import streamlit as st

# 앱 제목 설정
st.title("📦 배송비 및 총 결제금액 안내")
st.write("회원 등급과 주문 금액에 따른 최종 결제 금액을 확인하세요.")
st.write("---")

# 1. 회원 여부 입력 (라디오 버튼 활용)
# 기존 코드의 'y/n' 입력을 예/아니오 선택 방식으로 직관화했습니다.
member = st.radio(
    "정기 회원 여부를 선택해주세요:",
    options=["예 (y)", "아니오 (n)"],
    index=1 # 기본값을 '아니오'로 설정
)

# 2. 주문 금액 입력 (숫자 입력창 활용)
# 만 단위로 쉽게 조절할 수 있도록 step을 10,000원으로 지정했습니다.
total = st.number_input("주문 금액을 입력하세요 (원):", min_value=0, value=0, step=10000)

st.write("---")

# 3. 배송비 계산 및 결과 출력
if total > 0: # 주문 금액이 입력되었을 때만 계산 시작
    shipping_fee = 0
    
    if member == "예 (y)":
        st.success("✨ 정기회원으로 배송비가 면제됩니다!")
    else:
        st.info("🚚 배송비 3,000원이 부과됩니다.")
        shipping_fee = 3000
        total += shipping_fee

    # 최종 금액 강조 출력
    st.subheader("💰 최종 결제 금액")
    st.metric(label="총 금액 (배송비 포함)", value=f"{total:,} 원")
else:
    st.warning("주문 금액을 입력하시면 최종 결제 금액이 표시됩니다.")