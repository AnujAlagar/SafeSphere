import streamlit as st

st.title("🚨 SOS Emergency System")

# ---------------------------
# Pre-written SOS Message
# ---------------------------
message = "I need help! Please contact me immediately."

st.subheader("Emergency Message")
custom_msg = st.text_area("Edit message (optional)", message)

# ---------------------------
# Location (SIMULATED)
# ---------------------------
st.subheader("📍 Location")

location = st.text_input("Enter your current location (for demo)", "Bangalore")

# ---------------------------
# Alarm Toggle
# ---------------------------
alarm = st.checkbox("🔊 Enable Loud Alarm")

if alarm:
    st.warning("ALARM ACTIVATED 🚨 (Simulated)")

# ---------------------------
# SOS BUTTON
# ---------------------------
if st.button("🚨 SEND SOS ALERT", use_container_width=True):

    st.error("🚨 SOS ALERT TRIGGERED!")

    # Simulated sending
    st.write("📩 Sending message:")
    st.code(f"{custom_msg}\nLocation: {location}")

    # Simulated contacts
    contacts = ["Mom: 9876543210", "Friend: 9123456780"]

    st.write("📞 Alert sent to:")
    for c in contacts:
        st.write("•", c)

    if alarm:
        st.warning("🔊 Alarm Sound Playing...")

# ---------------------------
# QUICK DIAL PANEL
# ---------------------------
st.subheader("📞 Quick Emergency Dial")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Police 🚔"):
        st.info("Dialing 100... (Simulated)")

with col2:
    if st.button("Women Helpline 👩"):
        st.info("Dialing 1091... (Simulated)")

with col3:
    if st.button("Emergency 🚑"):
        st.info("Dialing 112... (Simulated)")
