import streamlit as st

st.title("OpenCV Debug")

try:
    import cv2
    st.success(f"✅ cv2 imported successfully — version: {cv2.__version__}")
except ImportError as e:
    st.error(f"❌ ImportError: {e}")
except Exception as e:
    st.error(f"❌ Unexpected error: {e}")