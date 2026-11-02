import os
import glob
import time
from datetime import datetime
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

# Page setup
st.set_page_config(
    page_title="Guardian Angel — Travel Safety Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for polished Guardian Angel styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1e3a8a;
        margin-bottom: 2px;
        letter-spacing: -0.5px;
    }
    .sub-title {
        font-size: 1.15rem;
        color: #475569;
        margin-bottom: 24px;
    }
    .pillar-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 22px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .pillar-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
    }
    .pillar-icon {
        font-size: 2.2rem;
        margin-bottom: 10px;
    }
    .pillar-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
    }
    .pillar-desc {
        font-size: 0.95rem;
        color: #64748b;
        line-height: 1.5;
        min-height: 70px;
    }
    .sos-badge {
        display: inline-block;
        background: #fee2e2;
        color: #991b1b;
        padding: 6px 14px;
        border-radius: 999px;
        font-weight: 700;
        font-size: 0.95rem;
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
    st.caption("AI-Powered Personal & Public Travel Safety")
    st.markdown("---")
    
    page = st.radio(
        "Safety Modules",
        [
            "🏠 Overview & Command Center",
            "🎨 Perpetrator Face Generator",
            "📞 Police Intimidation Fake Call",
            "🗺️ Anti-Kidnapping Route Checker",
            "🚌 Bus Passenger Manifest Tracker",
            "🎙️ Voice Distress Listener",
            "🚨 Emergency Contacts & SOS"
        ],
        index=0
    )
    
    st.markdown("---")
    st.markdown("### 🚨 Emergency SOS")
    st.error("**Emergency Services:** [112](tel:112)")
    st.warning("**Women's Helpline:** [1091](tel:1091)")
    st.info("**Railway Police:** [139](tel:139)")

# ==================== PAGE: OVERVIEW ====================
if page == "🏠 Overview & Command Center":
    st.markdown('<p class="main-title">🛡️ Guardian Angel — Travel Safety Suite</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">A complete multi-tier personal defense and travel safety platform designed to deter threats, track public transport passengers, and provide immediate anti-abduction alerts.</p>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">🎨</div>
            <div class="pillar-title">1. Perpetrator Face Generator (Rekhachitram)</div>
            <div class="pillar-desc">
                Generate detailed forensic likenesses and composite sketches of criminals or suspicious individuals from memory, based on specific facial traits, scars, age, and style.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">📞</div>
            <div class="pillar-title">2. Police Intimidation Fake Call</div>
            <div class="pillar-desc">
                Deter stalkers and creeps around you by triggering a realistic incoming call from an authoritative police sub-inspector or 112 dispatch, playing spoken radio audio to make it clear you are being monitored.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">🗺️</div>
            <div class="pillar-title">3. Anti-Kidnapping Route Checker</div>
            <div class="pillar-desc">
                Monitor your journey corridor in real-time. If your bus, taxi, or auto-rickshaw veers away from the planned route, loud anti-abduction sirens activate and emergency alerts trigger.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="pillar-card">
            <div class="pillar-icon">🚌</div>
            <div class="pillar-title">4. Bus Passenger Manifest Tracker</div>
            <div class="pillar-desc">
                Computer vision program deployed at the bus entrance. Automatically logs every boarding passenger's photo, timestamp, and unique track ID into a manifest file to deter transit crimes.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("📊 Live System Dashboard & Activity")
    
    manifest_path = os.path.join(BASE_DIR, "bus_manifest.csv")
    passenger_count = 0
    if os.path.exists(manifest_path):
        try:
            m_df = pd.read_csv(manifest_path)
            passenger_count = len(m_df)
        except Exception:
            passenger_count = 0

    danger_count = len(glob.glob(os.path.join(BASE_DIR, "dangerous", "*.*")))
    
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Safe Corridors Active", value="14 Kerala Districts")
    with m2:
        st.metric(label="Passengers Logged to Manifest", value=passenger_count)
    with m3:
        st.metric(label="Threat Snapshots Captured", value=danger_count)
    with m4:
        st.metric(label="AI Vision Backbone", value="YOLOv8 + ByteTrack")

# ==================== PAGE: PERPETRATOR FACE GENERATOR ====================
elif page == "🎨 Perpetrator Face Generator":
    st.markdown('<p class="main-title">🎨 Rekhachitram — Criminal & Suspect Face Generator</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Generate high-fidelity forensic composite sketches of perpetrators, suspects, or missing persons from witness and victim descriptions.</p>', unsafe_allow_html=True)

    tab_interactive, tab_native = st.tabs(["🖌️ Interactive Forensic Composer", "⚙️ Guided Attribute Generator"])
    
    with tab_interactive:
        html_code = get_file_content("face-generator.html")
        if html_code:
            components.html(html_code, height=920, scrolling=True)
        else:
            st.warning("face-generator.html not found.")
            
    with tab_native:
        st.subheader("Generate Perpetrator Likeness via AI")
        c1, c2, c3 = st.columns(3)
        with c1:
            style = st.selectbox("Composite Style", ["Pencil sketch (Forensic Police)", "Photorealistic", "Digital illustration", "Oil painting", "3D render"])
            gender = st.selectbox("Perpetrator Gender", ["Man", "Woman", "Non-binary person", "Any"])
            age = st.selectbox("Estimated Age", ["Young adult (20-30)", "Teenager (15-19)", "Middle-aged (35-50)", "Elderly (55+)", "Any"])
        with c2:
            face_shape = st.selectbox("Face Shape", ["Any", "Oval", "Round", "Square", "Heart-shaped", "Long", "Diamond"])
            skin = st.selectbox("Skin Tone / Complexion", ["Any", "Tan", "Brown", "Dark brown", "Light olive", "Fair", "Very fair", "Deep ebony"])
            eyes = st.selectbox("Eye Characteristics", ["Any", "Dark brown", "Black", "Hooded", "Deep-set", "Almond", "Light colored"])
        with c3:
            hair = st.selectbox("Hairstyle", ["Any", "Short crop", "Buzz cut", "Messy wavy", "Curly", "Bald", "Long straight"])
            facial_hair = st.selectbox("Facial Hair", ["Any", "Stubble", "Full beard", "Mustache", "Goatee", "Clean shaven"])
            expression = st.selectbox("Facial Expression", ["Serious", "Intimidating/Aggressive", "Neutral", "Smirking", "Suspicious"])
            
        custom_prompt = st.text_area(
            "Distinct Identifying Marks (Scars, Tattoos, Eyewear, Piercings, Clothing)",
            placeholder="e.g. deep scar on right eyebrow, wearing black jacket and glasses, prominent cheekbones"
        )
        
        if st.button("Generate Suspect Sketch", type="primary"):
            parts = []
            if "sketch" in style.lower():
                parts.append("forensic police pencil sketch portrait of suspect, front facing, police bulletin criminal composite")
            else:
                parts.append(f"{style.lower()} portrait of a suspect, front view, police file format")
                
            if gender != "Any": parts.append(gender.lower())
            if age != "Any": parts.append(age.split('(')[0].strip().lower())
            if face_shape != "Any": parts.append(f"{face_shape.lower()} face")
            if skin != "Any": parts.append(f"{skin.lower()} skin")
            if eyes != "Any": parts.append(f"{eyes.lower()} eyes")
            if hair != "Any": parts.append(f"{hair.lower()} hair")
            if facial_hair != "Any": parts.append(facial_hair.lower())
            if expression != "Any": parts.append(f"{expression.lower()} expression")
            if custom_prompt.strip(): parts.append(custom_prompt.strip())
            parts.append("sharp facial features, criminal lineup background, high detail")
            
            full_prompt = ", ".join(parts)
            st.info(f"**Synthesized Forensic Description:** {full_prompt}")
            
            seed = int(time.time()) % 1000000
            pollinations_url = f"https://image.pollinations.ai/prompt/{full_prompt}?width=768&height=768&seed={seed}&nologo=true&model=flux"
            
            with st.spinner("Rendering suspect composite image..."):
                st.image(pollinations_url, caption="Generated Rekhachitram Suspect Likeness", use_container_width=True)
                st.markdown(f"[📥 Download High-Resolution Composite Sketch]({pollinations_url})")

# ==================== PAGE: POLICE INTIMIDATION FAKE CALL ====================
elif page == "📞 Police Intimidation Fake Call":
    st.markdown('<p class="main-title">📞 Police Intimidation & Deterrent Call</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Intimidate creeps or harassers around you by staging a loud, realistic incoming call from a Police Sub-Inspector or 112 Control Room tracking your live GPS.</p>', unsafe_allow_html=True)
    
    call_html = get_file_content("fake-call.html")
    if call_html:
        components.html(call_html, height=720, scrolling=True)
    else:
        st.warning("fake-call.html not found.")

# ==================== PAGE: ANTI-KIDNAPPING ROUTE CHECKER ====================
elif page == "🗺️ Anti-Kidnapping Route Checker":
    st.markdown('<p class="main-title">🗺️ Anti-Kidnapping Route Corridor Checker</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Protects you against unauthorized route diversions and abductions. If your vehicle strays outside the safety corridor, loud anti-kidnapping sirens sound and emergency protocols activate.</p>', unsafe_allow_html=True)
    
    route_html = get_file_content("route.html")
    if route_html:
        components.html(route_html, height=880, scrolling=True)
    else:
        st.warning("route.html not found.")

# ==================== PAGE: BUS PASSENGER MANIFEST TRACKER ====================
elif page == "🚌 Bus Passenger Manifest Tracker":
    st.markdown('<p class="main-title">🚌 Bus Passenger Manifest & Entry Tracker</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Automated computer vision tracker that monitors bus boarding doors, logs every passenger to a manifest file, and saves high-resolution portraits to establish biometric accountability.</p>', unsafe_allow_html=True)

    tab_cam, tab_data = st.tabs(["📹 Live Entrance Camera & Detection", "📋 Manifest Records & Analysis"])

    with tab_cam:
        bus_html = get_file_content("bus-passenger.html")
        if bus_html:
            components.html(bus_html, height=920, scrolling=True)
        else:
            st.warning("bus-passenger.html not found.")

    with tab_data:
        manifest_path = os.path.join(BASE_DIR, "bus_manifest.csv")
        threat_path = os.path.join(BASE_DIR, "threat_alerts.csv")

        p_col1, p_col2 = st.columns([1, 1])
        with p_col1:
            st.markdown("### 📋 How the Bus Tracker Works")
            st.markdown("""
            1. **Doorway Camera Monitoring:** A camera mounted above the bus entrance continuously tracks passengers entering.
            2. **Unique Persistent Tracking:** YOLOv8 + ByteTrack assigns a persistent track ID so passengers are not double-counted.
            3. **Dual Image Capture:** For every passenger, both a **full-frame entry photo** and a **cropped face/bust portrait** are saved in `travellers/`.
            4. **Structured Manifest File:** Details are saved directly to `bus_manifest.csv`.
            5. **Concealed Weapon Alarm:** If someone boards with an open blade or weapon, it triggers an instant alert saved to `threat_alerts.csv`.
            """)
            st.info("💡 **Run the Python OpenCV Tracker:** Run `python traveller_tracker.py` in your terminal for GPU-accelerated local camera logging.")

        with p_col2:
            st.markdown("### 🧪 Instant Image Passenger & Threat Tester")
            test_file = st.file_uploader("Upload bus entrance photo to test passenger/weapon logging", type=["jpg", "jpeg", "png"])
            if test_file is not None:
                img = Image.open(test_file)
                st.image(img, caption="Uploaded Bus Entrance Frame", use_container_width=True)
                if st.button("Run YOLOv8 Bus Entrance Scan", type="primary"):
                    with st.spinner("Analyzing entry frame..."):
                        try:
                            from ultralytics import YOLO
                            model_path = os.path.join(BASE_DIR, "yolov8n.pt")
                            if not os.path.exists(model_path): model_path = "yolov8n.pt"
                            model = YOLO(model_path)
                            res = model(img, conf=0.35)[0]
                            st.image(res.plot(), caption="Detected Persons & Objects", use_container_width=True)
                            classes = [model.names[int(c)] for c in res.boxes.cls]
                            st.write(f"**Detected in Entry Frame:** {', '.join(set(classes)) if classes else 'None'}")
                            if "knife" in classes:
                                st.error("🚨 DANGER: Weapon / Knife detected on boarding passenger!")
                        except Exception as e:
                            st.error(f"Error: {e}")

        st.markdown("---")
        st.subheader("📁 Bus Passenger Manifest Records (`bus_manifest.csv`)")

        if os.path.exists(manifest_path):
            try:
                df = pd.read_csv(manifest_path)
                if not df.empty:
                    st.dataframe(df, use_container_width=True)
                    csv_bytes = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download Passenger Manifest (CSV)",
                        data=csv_bytes,
                        file_name="bus_passenger_manifest.csv",
                        mime="text/csv"
                    )
                else:
                    st.info("Manifest file is initialized but no passenger entries have been recorded yet.")
            except Exception as e:
                st.warning(f"Unable to read bus_manifest.csv: {e}")
        else:
            st.info("No bus_manifest.csv found. Run `python traveller_tracker.py` to start logging passengers.")

        st.markdown("---")
        st.subheader("👥 Boarded Passenger Photo Gallery (`travellers/`)")
        traveller_files = glob.glob(os.path.join(BASE_DIR, "travellers", "*.*"))
        if traveller_files:
            st.caption(f"Showing {len(traveller_files)} saved passenger entry captures:")
            cols = st.columns(4)
            for i, img_path in enumerate(traveller_files[-12:]):
                with cols[i % 4]:
                    st.image(img_path, caption=os.path.basename(img_path), use_container_width=True)
        else:
            st.info("No passenger portrait captures found yet in travellers/ folder.")

# ==================== PAGE: VOICE DISTRESS LISTENER ====================
elif page == "🎙️ Voice Distress Listener":
    st.markdown('<p class="main-title">🎙️ Voice Distress & Keyword Listener</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Hands-free emergency activation. Continuously monitors for emergency phrases ("help", "save me", "leave me alone") to trigger flashing distress alarms and voice deterrents.</p>', unsafe_allow_html=True)
    
    voice_html = get_file_content("voice.html")
    if voice_html:
        components.html(voice_html, height=520, scrolling=True)
    else:
        st.warning("voice.html not found.")

# ==================== PAGE: EMERGENCY SOS ====================
elif page == "🚨 Emergency Contacts & SOS":
    st.markdown('<p class="main-title">🚨 Emergency Contacts & Safety Protocols</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Direct emergency hotlines and protocol guidelines for immediate threat response.</p>', unsafe_allow_html=True)
    
    st.error("### ⚠️ Primary Emergency Numbers (India & Kerala)")
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        - **National Emergency Unified Number:** `112`
        - **Women Helpline (24/7):** `1091` / `181`
        - **Kerala Police Cyber Crime:** `1930`
        - **Childline Helpline:** `1098`
        """)
    with c2:
        st.markdown("""
        - **Railway Protection Force (RPF):** `139`
        - **Kerala Highway Police Alert:** `9846 100 100`
        - **State Disaster Helpline:** `1077`
        - **Medical Emergency / Ambulance:** `108` / `102`
        """)
    
    st.markdown("---")
    st.markdown("### 🛡️ How These 4 Safety Features Work Together:")
    st.info("""
    - **Step 1 (Pre-Boarding / Waiting):** Use the **Police Intimidation Fake Call** if anyone approaches or looks suspicious at an isolated stop.
    - **Step 2 (Boarding Public Transit):** The **Bus Passenger Manifest Tracker** records every passenger's face and entry timestamp to a file so nobody can commit a crime anonymously.
    - **Step 3 (In Transit):** Enable the **Anti-Kidnapping Route Checker** to ensure the driver does not divert from your designated route.
    - **Step 4 (Post-Incident / Investigation):** If an incident occurs, use **Rekhachitram** to compose a detailed forensic sketch of the perpetrator to assist law enforcement.
    """)
