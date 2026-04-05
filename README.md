# SafeSphere( ONGOING )
An AI-powered real-life scenario simulator designed to help users build safety awareness, confidence, and decision-making skills through interactive learning and emergency support features.

**Overview**

SafeSphere is a safety-focused application that simulates real-world situations and trains users to respond effectively.
It combines scenario-based learning, personalization, and an SOS emergency system to provide a comprehensive safety solution.

**Key Features**

🎮 Scenario-Based Learning

Interactive real-life situations (e.g., harassment, online threats, peer pressure)
Multiple decision options with different outcomes
Helps users understand consequences of actions

🤖 AI-Based Feedback

Provides feedback on user decisions
Suggests safer alternatives
Assigns risk levels (safe / risky / dangerous)

🎤 Voice Confidence Trainer (Planned)

Analyze tone, hesitation, and confidence
Suggest improvements for assertive communication

🧠 Personalization System

Collects user preferences:
Confidence level
Fear-based situations
Customizes scenarios accordingly

🚨 SOS Emergency System

One-click SOS alert
Sends emergency message to trusted contacts
Includes location data
Loud alarm simulation
Integrated with Twilio API for real SMS alerts

📞 Emergency Contacts

Add multiple trusted contacts
Used during SOS activation

📍 Location Support

Retrieves approximate user location (IP-based)
Can open location in Google Maps

📊 Growth Tracker (Planned)

Tracks confidence and decision-making improvement over time
📞 Quick Emergency Dial (India)
🚔 Police: 100
👩 Women Helpline: 1091
🚑 Emergency: 112

**Tech Stack**

Frontend/UI: Python (Streamlit)
Backend Logic: Python
API Integration: Twilio (SMS alerts)
Location Services: IP-based location API

**How It Works**

User completes onboarding:
Basic details
Personalization inputs
Emergency contacts
User accesses SOS dashboard
On pressing SOS:
Message is generated
Location is fetched
SMS is sent to contacts
