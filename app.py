import streamlit as st
import opencv-python.cv2 as cv2
import numpy as np
from ball_tracker import track_ball
from pages.rules import show_rules_page
from pages.techniques import show_techniques_page
from pages.drills import show_drills_page
from pages.mental_game import show_mental_game_page

# Set page config
st.set_page_config(
    page_title="Table Tennis Trainer",
    page_icon="🏓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Ball Tracking", "Rules", "Techniques", "Training Drills", "Mental Game", "Analytics"]
)

# Home page
if page == "Home":
    st.title("Table Tennis Skills Development Platform")
    st.write("""
    Welcome to your personal table tennis training assistant. This platform combines
    real-time ball tracking technology with comprehensive educational content to help
    you improve your game at any level.
    """)
    
    st.image("assets/table_tennis_hero.jpg", use_column_width=True)
    
    st.subheader("Features")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🎯 Ball Tracking")
        st.write("Analyze your shots with real-time ball tracking")
    
    with col2:
        st.markdown("### 📚 Learning Resources")
        st.write("Comprehensive guides on techniques, rules, and strategy")
    
    with col3:
        st.markdown("### 🏆 Progress Tracking")
        st.write("Monitor your improvement over time")

# Ball Tracking page
elif page == "Ball Tracking":
    st.title("Ball Tracking Analysis")
    
    run = st.button("Start Camera")
    stop = st.button("Stop")
    
    frame_placeholder = st.empty()
    
    if run and not stop:
        cap = cv2.VideoCapture(0)
        
        while cap.isOpened() and not stop:
            success, frame = cap.read()
            if not success:
                st.write("Video capture has ended")
                break
            
            # Process frame with ball tracking
            processed_frame, ball_data = track_ball(frame)
            
            # Convert from BGR to RGB for Streamlit
            processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)
            
            # Display frame
            frame_placeholder.image(processed_frame_rgb, channels="RGB")
            
            # Display metrics if ball detected
            if ball_data:
                st.metric("Ball Speed", f"{ball_data['speed']:.2f} m/s")
                st.metric("Spin Type", ball_data['spin_type'])
            
            if cv2.waitKey(1) & 0xFF == ord('q') or stop:
                break
        
        cap.release()
        cv2.destroyAllWindows()

# Rules page
elif page == "Rules":
    show_rules_page()

# Techniques page
elif page == "Techniques":
    show_techniques_page()

# Training Drills page
elif page == "Training Drills":
    show_drills_page()

# Mental Game page
elif page == "Mental Game":
    show_mental_game_page()

# Analytics page
elif page == "Analytics":
    st.title("Performance Analytics")
    st.write("Analytics content will go here.")
