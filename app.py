import streamlit as st
import threading
import tempfile
from surveillance import SurveillanceSystem

# --- Initialize Stop Event once ---
if 'stop_event_obj' not in st.session_state:
    st.session_state.stop_event_obj = threading.Event()
if 'surveillance_thread' not in st.session_state:
    st.session_state.surveillance_thread = None
if 'video_path' not in st.session_state:
    st.session_state.video_path = None

def run_surveillance(stop_event, video_path):
    system = SurveillanceSystem(
        video_source=video_path if video_path else 0,
        stop_event=stop_event
    )
    system.run()

st.title("🏠 Home Surveillance System with YOLOv8")

# Upload video
uploaded_file = st.file_uploader("📼 Upload video file (or use webcam)", type=["mp4", "avi", "mov"])
if uploaded_file is not None:
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(uploaded_file.read())
    st.session_state.video_path = temp_file.name
    st.success("Video uploaded!")

# Start Surveillance
if st.button("▶ Start Surveillance"):
    if st.session_state.surveillance_thread is None or not st.session_state.surveillance_thread.is_alive():
        st.session_state.stop_event_obj.clear()
        st.session_state.surveillance_thread = threading.Thread(
            target=run_surveillance,
            args=(st.session_state.stop_event_obj, st.session_state.video_path)
        )
        st.session_state.surveillance_thread.start()
        st.success("Surveillance started.")

# Stop Surveillance
if st.button("⏹ Stop Surveillance"):
    st.session_state.stop_event_obj.set()
    st.success("Surveillance stopping...")

