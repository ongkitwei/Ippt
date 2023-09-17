import streamlit as st
import data

st.set_page_config(layout="centered",
                   page_title="IPPT calculator")
st.title("Ippt Calculator")
option = st.selectbox("Choose Age:",
                        (data.get_age())
)
print(option)
print(type(option))

col1,colmid,col2= st.columns([3,5,3])
with col1:
    st.image("Images/pushup.png", width=230)
    pushup_reps = st.number_input(label="Pushup reps", step=1, min_value=0, key="pushup_reps_key")
    print(pushup_reps)

with col2:
    st.image("Images/situp.png", width=230)
    situp_reps = st.number_input(label="Situp reps", step=1, min_value=0, key="situp_reps_key")



col3,col4,col5 = st.columns(3)
with col4:
    st.image("Images/running.png", width=230)

col6L, col6, col7, col7R = st.columns([0.65,1,1,0.65])
minutes = col6.number_input("Minutes", min_value=0, max_value=59, step=1, key="run_time_minutes_key")
seconds = col7.number_input("Seconds", min_value=0, max_value=59, step=1, key="run_time_seconds_key")

st.write("")
st.write("")
colb1, colb2,colb3 = st.columns([1,1.5,1])
calculate_button = colb2.button(label="CALCULATE",use_container_width=True)

if pushup_reps:
    print(type(pushup_reps))
    with col1:
        st.write(f'<b>{str(data.get_pushup_points(pushup_reps, age=option.strip()))} points</b>', unsafe_allow_html=True)

if situp_reps:
    with col2:
        st.write(f'<b>{str(data.get_situp_points(situp_reps, option))} points</b>', unsafe_allow_html=True)

if minutes or seconds:
    print(type(minutes))
    print(type(seconds))
    with col6:
        st.write(f'<b>{str(data.get_running_points(minutes, seconds, option))} points</b>', unsafe_allow_html=True)
        # st.write(minutes)
        # st.write(seconds)

if calculate_button:
    pushup_points = data.get_pushup_points(pushup_reps, age=option.strip())
    situp_points = data.get_situp_points(situp_reps, option)
    run_points = data.get_running_points(minutes, seconds, option)
    total_points = pushup_points + situp_points + run_points
    # total_points = float(pushup_points) + float(situp_points) + float(run_points)
    # st.info(f'You did {pushup_reps} and it gave you {pushup_points} points')
    # st.info(f'You did {situp_reps} and it gave you {situp_points} points')
    print(type(pushup_points))
    print(type(situp_points))
    print(type(run_points))
    st.info(f"Total: {total_points}")
    if total_points >= 51:
        st.info("Result: Pass")
    else:
        st.info("Result: Fail")
