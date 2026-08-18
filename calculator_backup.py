import streamlit as st

# -----------------------------
# INITIAL SETUP
# -----------------------------

if "page" not in st.session_state:
    st.session_state.page = 1

if "name" not in st.session_state:
    st.session_state.name = ""

if "numbers" not in st.session_state:
    st.session_state.numbers = []


# -----------------------------
# SCREEN 1: INTRODUCTION
# -----------------------------

if st.session_state.page == 1:

    st.title("👋 Hey there! Welcome!")

    st.write("I'm Emmanuel's little calculation assistant.")
    st.write("Before we begin, I'd like to know who I'm working with.")

    name = st.text_input("What's your name?")

    if st.button("Continue →"):

        if name.strip() == "":
            st.warning("Please enter your name first.")

        else:
            st.session_state.name = name
            st.session_state.page = 2
            st.rerun()


# -----------------------------
# SCREEN 2: WELCOME
# -----------------------------

elif st.session_state.page == 2:

    st.title(f"🎉 Hi, {st.session_state.name}!")

    st.write("Welcome to Emmanuel's Calculations Site. 🧮")

    st.write(
        "In this session, we're going to calculate "
        "the average of four numbers."
    )

    st.write(
        "I'll guide you through it one number at a time, "
        "so you don't have to worry about the mathematics."
    )

    st.write("🚀 Ready to dive in?")

    if st.button("Let's Go! 🚀"):

        st.session_state.numbers = []
        st.session_state.page = 3
        st.rerun()


# -----------------------------
# SCREEN 3: NUMBER 1
# -----------------------------

elif st.session_state.page == 3:

    st.title("🔢 Number 1 of 4")

    st.write("Let's get our first number.")

    number = st.number_input(
        "Enter your first number:",
        key="number_1"
    )

    if st.button("Next →"):

        st.session_state.numbers.append(number)
        st.session_state.page = 4
        st.rerun()


# -----------------------------
# SCREEN 4: NUMBER 2
# -----------------------------

elif st.session_state.page == 4:

    st.title("🔢 Number 2 of 4")

    st.write("Great! Now let's get the second number.")

    number = st.number_input(
        "Enter your second number:",
        key="number_2"
    )

    if st.button("Next →"):

        st.session_state.numbers.append(number)
        st.session_state.page = 5
        st.rerun()


# -----------------------------
# SCREEN 5: NUMBER 3
# -----------------------------

elif st.session_state.page == 5:

    st.title("🔢 Number 3 of 4")

    st.write("You're doing great! Just two more numbers.")

    number = st.number_input(
        "Enter your third number:",
        key="number_3"
    )

    if st.button("Next →"):

        st.session_state.numbers.append(number)
        st.session_state.page = 6
        st.rerun()


# -----------------------------
# SCREEN 6: NUMBER 4
# -----------------------------

elif st.session_state.page == 6:

    st.title("🔢 Number 4 of 4")

    st.write("Last one! Give me your fourth number.")

    number = st.number_input(
        "Enter your fourth number:",
        key="number_4"
    )

    if st.button("Calculate Average 🧮"):

        st.session_state.numbers.append(number)
        st.session_state.page = 7
        st.rerun()


# -----------------------------
# SCREEN 7: RESULT
# -----------------------------

elif st.session_state.page == 7:

    st.title("🎯 We've got your answer!")

    numbers = st.session_state.numbers

    total = sum(numbers)
    average = total / len(numbers)

    st.write(
        f"Well done, {st.session_state.name}! 🎉"
    )

    st.write("You entered:")

    for number in numbers:
        st.write(f"• {number}")

    st.write(f"### Your average is: **{average}**")

    st.success("Calculation completed successfully! ✅")

    if st.button("🔄 Calculate Again"):

        st.session_state.numbers = []
        st.session_state.page = 3
        st.rerun()
