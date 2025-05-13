import streamlit as st
import cv2 
import numpy as np
from ball_tracker import track_ball
from data.rules import show_rules_page
from data.techniques import show_techniques_page
from data.drills import show_drills_page
from data.mental_game import show_mental_game_page
import tempfile
from utils import run_roboflow_inference, extract_ball_positions
from utils import overlay_video
import os
import plotly.graph_objs as go

# Set page config
st.set_page_config(
    page_title="Table Tennis Trainer",
    page_icon="🏓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.title("Table Tennis Trainer")
page = st.sidebar.radio(
    "Go to",
    ["Home", "Ball Detection", "3D Trajectory", "Rules", "Techniques", "Training Drills", "Mental Game", "Analytics"]
)

# Home page
if page == "Home":
    st.title("Table Tennis Skills Development Platform")
    st.write("""
    Welcome to your personal table tennis training assistant. This platform combines
    real-time ball tracking technology with comprehensive educational content to help
    you improve your game at any level.
    """)
    
    st.image("assets/table_tennis_hero.jpg", use_container_width=True)
    
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

elif page == "Ball Detection":
    st.title("Ball Detection from Uploaded Video")
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "webm"])
    if uploaded_file is not None:
        save_dir = os.path.join(os.getcwd(), "outputs")
        os.makedirs(save_dir, exist_ok=True)
        save_path = os.path.join(save_dir, uploaded_file.name)
        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())
        input_video_path = save_path
        st.video(input_video_path)
        # Use regex to replace extension for JSON and overlay video
        base, ext = os.path.splitext(input_video_path)
        output_json_path = base + "-output.json"
        output_video_path = base + "-overlay.mp4"
        print("Output JSON path:", output_json_path)
        print("Output video path:", output_video_path)

        with st.spinner("Running inference..."):
            run_roboflow_inference(input_video_path, output_json_path)
        with st.spinner("Generating overlay video..."):
            overlay_video(input_video_path, output_json_path, output_video_path)

        st.success("Processing complete!")
        st.video(output_video_path)

elif page == "3D Trajectory":
    st.title("3D Ball Trajectory from Top and Side Views")
    col1, col2 = st.columns(2)
    with col1:
        top_file = st.file_uploader("Upload Top View Video", type=["mp4", "webm"], key="top")
    with col2:
        side_file = st.file_uploader("Upload Side View Video", type=["mp4", "webm"], key="side")

    if top_file and side_file:
        save_dir = os.path.join(os.getcwd(), "outputs")
        os.makedirs(save_dir, exist_ok=True)
        top_path = os.path.join(save_dir, "top_" + top_file.name)
        side_path = os.path.join(save_dir, "side_" + side_file.name)
        with open(top_path, "wb") as f:
            f.write(top_file.read())
        with open(side_path, "wb") as f:
            f.write(side_file.read())
        st.video(top_path)
        st.video(side_path)

        top_json = top_path.replace(".mp4", "-output.json").replace(".webm", "-output.json")
        side_json = side_path.replace(".mp4", "-output.json").replace(".webm", "-output.json")

        with st.spinner("Running inference on Top View..."):
            run_roboflow_inference(top_path, top_json)
        with st.spinner("Running inference on Side View..."):
            run_roboflow_inference(side_path, side_json)
        st.success("Inference complete on both views!")

        # Extract positions
        top_positions = extract_ball_positions(top_json)
        side_positions = extract_ball_positions(side_json)

        # Synchronize lengths
        min_len = min(len(top_positions), len(side_positions))
        top_positions = top_positions[:min_len]
        side_positions = side_positions[:min_len]

        # Reconstruct 3D trajectory
        trajectory = []
        for (x_top, y_top), (x_side, y_side) in zip(top_positions, side_positions):
            x = x_top
            y = y_top
            z = y_side  # y from side view as height
            trajectory.append((x, y, z))

        if trajectory:
            xs, ys, zs = zip(*trajectory)
            fig = go.Figure(data=[go.Scatter3d(
                x=xs, y=ys, z=zs,
                mode='lines+markers',
                marker=dict(size=4, color='red'),
                line=dict(color='blue', width=2)
            )])
            fig.update_layout(
                scene=dict(
                    xaxis_title='X',
                    yaxis_title='Y',
                    zaxis_title='Z (height)'
                ),
                width=800,
                margin=dict(r=20, l=10, b=10, t=10)
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No trajectory data found.")
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
