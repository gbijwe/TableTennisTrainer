import cv2
import numpy as np
import streamlit as st
from roboflow import Roboflow
import json
import traceback
import os
def run_roboflow_inference(input_video_path, output_json_path):
    try:
        st.info(f"Starting Roboflow inference for: {input_video_path}")
        rf = Roboflow(api_key="EJuRj2c5k4WSeHZHmqG7")
        project = rf.workspace().project("ball-ugsvu-pejz9-l1ln1")
        model = project.version("1").model

        st.info("Calling model.predict_video...")
        job_id, signed_url, expire_time = model.predict_video(
            input_video_path,
            fps=24,
            prediction_type="batch-video",
        )
        st.write(f"Roboflow job_id: {job_id}")
        # st.write(f"Signed URL: {signed_url}")
        # st.write(f"Expire time: {expire_time}")

        st.info("Polling for video results...")
        results = model.poll_until_video_results(job_id)
        st.write("Roboflow results:", results)

        with open(output_json_path, "w") as json_file:
            json.dump(results, json_file, indent=2)
        st.success(f"Roboflow inference complete. Output saved to {output_json_path}")
        return output_json_path
    except Exception as e:
        st.error(f"Roboflow inference failed: {e}")
        st.error(traceback.format_exc())
        return None

def overlay_video(input_video_path, json_path, output_video_path):
    with open(json_path, 'r') as json_file:
        inference_data = json.load(json_file)

    cap = cv2.VideoCapture(input_video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    if inference_data.get("status_info") == "decode error":
        st.error("Inference failed: decode error. Please check your video format.")
        return None
    
    frame_idx = 0
    for frame_data in inference_data['ball-ugsvu-pejz9-l1ln1']:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_idx)
        ret, frame = cap.read()
        if not ret:
            break
        for prediction in frame_data['predictions']:
            x = int(prediction['x'])
            y = int(prediction['y'])
            w = int(prediction['width'])
            h = int(prediction['height'])
            confidence = prediction['confidence']
            x1 = int(x - w / 2)
            y1 = int(y - h / 2)
            x2 = int(x + w / 2)
            y2 = int(y + h / 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            coords_text = f"x: {x}, y: {y}"
            text_size = cv2.getTextSize(coords_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)[0]
            text_x = width - text_size[0] - 10
            text_y = 30
            cv2.putText(frame, coords_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
        out.write(frame)
        frame_idx += 1
    cap.release()
    out.release()

    if not os.path.exists(output_video_path) or os.path.getsize(output_video_path) < 1000:
        st.error(f"Output video was not created or is empty: {output_video_path}")
        return None
    return output_video_path

def extract_ball_positions(json_path):
    """Extracts (x, y) positions from Roboflow JSON output."""
    with open(json_path, 'r') as json_file:
        inference_data = json.load(json_file)
    positions = []
    frames = inference_data.get('ball-ugsvu-pejz9-l1ln1', [])
    for frame_data in frames:
        preds = frame_data.get('predictions', [])
        if preds:
            # Use the first prediction (or refine as needed)
            x = int(preds[0]['x'])
            y = int(preds[0]['y'])
            positions.append((x, y))
        else:
            positions.append((None, None))  # No detection in this frame
    # Remove frames with None
    positions = [p for p in positions if None not in p]
    return positions