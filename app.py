import streamlit as st
import random

st.set_page_config(
    page_title="오늘 저녁 메뉴 추천기",
    page_icon="🍽️",
    layout="wide"
)

st.title("🍽️ 오늘 저녁 메뉴 추천기")
st.write("메뉴 고민 시간을 줄여주는 고3 맞춤형 저녁 추천 앱")

with st.sidebar:
    st.header("사용자 정보")

    mood = st.text_input(
        "현재 기분",
        placeholder="예) 피곤함, 배고픔"
    )

    food_type = st.selectbox(
        "음식 종류",
        ["한식", "양식", "중식", "분식"]
    )

    hungry = st.slider(
        "배고픔 정도",
        1, 10, 5
    )

    spicy = st.slider(
        "맵기 선호도",
        1, 10, 5
    )

    allergy = st.multiselect(
        "알레르기",
        ["우유", "계란", "밀", "새우", "땅콩"]
    )

    ingredients = st.multiselect(
        "냉장고 재료",
        ["김치", "치즈", "계란", "라면", "햄", "떡"]
    )

menu_data = {
    "한식": [
        {"name":"김치볶음밥","cal":650,"protein":18,"time":"10분","allergy":["계란"]},
        {"name":"제육볶음","cal":750,"protein":30,"time":"20분","allergy":[]},
        {"name":"부대찌개","cal":700,"protein":25,"time":"15분","allergy":["우유"]}
    ],

    "양식": [
        {"name":"파스타","cal":600,"protein":20,"time":"15분","allergy":["밀","우유"]},
        {"name":"피자","cal":850,"protein":25,"time":"30분","allergy":["밀","우유"]},
        {"name":"햄버거","cal":780,"protein":28,"time":"15분","allergy":["밀","계란"]}
    ],

    "중식": [
        {"name":"짜장면","cal":700,"protein":15,"time":"15분","allergy":["밀"]},
        {"name":"짬뽕","cal":680,"protein":20,"time":"15분","allergy":["새우"]},
        {"name":"마라탕","cal":750,"protein":22,"time":"20분","allergy":["땅콩"]}
    ],

    "분식": [
        {"name":"떡볶이","cal":550,"protein":10,"time":"10분","allergy":[]},
        {"name":"라볶이","cal":700,"protein":15,"time":"10분","allergy":["밀"]},
        {"name":"김밥","cal":450,"protein":12,"time":"15분","allergy":["계란"]}
    ]
}

def recommend_menu():

    menus = []

    for menu in menu_data[food_type]:

        blocked = False

        for item in allergy:
            if item in menu["allergy"]:
                blocked = True

        if not blocked:
            menus.append(menu)

    if len(menus) == 0:
        return None

    return random.choice(menus)

if st.button("🍴 추천 받기", use_container_width=True):

    menu = recommend_menu()

    if menu is None:

        st.error("추천 가능한 메뉴가 없습니다.")

    else:

        st.success(f"오늘의 추천 메뉴 : {menu['name']}")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "칼로리",
            f"{menu['cal']} kcal"
        )

        col2.metric(
            "단백질",
            f"{menu['protein']} g"
        )

        col3.metric(
            "조리시간",
            menu["time"]
        )

        st.subheader("입력 정보")

        st.write(f"😊 기분 : {mood}")
        st.write(f"🔥 배고픔 : {hungry}/10")
        st.write(f"🌶️ 맵기 : {spicy}/10")

        if allergy:
            st.write("⚠️ 알레르기 :", ", ".join(allergy))

        if ingredients:
            st.write("🧀 냉장고 재료 :", ", ".join(ingredients))

        st.info(
            "알레르기 재료가 포함된 메뉴는 자동으로 제외되었습니다."
        )

        st.balloons()

st.divider()

st.subheader("📌 앱 소개")

st.write("""
이 앱은 고등학생들이 야간자율학습이나 학원 후
'오늘 저녁 뭐 먹지?'라는 고민을 빠르게 해결할 수 있도록 제작되었습니다.

✔ 기분 반영
✔ 알레르기 고려
✔ 영양 정보 제공
✔ 빠른 메뉴 추천
""")