import streamlit as st

st.set_page_config(page_title="SafeSphere", layout="centered")

# -------------------------
# SESSION SETUP
# -------------------------
if "step" not in st.session_state:
    st.session_state.step = 1

if "user_data" not in st.session_state:
    st.session_state.user_data = {}

if "contacts" not in st.session_state:
    st.session_state.contacts = []

# -------------------------
# STEP 1: BASIC DETAILS
# -------------------------
if st.session_state.step == 1:
    st.title("Step 1: Basic Details")

    name = st.text_input("Name / Nickname")
    age = st.selectbox("Age Range", ["13-15", "16-18", "18-25"])
    city = st.text_input("City")
    language = st.selectbox("Preferred Language", ["English", "Hindi", "Kannada"])

    if st.button("Next →"):
        if city == "":
            st.warning("Enter city")
        else:
            st.session_state.user_data.update({
                "name": name,
                "age": age,
                "city": city,
                "language": language
            })
            st.session_state.step = 2

# -------------------------
# STEP 2: PERSONALIZATION
# -------------------------
elif st.session_state.step == 2:
    st.title("Step 2: Personalization")

    confidence = st.radio("Confidence Level", ["Low", "Medium", "High"])

    fears = st.multiselect(
        "Situations You Fear Most",
        ["Public harassment", "Online threats", "Peer pressure", "Workplace/school pressure"]
    )

    if st.button("Next →"):
        if len(fears) == 0:
            st.warning("Select at least one fear")
        else:
            st.session_state.user_data.update({
                "confidence": confidence,
                "fears": fears
            })
            st.session_state.step = 3

# -------------------------
# STEP 3: EMERGENCY SETUP
# -------------------------
elif st.session_state.step == 3:
    st.title("Step 3: Emergency Setup")

    name = st.text_input("Contact Name")
    phone = st.text_input("Phone Number")

    if st.button("Add Contact"):
        if name and phone:
            st.session_state.contacts.append({
                "name": name,
                "phone": phone
            })

    st.write("### Saved Contacts")
    st.write(st.session_state.contacts)

    share_location = st.checkbox("Share Live Location")
    auto_alert = st.checkbox("Auto-send Alert")

    if st.button("Finish →"):
        if len(st.session_state.contacts) == 0:
            st.warning("Add at least one contact")
        else:
            st.session_state.user_data.update({
                "contacts": st.session_state.contacts,
                "share_location": share_location,
                "auto_alert": auto_alert
            })
            st.session_state.step = 4

# -------------------------
# STEP 4: SOS DASHBOARD
# -------------------------
elif st.session_state.step == 4:
    st.title("🚨 SafeSphere SOS Dashboard")

    user = st.session_state.user_data

    st.subheader("User Info")
    st.json(user)

    # SOS message
    default_msg = f"I need help! I am in {user.get('city')}."
    msg = st.text_area("Emergency Message", default_msg)

    # Alarm
    alarm = st.checkbox("🔊 Enable Alarm")

    # SOS BUTTON
    if st.button("🚨 SEND SOS ALERT", use_container_width=True):

        st.error("🚨 SOS ACTIVATED!")

        st.write("📩 Message Sent:")
        st.code(msg)

        st.write("📞 Contacts Notified:")
        for c in user.get("contacts", []):
            st.write(f"• {c['name']} ({c['phone']})")

        if user.get("share_location"):
            st.success(f"📍 Location Shared: {user.get('city')}")

        if alarm:
            st.warning("🔊 Alarm Playing...")

    # QUICK DIAL PANEL
    st.subheader("📞 Quick Dial")

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("🚔 Police (100)"):
            st.info("Calling 100...")

    with col2:
        if st.button("👩 Helpline (1091)"):
            st.info("Calling 1091...")

    with col3:
        if st.button("🚑 Emergency (112)"):
            st.info("Calling 112...")
