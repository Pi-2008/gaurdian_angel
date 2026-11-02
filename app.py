import os
import glob
import time
from datetime import datetime
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Page setup
st.set_page_config(
    page_title="Guardian Angel - Personal Safety Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished Guardian Angel styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.3rem;
        font-weight: 700;
        color: #1f4e8c;
        margin-bottom: 0px;
    }
    .sub-tagline {
        font-size: 1.1rem;
        color: #64748b;
        margin-bottom: 24px;
    }
    .feature-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .sos-badge {
        display: inline-block;
        background: #fee2e2;
        color: #b91c1c;
        padding: 6px 14px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 1rem;
    }
</style>
""", unsafe_allow_html=True)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_file_content(filename):
    filepath = os.path.join(BASE_DIR, filename)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    return ""

# Sidebar navigation
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/shield.png", width=64)
    st.title("Guardian Angel")
    st.caption("You are not alone • Personal Safety Suite")
    st.markdown("---")
    
    page = st.radio(
        "Modules",
        [
            "🏠 Overview",
            "🎨 Rekhachitram (Face Generator)",
            "🗺️ Travel Route Guard",
            "📞 Fake Escort Call",
            "🎙️ Voice Danger Listener",
            "👁️ AI Threat & Person Tracker",
            "🚨 Emergency Contacts & SOS"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 🚨 Emergency SOS")
    st.error("**Emergency Helpline:** [112](tel:112)")
    st.warning("**Women Helpline:** [1091](tel:1091)")
    st.info("**Railway Helpline:** [139](tel:139)")

# ==================== PAGE: OVERVIEW ====================
if page == "🏠 Overview":
    st.markdown('<p class="main-header">🛡️ Guardian Angel</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Comprehensive safety suite: AI facial composite sketcher, journey corridor guard, simulated deterrent calls, voice distress recognition, and AI vision.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### 🎨 Rekhachitram
        Forensic suspect sketch generation powered by Pollinations AI. Select fine-grained facial traits or type custom prompts to render forensic likenesses.
        
        ### 🗺️ Travel Route Guard
        Real-time GPS journey monitor covering all Kerala districts. Geofenced corridor tracking, straight line / OSRM routing, deviation alarms, and audio sirens.
        
        ### 📞 Fake Escort Call
        Simulate an incoming phone call from "Dad" or a "Police Officer" with interactive speech-to-text dialogue to safely deter unwanted attention.
        """)

    with col2:
        st.markdown("""
        ### 🎙️ Voice Danger Listener
        Always-listening browser-based acoustic distress trigger. Detects keywords such as "help", "save me", or "leave me alone" to activate emergency alarms.
        
        ### 👁️ AI Threat Vision Tracker
        YOLOv8 & ByteTrack computer vision pipeline identifying knives, weapons, and untracked individuals with automated snapshot logging.
        
        ### 🚨 Emergency SOS Hotlines
        Direct quick-dial links to 112 (National Emergency), 1091 (Women's Helpline), 139 (Railway Police), and local Kerala emergency services.
        """)

    st.markdown("---")
    st.markdown("### 📊 Status & Detection Archives")
    
    traveller_count = len(glob.glob(os.path.join(BASE_DIR, "travellers", "*.*")))
    danger_count = len(glob.glob(os.path.join(BASE_DIR, "dangerous", "*.*")))
    
    sc1, sc2, sc3, sc4 = st.columns(4)
    with sc1:
        st.metric(label="Safe Corridors", value="Kerala (14 Dists)")
    with sc2:
        st.metric(label="Logged Person Snapshots", value=traveller_count)
    with sc3:
        st.metric(label="Logged Weapon Snapshots", value=danger_count)
    with sc4:
        st.metric(label="Computer Vision Engine", value="YOLOv8 + ByteTrack")

# ==================== PAGE: REKHACHITRAM ====================
elif page == "🎨 Rekhachitram (Face Generator)":
    st.markdown('<p class="main-header">🎨 Rekhachitram — Face Composer</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Compose suspect or missing person likenesses from detailed descriptions, or use the interactive canvas below.</p>', unsafe_allow_html=True)

    tab_interactive, tab_native = st.tabs(["🖌️ Interactive Web Composer", "⚙️ Streamlit Generator"])
    
    with tab_interactive:
        html_code = get_file_content("face-generator.html")
        if html_code:
            components.html(html_code, height=920, scrolling=True)
        else:
            st.warning("face-generator.html not found.")
            
    with tab_native:
        st.subheader("Generate Portrait via AI")
        c1, c2, c3 = st.columns(3)
        with c1:
            style = st.selectbox("Art Style", ["Photorealistic", "Digital illustration", "Pencil sketch", "Oil painting", "3D render"])
            gender = st.selectbox("Gender", ["Woman", "Man", "Non-binary person", "Any"])
            age = st.selectbox("Age Group", ["Child", "Teenager", "Young adult", "Middle-aged", "Elderly", "Any"])
        with c2:
            face_shape = st.selectbox("Face Shape", ["Any", "Oval", "Round", "Square", "Heart-shaped", "Long", "Diamond"])
            skin = st.selectbox("Skin Tone", ["Any", "Very fair", "Fair", "Light olive", "Tan", "Brown", "Dark brown", "Deep ebony"])
            eyes = st.selectbox("Eye Color", ["Any", "Brown", "Blue", "Green", "Hazel", "Gray", "Amber"])
        with c3:
            hair = st.selectbox("Hairstyle", ["Any", "Short crop", "Buzz cut", "Long straight", "Curly", "Bob", "Braids", "Bald"])
            facial_hair = st.selectbox("Facial Hair", ["Any", "Clean shaven", "Stubble", "Full beard", "Goatee", "Mustache"])
            expression = st.selectbox("Expression", ["Neutral", "Smiling", "Serious", "Surprised", "Sad", "Smirking"])
            
        custom_prompt = st.text_area(
            "Custom Prompt / Additional Clues (scars, tattoos, clothing, lighting)",
            placeholder="e.g. scar on left cheek, wearing glasses, dark jacket, dramatic lighting"
        )
        
        if st.button("Generate Face with AI", type="primary"):
            parts = []
            parts.append(f"{style.lower()} portrait photo of a face, front view, head and shoulders")
            if gender != "Any": parts.append(gender.lower())
            if age != "Any": parts.append(age.lower())
            if face_shape != "Any": parts.append(f"{face_shape.lower()} face shape")
            if skin != "Any": parts.append(f"{skin.lower()} skin tone")
            if eyes != "Any": parts.append(f"{eyes.lower()} eyes")
            if hair != "Any": parts.append(f"{hair.lower()} hair")
            if facial_hair != "Any": parts.append(facial_hair.lower())
            if expression != "Any": parts.append(f"{expression.lower()} expression")
            if custom_prompt.strip(): parts.append(custom_prompt.strip())
            parts.append("highly detailed, sharp focus, plain background")
            
            full_prompt = ", ".join(parts)
            st.info(f"**Synthesized Prompt:** {full_prompt}")
            
            seed = int(time.time()) % 1000000
            pollinations_url = f"https://image.pollinations.ai/prompt/{full_prompt}?width=768&height=768&seed={seed}&nologo=true&model=flux"
            
            with st.spinner("Generating composite face..."):
                st.image(pollinations_url, caption="Generated Rekhachitram Likeness", use_container_width=True)
                st.markdown(f"[📥 Direct High-Res Image Link]({pollinations_url})")

# ==================== PAGE: TRAVEL ROUTE GUARD ====================
elif page == "🗺️ Travel Route Guard":
    st.markdown('<p class="main-header">🗺️ Travel Route Guard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Real-time journey tracking with geofence corridor monitoring, deviation simulation, and emergency alert alarms.</p>', unsafe_allow_html=True)
    
    route_html = get_file_content("route.html")
    if route_html:
        components.html(route_html, height=880, scrolling=True)
    else:
        st.warning("route.html not found.")

# ==================== PAGE: FAKE ESCORT CALL ====================
elif page == "📞 Fake Escort Call":
    st.markdown('<p class="main-header">📞 Fake Escort Call Simulator</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Trigger a realistic incoming phone call from "Dad" or a "Police Officer" with spoken dialogue to help exit uncomfortable situations.</p>', unsafe_allow_html=True)
    
    call_html = get_file_content("fake-call.html")
    if call_html:
        components.html(call_html, height=600, scrolling=True)
    else:
        st.warning("fake-call.html not found.")

# ==================== PAGE: VOICE DANGER LISTENER ====================
elif page == "🎙️ Voice Danger Listener":
    st.markdown('<p class="main-header">🎙️ Voice Distress Listener</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Continuous voice listener detecting spoken emergency words ("help", "save me", "stop") to sound alarms and trigger alert sequences.</p>', unsafe_allow_html=True)
    
    voice_html = get_file_content("voice.html")
    if voice_html:
        components.html(voice_html, height=520, scrolling=True)
    else:
        st.warning("voice.html not found.")

# ==================== PAGE: AI THREAT DETECTION ====================
elif page == "👁️ AI Threat & Person Tracker":
    st.markdown('<p class="main-header">👁️ AI Threat & Person Detection</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Powered by YOLOv8 and ByteTrack computer vision models to detect persons and weapons.</p>', unsafe_allow_html=True)
    
    v_tab1, v_tab2 = st.tabs(["🖼️ Image & Video Threat Inspector", "📁 Detection Snapshot Archive"])
    
    with v_tab1:
        st.subheader("Run Instant YOLOv8 Threat Scanner")
        uploaded_file = st.file_uploader("Upload photo to test threat detection (weapons/persons)", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_container_width=True)
            
            conf_thresh = st.slider("Detection Confidence Threshold", min_value=0.1, max_value=1.0, value=0.35, step=0.05)
            
            if st.button("Scan for Threats (YOLOv8)", type="primary"):
                with st.spinner("Analyzing frame with YOLOv8..."):
                    try:
                        from ultralytics import YOLO
                        model_path = os.path.join(BASE_DIR, "yolov8n.pt")
                        if not os.path.exists(model_path):
                            model_path = "yolov8n.pt"
                        
                        model = YOLO(model_path)
                        results = model(image, conf=conf_thresh)
                        res_plotted = results[0].plot()
                        
                        st.success("Analysis complete!")
                        st.image(res_plotted, caption="YOLOv8 Detections", use_container_width=True)
                        
                        detected_classes = [model.names[int(c)] for c in results[0].boxes.cls]
                        st.write(f"**Identified Objects:** {', '.join(set(detected_classes)) if detected_classes else 'None'}")
                        
                        if "knife" in detected_classes or "scissors" in detected_classes:
                            st.error("⚠️ WEAPON / SHARP OBJECT DETECTED IN FRAME!")
                    except Exception as e:
                        st.error(f"Error executing YOLOv8 model: {e}")

    with v_tab2:
        st.subheader("Captured Threat & Traveller Snapshots")
        st.write("Snapshots automatically stored during live tracking:")
        
        col_t, col_d = st.columns(2)
        with col_t:
            st.markdown("#### 👥 Travellers Detected")
            traveller_files = glob.glob(os.path.join(BASE_DIR, "travellers", "*.*"))
            if traveller_files:
                for img_p in traveller_files[-6:]:
                    st.image(img_p, caption=os.path.basename(img_p), use_container_width=True)
            else:
                st.info("No traveller snapshots recorded yet.")
                
        with col_d:
            st.markdown("#### ⚠️ Danger / Threat Detections")
            danger_files = glob.glob(os.path.join(BASE_DIR, "dangerous", "*.*"))
            if danger_files:
                for img_p in danger_files[-6:]:
                    st.image(img_p, caption=os.path.basename(img_p), use_container_width=True)
            else:
                st.info("No threat snapshots recorded yet.")

# ==================== PAGE: EMERGENCY SOS ====================
elif page == "🚨 Emergency Contacts & SOS":
    st.markdown('<p class="main-header">🚨 Emergency Contacts & Support</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-tagline">Immediate emergency assistance, quick-dial contacts, and safety protocols.</p>', unsafe_allow_html=True)
    
    st.error("### ⚠️ Emergency Hotlines (India & Kerala)")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        - **National Emergency Number:** `112`
        - **Women Helpline (Domestic & Public):** `1091` / `181`
        - **Kerala Police Cyber Dome:** `1930`
        - **Child Helpline:** `1098`
        """)
    with c2:
        st.markdown("""
        - **Railway Protection Force (RPF) Security:** `139`
        - **Highway Police Helpline:** `9846 100 100`
        - **Disaster Management (Kerala State):** `1077`
        - **Ambulance:** `108` / `102`
        """)
    
    st.markdown("---")
    st.markdown("### 🔔 Safety Protocol Guidelines")
    st.info("""
    1. **If you deviate from your safe route:** Ensure your mobile GPS remains active. Guardian Angel will sound an alert if deviation exceeds the set perimeter radius.
    2. **In case of immediate threat:** Tap the phone dialer links above or call **112**.
    3. **Face composite generation:** Share generated suspect images promptly with local law enforcement.
    """)
