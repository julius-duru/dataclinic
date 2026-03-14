import streamlit as st

# ------------------------------------------------
# Page Configuration
# ------------------------------------------------
st.set_page_config(page_title="Computer Vision", layout="wide")

# ------------------------------------------------
# Top Navigation Links
# ------------------------------------------------
nav1, nav2, nav3, nav4, nav5, nav6, nav7 = st.columns(7)

with nav1:
    st.page_link("app.py", label="🏠 Home", use_container_width=True)
with nav2:
    st.page_link("pages/beginner.py", label="Beginner", use_container_width=True)
with nav3:
    st.page_link("pages/proficient.py", label="Proficient", use_container_width=True)
with nav4:
    st.page_link("pages/advanced.py", label="Advanced", use_container_width=True)
with nav5:
    st.page_link("pages/machine_learning.py", label="ML", use_container_width=True)
with nav6:
    st.page_link("pages/projects.py", label="Projects", use_container_width=True)
with nav7:
    st.page_link("pages/career_soft_skills.py", label="Soft Skills", use_container_width=True)

st.markdown("---")

# ------------------------------------------------
# Page Title and Hero Image
# ------------------------------------------------
st.title("🖼️ Computer Vision in Data Science")
st.write("Explore the technology that enables machines to **see, interpret, and understand the visual world**.")

st.image(
    "https://images.unsplash.com/photo-1677442136019-21780ecad995",
    use_container_width=True
)

st.markdown("---")

# ------------------------------------------------
# Overview of Computer Vision
# ------------------------------------------------
st.header("What is Computer Vision?")
st.write("""
Computer Vision (CV) is a field of **Artificial Intelligence (AI)** that enables computers to **process and interpret visual information** from the world, such as images and videos.  
Unlike humans, machines do not inherently “see” the world; CV combines **image processing, machine learning, and deep learning** to allow computers to recognize objects, detect patterns, and make predictions.

CV powers technologies like:
- Facial recognition systems  
- Self-driving cars  
- Medical imaging diagnostics  
- Automated retail and warehouse systems  

The ultimate goal is to enable machines to perform visual tasks **with accuracy, speed, and scalability**, similar to human perception.
""")

st.markdown("---")

# ------------------------------------------------
# How Computer Vision Works
# ------------------------------------------------
st.header("How Computer Vision Works: Detailed Workflow")

st.write("""
A typical computer vision pipeline includes several critical stages:

1️⃣ **Image Acquisition**  
   - Capturing images or videos using cameras, sensors, or satellites.  
   - Data quality and resolution impact downstream model accuracy.

2️⃣ **Preprocessing**  
   - Noise removal, normalization, resizing, and enhancement.  
   - Ensures images are consistent and suitable for analysis.

3️⃣ **Feature Extraction**  
   - Identifying meaningful patterns such as edges, textures, and key points.  
   - Classical methods: SIFT, HOG, SURF.  
   - Deep learning: CNN automatically learns hierarchical features.

4️⃣ **Model Training**  
   - Using labeled datasets to train machine learning or deep learning models.  
   - Common algorithms: CNN, R-CNN, YOLO, Transformer-based models.

5️⃣ **Prediction & Evaluation**  
   - Applying trained models to new images for classification, detection, or segmentation.  
   - Evaluation metrics: Accuracy, Precision, Recall, F1-score, IoU (for detection/segmentation).

6️⃣ **Deployment**  
   - Integrating CV models into real-world applications like mobile apps, web services, or edge devices.
""")

st.markdown("---")

# ------------------------------------------------
# Core Computer Vision Tasks
# ------------------------------------------------
st.header("Core Tasks in Computer Vision")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1️⃣ Image Classification")
    st.write("""
- Determines the **category of an object** in an image.  
- Example: Identifying if a picture contains a cat, dog, or bird.  
- Uses Convolutional Neural Networks (CNNs) for feature learning.  
- Applications: Face recognition, quality inspection in manufacturing.
""")

with col2:
    st.subheader("2️⃣ Object Detection")
    st.write("""
- Locates **multiple objects** in an image and assigns labels.  
- Example: Detecting pedestrians and vehicles in street scenes.  
- Models: YOLO, SSD, Faster R-CNN.  
- Applications: Autonomous vehicles, surveillance, robotics.
""")

with col3:
    st.subheader("3️⃣ Image Segmentation")
    st.write("""
- Divides an image into **distinct regions** for pixel-level understanding.  
- Types: Semantic segmentation, instance segmentation.  
- Models: U-Net, Mask R-CNN, DeepLab.  
- Applications: Medical imaging, autonomous driving, AR/VR systems.
""")

st.markdown("---")

# ------------------------------------------------
# Tools, Frameworks, and Libraries
# ------------------------------------------------
st.header("🧰 Tools and Libraries in Computer Vision")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("Python Libraries")
    st.write("""
- OpenCV: Image processing, computer vision algorithms  
- Pillow: Image manipulation  
- scikit-image: Advanced image analysis  
""")

with col2:
    st.subheader("Deep Learning Frameworks")
    st.write("""
- TensorFlow / Keras: Neural network modeling  
- PyTorch: Dynamic deep learning workflows  
- FastAI: High-level abstractions for CV projects
""")

with col3:
    st.subheader("Specialized CV Frameworks")
    st.write("""
- YOLO: Real-time object detection  
- Detectron2: Modular detection and segmentation  
- MediaPipe: Hand, face, and pose tracking
""")

with col4:
    st.subheader("Cloud & Deployment Tools")
    st.write("""
- AWS Rekognition, Google Vision AI, Azure Vision  
- Streamlit / Flask for serving models  
- Docker & Kubernetes for deployment and scaling
""")

st.markdown("---")

# ------------------------------------------------
# Real-World Applications
# ------------------------------------------------
st.header("🌍 Real-World Applications of Computer Vision")

st.write("""
Computer vision is transforming multiple industries:

**Healthcare**  
- Automated analysis of X-rays, CT scans, and MRIs.  
- Detect tumors, fractures, and anomalies early.

**Retail & E-commerce**  
- Visual search, product recommendations, and automated checkout.  
- Customer behavior analysis using cameras and CV.

**Transportation & Autonomous Vehicles**  
- Detect pedestrians, traffic signs, and other vehicles.  
- Real-time decision making for safe navigation.

**Security & Surveillance**  
- Facial recognition and anomaly detection in public spaces.  
- Monitoring industrial safety and restricted areas.

**Agriculture**  
- Crop monitoring with drones.  
- Detect diseases, estimate yield, and optimize irrigation.

**Manufacturing**  
- Quality control via automated visual inspection.  
- Detect defects and improve production efficiency.
""")

st.markdown("---")

# ------------------------------------------------
# Learning Path & Projects
# ------------------------------------------------
st.header("📚 Learning Computer Vision")

st.write("""
To become proficient in computer vision:

1️⃣ **Learn Python programming** – NumPy, Pandas, OpenCV  
2️⃣ **Mathematics foundations** – Linear algebra, probability, statistics  
3️⃣ **Machine Learning fundamentals** – Regression, classification, clustering  
4️⃣ **Deep Learning for CV** – CNNs, R-CNN, YOLO, Transformers  
5️⃣ **Build Projects** – Examples:
    - Facial recognition system  
    - Object detection for vehicles or retail  
    - Semantic segmentation for medical images  
6️⃣ **Deploy Models** – Using Streamlit, Flask, or cloud APIs  
7️⃣ **Stay Updated** – Research papers, Kaggle competitions, and open-source contributions
""")

st.markdown("---")

# ------------------------------------------------
# Continue Learning Navigation
# ------------------------------------------------
st.header("Continue Learning")

col1, col2, col3 = st.columns(3)
with col1:
    st.page_link("pages/beginner.py", label="🟢 Beginner Path")
with col2:
    st.page_link("pages/proficient.py", label="🟡 Proficient Path")
with col3:
    st.page_link("pages/machine_learning.py", label="🤖 Machine Learning Path")

st.markdown("---")
st.success("By mastering computer vision, you can **build intelligent visual systems** for multiple industries and applications.")