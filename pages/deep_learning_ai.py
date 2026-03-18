import streamlit as st
import pandas as pd


def show():

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
    # Page Header
    # ------------------------------------------------
    st.title("🧠 Deep Learning")

    st.write("""
Deep learning is one of the most exciting areas in **artificial intelligence and data science**.

""")

    st.image(
        "images/deep_learning.jpg",
        use_container_width=True
    )

    st.markdown("---")

    st.write("""
You may have heard about technologies like **self-driving cars, voice assistants, facial recognition,
or ChatGPT**. Behind many of these systems is a powerful technology called **deep learning**.

Deep learning is a branch of **machine learning** that uses **artificial neural networks** to
learn patterns from very large amounts of data.

Unlike traditional machine learning models that require manual feature engineering,
deep learning models are capable of **automatically learning complex patterns** from data.

Think of deep learning as a way to **teach computers how to learn like humans**.

Instead of explicitly programming rules, we allow models to learn patterns by
processing large datasets and adjusting their internal parameters.
""")

    st.markdown("---")

    # ==================================================
    # What Makes Deep Learning Different
    # ==================================================
    st.subheader("🤖 Why Deep Learning is Powerful")

    st.write("""
Deep learning has become extremely popular because it performs very well
in tasks that involve **complex and unstructured data**.

Examples include:

• Images  
• Videos  
• Speech  
• Natural language text  

Traditional machine learning struggles with these types of data,
but deep learning models can **extract patterns automatically**.
""")

    concepts = [
        ["Large Neural Networks", "Models with many layers that learn hierarchical patterns", "Core Concept"],
        ["Automatic Feature Learning", "The model discovers important patterns itself", "Key Advantage"],
        ["Big Data Friendly", "Works best with large datasets", "Data Requirement"],
        ["High Computing Power", "Often trained using GPUs or cloud computing", "Infrastructure"]
    ]

    df_concepts = pd.DataFrame(concepts, columns=["Concept", "Description", "Category"])
    st.table(df_concepts)

    st.markdown("---")

    # ==================================================
    # Neural Networks
    # ==================================================
    st.subheader("🧠 Understanding Neural Networks")

    st.write("""
Deep learning models are built using **artificial neural networks**.

These networks are inspired by the structure of the **human brain**.

A neural network consists of multiple layers:

• **Input Layer** – receives the raw data  
• **Hidden Layers** – process and transform the data  
• **Output Layer** – produces predictions  

Each layer learns increasingly complex patterns.
""")

    layers = [
        ["Input Layer", "Receives raw data such as images, numbers, or text"],
        ["Hidden Layers", "Perform mathematical transformations and pattern learning"],
        ["Output Layer", "Produces predictions such as classification results"]
    ]

    df_layers = pd.DataFrame(layers, columns=["Layer", "Role"])
    st.table(df_layers)

    st.markdown("---")

    # ==================================================
    # Popular Deep Learning Architectures
    # ==================================================
    st.subheader("🏗 Deep Learning Architecture")

    st.write("""
Different neural network architectures are designed for different types of problems.
Below are some of the most widely used deep learning models.
""")

    architectures = [
        ["CNN (Convolutional Neural Networks)", "Image recognition and computer vision", "Used in facial recognition and medical imaging"],
        ["RNN (Recurrent Neural Networks)", "Sequential data such as text and time series", "Used in speech recognition and forecasting"],
        ["LSTM", "Improved RNN architecture for long-term memory", "Used in NLP and financial forecasting"],
        ["Transformers", "Advanced deep learning models for language tasks", "Used in ChatGPT, BERT, and GPT models"]
    ]

    df_arch = pd.DataFrame(architectures, columns=["Architecture", "Best For", "Example Use"])
    st.table(df_arch)

    st.markdown("---")

    # ==================================================
    # Tools & Frameworks
    # ==================================================
    st.subheader("🧰 Deep Learning Tools")

    st.write("""
Training deep learning models requires specialized libraries and frameworks.
These tools make it easier to design, train, and deploy neural networks.
""")

    tools = [
        ["TensorFlow", "Deep learning framework developed by Google", "Widely used for production AI systems"],
        ["PyTorch", "Flexible deep learning framework developed by Meta", "Popular among researchers"],
        ["Keras", "High-level neural network API", "Simplifies deep learning development"],
        ["CUDA / GPUs", "Hardware acceleration for training models", "Speeds up training significantly"]
    ]

    df_tools = pd.DataFrame(tools, columns=["Tool", "Purpose", "Notes"])
    st.table(df_tools)

    st.markdown("---")

    # ==================================================
    # Real World Applications
    # ==================================================
    st.subheader("🌍 Real-World Applications")

    st.write("""
Deep learning powers many technologies that we interact with every day.
""")

    applications = [
        ["Computer Vision", "Face recognition, self-driving cars, medical imaging"],
        ["Natural Language Processing", "Chatbots, language translation, sentiment analysis"],
        ["Speech Recognition", "Voice assistants like Alexa and Siri"],
        ["Recommendation Systems", "Netflix, Amazon, and Spotify recommendations"],
        ["Healthcare AI", "Disease detection from medical scans"]
    ]

    df_apps = pd.DataFrame(applications, columns=["Field", "Example Applications"])
    st.table(df_apps)

    st.markdown("---")

    # ==================================================
    # Practice Projects
    # ==================================================
    st.subheader("💡 Deep Learning Practice Projects")

    st.write("""
If you want to learn deep learning effectively, building projects is essential.

Here are some project ideas you can start with.
""")

    projects = [
        ["Handwritten Digit Recognition", "CNN + TensorFlow", "Beginner"],
        ["Image Classification System", "CNN + PyTorch", "Intermediate"],
        ["Sentiment Analysis Model", "LSTM + NLP", "Intermediate"],
        ["Chatbot using Transformers", "HuggingFace Transformers", "Advanced"],
        ["Object Detection System", "YOLO or Detectron", "Advanced"]
    ]

    df_projects = pd.DataFrame(projects, columns=["Project", "Tools", "Difficulty"])
    st.table(df_projects)

    st.markdown("---")

    # ==================================================
    # Learning Resources
    # ==================================================
    st.subheader("📚 Learning Resources")

    st.write("""
If you want to go deeper into deep learning, these resources are extremely helpful.
""")

    st.markdown("""
• **DeepLearning.ai** – Andrew Ng’s deep learning courses  
• **Fast.ai** – Practical deep learning tutorials  
• **Kaggle** – Datasets and competitions  
• **PyTorch Documentation** – Official tutorials and guides  
• **TensorFlow Documentation** – Production deep learning systems
""")


show()