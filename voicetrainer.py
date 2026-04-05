import speech_recognition as sr
import audioop
import time

def analyze_voice():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Speak now...")

        recognizer.adjust_for_ambient_noise(source)

        start_time = time.time()

        audio = recognizer.listen(source)

        end_time = time.time()

    # -------------------------
    # SPEECH TO TEXT
    # -------------------------
    try:
        text = recognizer.recognize_google(audio)
        print("\n📝 You said:", text)
    except:
        print("❌ Could not understand audio")
        return

    # -------------------------
    # ANALYZE VOLUME
    # -------------------------
    raw_data = audio.get_raw_data()
    volume = audioop.rms(raw_data, 2)

    # -------------------------
    # ANALYZE PAUSE (approx)
    # -------------------------
    duration = end_time - start_time
    word_count = len(text.split())
    words_per_sec = word_count / duration if duration > 0 else 0

    # -------------------------
    # FEEDBACK LOGIC
    # -------------------------
    print("\n🔍 ANALYSIS:")

    # Volume
    if volume < 300:
        print("🔉 You spoke too softly")
    else:
        print("🔊 Good volume")

    # Speed / pauses
    if words_per_sec < 1.5:
        print("⏳ You spoke slowly or hesitated")
    elif words_per_sec > 3:
        print("⚡ You spoke too fast")
    else:
        print("🗣️ Good speaking pace")

    # Confidence (simple rule-based)
    if volume < 300 or words_per_sec < 1.5:
        print("\n💡 You sounded unsure")
        print("👉 Try speaking louder and more confidently")
    else:
        print("\n✅ You sounded confident!")

# Run
analyze_voice()
