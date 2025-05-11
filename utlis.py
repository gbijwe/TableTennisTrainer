import cv2
import numpy as np
import streamlit as st

def load_image(image_path):
    """Load an image from disk."""
    image = cv2.imread(image_path)
    if image is None:
        st.error(f"Could not load image at {image_path}")
    return image

def resize_frame(frame, width=None, height=None):
    """Resize a frame to a given width or height while maintaining aspect ratio."""
    (h, w) = frame.shape[:2]
    if width is not None:
        r = width / float(w)
        dim = (width, int(h * r))
    elif height is not None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        return frame
    resized = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    return resized

def convert_bgr_to_rgb(frame):
    """Convert a BGR OpenCV image to RGB for Streamlit display."""
    return cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

def draw_ball_trajectory(frame, pts, color=(0, 0, 255), thickness=2):
    """Draw the trajectory of the ball on the frame."""
    for i in range(1, len(pts)):
        if pts[i - 1] is None or pts[i] is None:
            continue
        # Thickness decreases for older points
        t = int(np.sqrt(len(pts) / float(i + 1)) * thickness)
        cv2.line(frame, pts[i - 1], pts[i], color, t)
    return frame

def calculate_distance(pt1, pt2):
    """Calculate Euclidean distance between two points."""
    if pt1 is None or pt2 is None:
        return 0
    return np.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)

def get_ball_center(contour):
    """Get the center (x, y) of a contour."""
    M = cv2.moments(contour)
    if M["m00"] == 0:
        return None
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    return center

def mask_ball_hsv(frame, lower_hsv, upper_hsv):
    """Create a mask for the ball based on HSV color range."""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    # Morphological operations to remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    return mask

def find_largest_contour(mask):
    """Find the largest contour in a mask (assumed to be the ball)."""
    contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
        return None
    return max(contours, key=cv2.contourArea)
