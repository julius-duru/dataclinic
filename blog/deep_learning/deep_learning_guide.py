import streamlit as st
import pandas as pd

TITLE = "Deep Learning: Optimization, Regularization & Uncertainty"
CATEGORY = "deep_learning"

KEYWORDS = [
    "learning rate", "loss function", "gradient descent", "SGD", "Adam",
    "RMSProp", "Adagrad", "Adadelta", "regularization", "dropout",
    "batch norm", "early stopping", "imbalanced data", "label noise",
    "uncertainty estimation", "graph neural networks", "GNN"
]


def show():
    st.set_page_config(page_title=TITLE, page_icon="🧠", layout="wide")

    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Intermediate → Advanced")
    st.markdown("---")

    # =========================
    # INTRO
    # =========================
    st.markdown(
        """
At the heart of every neural network lies a simple loop:

- Initialize weights randomly  
- Loop until convergence  
- Pick a data point  
- Compute gradient  
- Update weights  

This is **Stochastic Gradient Descent (SGD)**.

But real-world training requires mastering three pillars:

1. **Optimization**  
2. **Regularization**  
3. **Uncertainty**

This guide bridges theory and practice so you can train models that generalize well.
"""
    )

    st.markdown("---")

    # =========================
    # PART 1
    # =========================
    st.header("Part 1 – The Trinity: Loss, Learning Rate & Optimizers")

    st.subheader("1.1 Loss Function")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Regression (predict a number)**")
        st.markdown(
            """
- **MSE** – penalizes large errors  
- **MAE** – robust to outliers  
- **Huber Loss** – balance between MSE and MAE
"""
        )

    with col2:
        st.markdown("**Classification (predict a class)**")
        st.markdown(
            """
- **Binary Cross-Entropy**  
- **Categorical Cross-Entropy**  
- **Focal Loss** – best for imbalance  
- **Contrastive Loss** – embeddings
"""
        )

    st.info("Use weighted loss or focal loss for imbalanced data.")

    # =========================
    # LEARNING RATE
    # =========================
    st.subheader("1.2 Learning Rate")

    st.markdown(
        """
The learning rate controls how big each update step is.

- Too high → divergence  
- Too low → slow training  
- Just right → smooth convergence
"""
    )

    with st.expander(" LR tuning techniques"):
        st.markdown(
            """
- Step decay  
- Cosine annealing  
- Warmup  
- LR Finder
"""
        )

    # =========================
    # OPTIMIZERS
    # =========================
    st.subheader("1.3 Optimizers")

    optim_df = pd.DataFrame({
        "Optimizer": ["SGD", "Momentum", "Adagrad", "RMSProp", "Adam"],
        "Idea": [
            "Basic gradient descent",
            "Adds velocity",
            "Adaptive per parameter",
            "Fixes Adagrad decay",
            "Momentum + RMSProp"
        ],
        "Best Use": [
            "Baseline",
            "Faster convergence",
            "Sparse data",
            "RNNs",
            "Default choice"
        ]
    })

    st.dataframe(optim_df, use_container_width=True)

    st.markdown("---")

    # =========================
    # PART 2
    # =========================
    st.header("Part 2 – Regularization")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Explicit Methods")
        st.markdown(
            """
- L1 / L2 (weight decay)  
- Dropout  
- BatchNorm  
- Label smoothing
"""
        )

    with col2:
        st.subheader("Implicit Methods")
        st.markdown(
            """
- Early stopping  
- Data augmentation
"""
        )

    st.success("Start with Early Stopping + Weight Decay")

    st.markdown("---")

    # =========================
    # PART 3
    # =========================
    st.header("Part 3 – Uncertainty")

    with st.expander("Handling Imbalance"):
        st.markdown(
            """
- Oversampling / Undersampling  
- Weighted loss  
- Focal Loss  

Use F1-score, not accuracy.
"""
        )

    with st.expander("Handling Noise"):
        st.markdown(
            """
- Huber Loss  
- Label cleaning   
- MC Dropout  
- Ensembles
"""
        )

    st.markdown("---")

    # =========================
    # PART 4
    # =========================
    st.header("Applications")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Neural Networks")
        st.markdown(
            """
- Computer Vision  
- NLP  
- Fraud Detection  
- Forecasting
"""
        )

    with col2:
        st.subheader("Graph Neural Networks (GNNs)")
        st.markdown(
            """
- Social networks  
- Drug discovery  
- Recommender systems  
- Traffic prediction
"""
        )

    st.markdown("---")

    # =========================
    # CHECKLIST
    # =========================
    st.header("Training Checklist")

    st.markdown(
        """
- Define metrics (F1, AUC)  
- Proper data split  
- Start with Adam (lr=0.001)  
- Use Early Stopping  
- Add weight decay  
- Handle imbalance if needed  
- Validate on unseen data
"""
    )

    st.markdown("---")

    # =========================
    # FINAL
    # =========================
    st.header("Summary")

    st.markdown(
        """
Deep learning is experimental.

Start simple → improve step by step.

The best model is the one that works reliably in production.
"""
    )

    st.markdown("---")
    st.caption("© 2026 | Deep Learning Guide")