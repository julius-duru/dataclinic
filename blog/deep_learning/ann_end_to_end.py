import streamlit as st
import pandas as pd


TITLE = "ANN from Scratch: Activation, Loss, Optimizers & Hyperparameter Tuning"
CATEGORY = "deep_learning"
KEYWORDS = [
    "artificial neural networks", "activation functions", "loss functions",
    "gradient descent", "backpropagation", "optimizers", "hyperparameter tuning",
    "regularization", "dropout", "deep learning basics"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        Ever wondered what really makes a neural network *learn*?  
        It's not magic – it's synergy between **activation functions**, **loss functions**, and **optimizers**, guided by **backpropagation**.

        In this guide, we'll break down every essential piece of an Artificial Neural Network (ANN) – from the tiny neuron to the final prediction.  
        **No black boxes** – just clear explanations, practical tables, and a complete code demo you can run yourself.

        **What you'll learn:**  
        - Which **activation function** to use where (ReLU, Sigmoid, Softmax, Tanh)  
        - Which **loss function** matches your problem (MSE, Cross‑Entropy)  
        - How **gradient descent** and **backpropagation** work under the hood  
        - The difference between **SGD, Adam, and RMSprop** optimizers  
        - How to fight **overfitting** with dropout and L2 regularization  
        - How to **tune hyperparameters** like learning rate, batch size, and layer size  

        > Ready to peek under the hood? Let's go! 
        """
    )
    st.markdown("---")

    # 1. ACTIVATION FUNCTIONS
    st.header(" Activation Functions – The Decision Makers")
    st.write(
        """
        An activation function decides whether a neuron should "fire" or not.  
        It also **adds non‑linearity** – without it, stacking layers would be useless (a deep network would collapse into a single linear layer).
        """
    )
    act_df = pd.DataFrame({
        "Function": ["Step", "Sigmoid", "Tanh", "ReLU", "Softmax"],
        "Formula / Output": [
            "0 or 1 (threshold)",
            "0 to 1 (probability)",
            "-1 to 1",
            "max(0, x)",
            "sum to 1 (probability distribution)"
        ],
        "Best for": [
            "Binary classification (old perceptron)",
            "Output layer – binary classification",
            "Hidden layers (zero‑centered, but vanishing gradient)",
            "Hidden layers (default!)",
            "Output layer – multi‑class classification"
        ],
        "Avoid in": [
            "Any modern deep network (zero gradient)",
            "Hidden layers (vanishing gradient)",
            "Output layer (range not 0‑1)",
            "Output layer (unless regression)",
            "Hidden layers (forces probabilities)"
        ]
    })
    st.dataframe(act_df, use_container_width=True, hide_index=True)
    st.info(
        " **Rule of thumb:** Use **ReLU** for all hidden layers. Use **Sigmoid** for binary output, **Softmax** for multi‑class output, and **Linear** (no activation) for regression."
    )
    st.markdown("---")

    # 2. LOSS FUNCTIONS
    st.header(" Loss Functions – How Wrong Are We?")
    st.write(
        """
        A loss function measures the difference between the network's prediction and the true target.  
        The goal of training is to **minimize** this loss.
        """
    )
    loss_df = pd.DataFrame({
        "Loss Function": ["Mean Squared Error (MSE)", "Mean Absolute Error (MAE)", "Binary Cross‑Entropy", "Categorical Cross‑Entropy"],
        "Formula (per sample)": ["(y - ŷ)²", "|y - ŷ|", "-(y log ŷ + (1-y) log(1-ŷ))", "-∑ y_c log ŷ_c"],
        "Used for": ["Regression", "Regression (robust to outliers)", "Binary classification", "Multi‑class classification"],
        "Output activation": ["Linear", "Linear", "Sigmoid", "Softmax"]
    })
    st.dataframe(loss_df, use_container_width=True, hide_index=True)
    st.warning(
        " Don't mix and match! Using cross‑entropy with a linear output (or MSE with softmax) will confuse the network and slow down learning."
    )
    st.markdown("---")

    # 3. GRADIENT DESCENT & BACKPROPAGATION
    st.header(" Gradient Descent & Backpropagation – The Learning Engine")
    st.write(
        """
        **Gradient Descent** is the algorithm that updates the weights to reduce the loss.  
        Imagine standing on a foggy hill and wanting to reach the lowest valley. You feel the slope (gradient) and take a small step downhill.

        **Backpropagation** is the efficient method that computes how much each weight contributed to the error – it propagates the error backwards through the network using the chain rule.

        The learning rate (**lr**) controls the step size:  
        - Too large → overshoot and never converge  
        - Too small → snail‑pace training
        """
    )
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Learning rate typical range", "1e-5 to 1e-1", delta="log scale")
    with col2:
        st.metric("Default for Adam", "0.001", delta="works for most tasks")
    st.markdown("---")

    # 4. OPTIMIZERS
    st.header(" Optimizers – SGD, Adam, RMSprop")
    st.write(
        """
        An optimizer is a specific variant of gradient descent. Here are the three you'll meet most often.
        """
    )
    opt_df = pd.DataFrame({
        "Optimizer": ["SGD (with momentum)", "RMSprop", "Adam"],
        "Key idea": [
            "Simple update, momentum smooths the path",
            "Adaptive learning rate per parameter (using recent gradients)",
            "Combines momentum + adaptive learning rate"
        ],
        "Pros": ["Works well after tuning", "Handles vanishing/exploding gradients", "Default choice, little tuning needed"],
        "Cons": ["Needs careful learning rate selection", "Can be unstable", "May overfit sometimes"]
    })
    st.dataframe(opt_df, use_container_width=True, hide_index=True)
    st.success(" **Adam** is the go‑to optimizer for 95% of problems. Start there.")
    st.markdown("---")

    # 5. REGULARIZATION – FIGHTING OVERFITTING
    st.header(" Regularization – Keeping Your Network Honest")
    st.write(
        """
        **Overfitting** happens when the network memorizes the training data instead of learning general patterns.  
        It performs great on training but poorly on new data.

        Here are the most effective cures:
        """
    )
    with st.expander(" Dropout (randomly turn off neurons)", expanded=False):
        st.write(
            """
            During training, dropout randomly sets a fraction of neurons to zero (e.g., 20‑50%).  
            This forces the network to learn redundant representations – no single neuron becomes too important.  
            At test time, dropout is turned off, and all neurons contribute (scaled down).  
            **Effect:** Dramatically reduces overfitting, especially in large networks.
            """
        )
    with st.expander(" L1 / L2 Regularization (weight penalties)", expanded=False):
        st.write(
            """
            Add a penalty term to the loss function:  
            - **L2** (Ridge) adds the sum of squared weights. It encourages small, spread‑out weights.  
            - **L1** (Lasso) adds the sum of absolute weights. It can drive some weights to zero (feature selection).  
            In Keras, you add `kernel_regularizer=regularizers.l2(0.01)` to a layer.
            """
        )
    with st.expander(" Early Stopping", expanded=False):
        st.write(
            """
            Monitor the validation loss during training. When it stops improving for a number of epochs (e.g., patience=10), stop training.  
            This prevents the network from over‑learning the training noise.
            """
        )
    with st.expander(" Data Augmentation", expanded=False):
        st.write(
            """
            Create more training data artificially: flip, rotate, zoom, or shift images.  
            A cat is still a cat upside‑down! More data = better generalization.
            """
        )
    st.markdown("---")

    # 6. HYPERPARAMETER TUNING
    st.header(" Hyperparameter Tuning – The Art of the Best Settings")
    st.write(
        """
        Hyperparameters are the knobs you turn **before** training. They are not learned from data.  
        Tuning them can turn a mediocre model into a state‑of‑the‑art one.

        **Common hyperparameters:**  
        - Learning rate (most important)  
        - Number of layers and neurons per layer  
        - Batch size  
        - Dropout rate / regularization strength  
        - Optimizer choice and its parameters  

        **Tuning methods:**  
        - **Grid Search** – try all combinations (expensive)  
        - **Random Search** – sample randomly (more efficient)  
        - **Bayesian Optimization** – smart guided search  
        - **Manual tuning** – based on learning curves
        """
    )
    hp_df = pd.DataFrame({
        "Hyperparameter": ["Learning rate", "Batch size", "Hidden units", "Dropout rate", "Number of layers"],
        "Typical range": ["1e-5 to 1e-1 (log)", "16, 32, 64, 128", "32 to 512 (powers of 2)", "0.0 to 0.5", "1 to 5"],
        "Impact": ["Very high", "Medium (speed & stability)", "High (model capacity)", "Medium (regularization)", "High (depth)"]
    })
    st.dataframe(hp_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 7. COMPLETE ANN DEMO (MNIST with tuning)
    st.header(" Complete ANN Demo: Handwritten Digit Recognition")
    st.write(
        """
        We'll build a small ANN from scratch using **TensorFlow/Keras**.  
        It will demonstrate:
        - ReLU hidden layers + Softmax output
        - Categorical cross‑entropy loss
        - Adam optimizer
        - Dropout for regularization
        - Hyperparameter tuning (just a taste – you can expand)
        """
    )
    with st.expander(" Full Code (runs in minutes)", expanded=True):
        st.code(
            """
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# 1. Load data (8x8 digits, 10 classes)
digits = load_digits()
X, y = digits.data, digits.target
y_cat = to_categorical(y, 10)

# 2. Train/validation/test split
X_train, X_temp, y_train, y_temp = train_test_split(X, y_cat, test_size=0.3, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# 3. Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# 4. Build model
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(64,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

# 5. Compile
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 6. Train
history = model.fit(X_train, y_train,
                    validation_data=(X_val, y_val),
                    epochs=50,
                    batch_size=32,
                    verbose=1,
                    callbacks=[keras.callbacks.EarlyStopping(patience=10, restore_best_weights=True)])

# 7. Evaluate
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"Test accuracy: {test_acc:.4f}")

# 8. Plot learning curves
plt.plot(history.history['accuracy'], label='train acc')
plt.plot(history.history['val_accuracy'], label='val acc')
plt.title('Accuracy over epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
            """,
            language="python"
        )
    st.success(
        " This simple ANN typically achieves **~96‑98% test accuracy** on the digits dataset. "
        "Try changing the number of layers, dropout rate, or optimizer to see how performance changes!"
    )

    # Optional: interactive tuning example (simplified)
    st.subheader(" Interactive Tuning Example (simulate with sliders)")
    st.write("Adjust the hyperparameters below to see how they affect validation accuracy (simulated).")
    col_a, col_b = st.columns(2)
    with col_a:
        lr_sim = st.select_slider("Learning rate (log scale)", options=[0.0001, 0.0005, 0.001, 0.005, 0.01], value=0.001)
        dropout_sim = st.slider("Dropout rate", 0.0, 0.5, 0.3, step=0.05)
    with col_b:
        units_sim = st.select_slider("Hidden units (first layer)", options=[32, 64, 128, 256], value=128)
        batch_sim = st.select_slider("Batch size", options=[16, 32, 64, 128], value=32)
    
    # Very rough simulation (for educational purposes only)
    base_acc = 0.96
    acc = base_acc
    if lr_sim not in [0.001, 0.0005]:
        acc -= 0.02
    if dropout_sim > 0.4:
        acc -= 0.01
    if units_sim < 64:
        acc -= 0.01
    if batch_sim not in [32, 64]:
        acc -= 0.005
    acc = min(0.98, max(0.90, acc))
    st.metric("Estimated validation accuracy", f"{acc:.2%}", delta="±2% (just a demo)")
    st.caption("This is a simplified simulation to illustrate the impact of hyperparameters. Real tuning requires training the model.")

    st.markdown("---")

    # 8. SUMMARY TABLE
    st.header(" One‑Page Cheat Sheet")
    summary_df = pd.DataFrame({
        "Component": ["Activation (hidden)", "Activation (binary out)", "Activation (multi out)", "Loss (regression)", "Loss (binary class)", "Loss (multi class)", "Optimizer (default)", "Regularization", "Tuning method"],
        "Recommendation": ["ReLU", "Sigmoid", "Softmax", "MSE", "Binary Cross‑Entropy", "Categorical Cross‑Entropy", "Adam", "Dropout + Early Stopping", "Random Search"],
        "Avoid": ["Sigmoid/Tanh", "ReLU/Linear", "Sigmoid/ReLU", "Cross‑Entropy", "MSE", "MSE", "SGD without tuning", "No regularization", "Grid search (expensive)"]
    })
    st.dataframe(summary_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
        **Best tips:**  
        - Always scale your input data (StandardScaler or MinMaxScaler).  
        - Start small – one or two hidden layers often suffice.  
        - Monitor validation loss to catch overfitting early.  
        - Use **Adam** + **ReLU** + **Cross‑Entropy** as your default starting point.  
        - Have fun and experiment – that's how you truly learn!

        Now you're ready to build your own ANNs from scratch. Go make some mistakes (and fix them with backpropagation)! 
        """
    )
    st.markdown("---")
    st.caption("© 2026 | ANN from Scratch – clear, practical, and no black boxes.")

