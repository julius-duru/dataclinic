import streamlit as st
import pandas as pd

TITLE = "Deep Learning from Scratch: ANN, CNN, RNN & LSTM"
CATEGORY = "deep_learning"
KEYWORDS = [
    "deep learning", "neural networks", "ANN", "CNN", "RNN", "LSTM", "backpropagation",
    "Streamlit", "computer vision", "NLP", "time series", "end-to-end projects"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate | 4 working projects inside")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        This guide takes you through **four essential types of neural networks** – ANN, CNN, RNN, and LSTM –  
        with **complete end‑to‑end Streamlit projects** for each. 

        **What you'll build:**  
        -  **ANN** – California house price predictor (tabular data)  
        -  **CNN** – Fashion MNIST clothing classifier (images)  
        -  **RNN** – Sine wave next‑step predictor (short sequences)  
        -  **LSTM** – Airline passenger forecast (long‑term memory)  

        Each project includes: data preparation, model training (with PyTorch/Keras), saving the model, and a full Streamlit app.  
        You can copy, run, and adapt them to your own problems.

        """
    )
    st.markdown("---")

    # 1. ANN – ARTIFICIAL NEURAL NETWORK
    st.header(" 1. ANN – Artificial Neural Network (Tabular Data)")
    st.write(
        """
        ANNs are the simplest and most versatile. They work great for **rows and columns** – like spreadsheets.  
        They have no memory of order or spatial structure, just pure mapping from inputs to outputs.
        """
    )
    with st.expander(" When to use ANN", expanded=False):
        st.markdown(
            """
            - House price prediction (square feet, bedrooms, location → price)  
            - Customer churn (usage patterns → will they leave?)  
            - Medical diagnosis (symptoms → disease)  
            - Credit scoring (income, debt → loan default risk)  
            """
        )

    st.subheader(" End‑to‑End Project: California Housing Price Predictor")
    st.write(
        """
        **Problem:** Predict median house value in a district from 8 features (income, house age, rooms, population, etc.).  
        **Dataset:** Built‑in `fetch_california_housing` from sklearn.  
        **Model:** Simple ANN with two hidden layers.
        """
    )

    with st.expander(" 1. Train the ANN model (save as house_ann_model.h5)", expanded=True):
        st.code(
            """
# train_ann.py
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import joblib

# Load data
data = fetch_california_housing()
X, y = data.data, data.target

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Build ANN
model = Sequential([
    Dense(64, activation='relu', input_shape=(8,)),
    Dropout(0.2),
    Dense(32, activation='relu'),
    Dense(1)   # regression output
])
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Train
model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2, verbose=1)

# Save model and scaler
model.save('house_ann_model.h5')
joblib.dump(scaler, 'scaler.pkl')
print("Model saved as house_ann_model.h5")
            """,
            language="python"
        )

    with st.expander(" 2. Streamlit app (app_ann.py)", expanded=False):
        st.code(
            """
import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

st.set_page_config(page_title="House Price Predictor", page_icon="")
st.title(" California House Price Predictor (ANN)")
st.markdown("Enter the 8 features of a district to predict median house value (in $100,000).")

MedInc = st.number_input("Median Income (in $10k)", 0.5, 15.0, 3.5)
HouseAge = st.number_input("Median House Age (years)", 1, 50, 20)
AveRooms = st.number_input("Average Rooms per Household", 1, 20, 5)
AveBedrms = st.number_input("Average Bedrooms per Household", 0.5, 10, 1)
Population = st.number_input("Population", 100, 50000, 2000)
AveOccup = st.number_input("Average Occupancy", 1, 10, 3)
Latitude = st.number_input("Latitude", 32, 42, 34)
Longitude = st.number_input("Longitude", -124, -114, -118)

if st.button("Predict Price"):
    model = load_model('house_ann_model.h5')
    scaler = joblib.load('scaler.pkl')
    input_array = np.array([[MedInc, HouseAge, AveRooms, AveBedrms,
                             Population, AveOccup, Latitude, Longitude]])
    input_scaled = scaler.transform(input_array)
    pred = model.predict(input_scaled)[0][0]
    st.success(f" Predicted Median House Value: **${pred*100:.0f}k**")
            """,
            language="python"
        )
    st.info("Run with: `streamlit run app_ann.py`")
    st.markdown("---")

    # 2. CNN – CONVOLUTIONAL NEURAL NETWORK
    st.header(" 2. CNN – Convolutional Neural Network (Images)")
    st.write(
        """
        CNNs are the kings of computer vision. They slide small filters across an image to detect edges, textures, and eventually whole objects.  
        **Key ideas:** local connectivity, weight sharing, and pooling.
        """
    )
    with st.expander(" When to use CNN", expanded=False):
        st.markdown(
            """
            - Image classification (cat vs. dog, handwritten digits, fashion items)  
            - Object detection (find cars in a street photo)  
            - Medical imaging (tumour detection in X‑rays)  
            - Facial recognition  
            """
        )

    st.subheader(" End‑to‑End Project: Fashion MNIST Classifier")
    st.write(
        """
        **Problem:** Recognise 10 types of clothing (T‑shirt, trouser, bag, sneaker, etc.) from 28×28 grayscale images.  
        **Dataset:** Fashion‑MNIST (built into Keras).  
        **Model:** Two convolutional layers + pooling + dense layers.
        """
    )

    with st.expander(" 1. Train the CNN model (save as fashion_cnn_model.h5)", expanded=True):
        st.code(
            """
# train_cnn.py
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import numpy as np

# Load and preprocess
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train = X_train / 255.0
X_test = X_test / 255.0
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

class_names = ['T‑shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Build CNN
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train
model.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.2)

# Save
model.save('fashion_cnn_model.h5')
print("Model saved as fashion_cnn_model.h5")
            """,
            language="python"
        )

    with st.expander(" 2. Streamlit app (app_cnn.py)", expanded=False):
        st.code(
            """
import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Fashion Recognizer", page_icon="")
st.title(" Fashion MNIST Classifier (CNN)")
st.markdown("Upload a 28×28 grayscale image of a clothing item (or any image will be resized).")

uploaded = st.file_uploader("Choose an image (PNG/JPG)", type=["png", "jpg", "jpeg"])
if uploaded is not None:
    img = Image.open(uploaded).convert('L')  # grayscale
    img = img.resize((28, 28))
    st.image(img, caption="Resized to 28×28", width=150)
    img_array = np.array(img) / 255.0
    img_array = img_array.reshape(1, 28, 28, 1)
    model = load_model('fashion_cnn_model.h5')
    pred_probs = model.predict(img_array)[0]
    pred_class = np.argmax(pred_probs)
    confidence = pred_probs[pred_class]
    class_names = ['T‑shirt','Trouser','Pullover','Dress','Coat',
                   'Sandal','Shirt','Sneaker','Bag','Ankle boot']
    st.success(f"**Prediction:** {class_names[pred_class]} (confidence: {confidence:.2%})")
            """,
            language="python"
        )
    st.info("Run with: `streamlit run app_cnn.py`")
    st.markdown("---")

    # 3. RNN – RECURRENT NEURAL NETWORK
    st.header(" 3. RNN – Recurrent Neural Network (Short Sequences)")
    st.write(
        """
        Vanilla RNNs have a simple feedback loop that passes a hidden state from one time step to the next.  
        They work well for short sequences but suffer from **vanishing gradient** – they forget after ~10‑20 steps.
        """
    )
    with st.expander("When to use RNN (vanilla)", expanded=False):
        st.markdown(
            """
            - Short time series (e.g., daily temperature for 2 weeks)  
            - Next‑word prediction for short phrases  
            - Simple sentiment analysis of tweets  
            - Stock price prediction with very short lookback  
            """
        )

    st.subheader(" End‑to‑End Project: Sine Wave Next‑Step Predictor")
    st.write(
        """
        **Problem:** Given the last 20 points of a sine wave, predict the next point.  
        **Dataset:** Generated sine wave (no real data needed).  
        **Model:** Simple RNN with one hidden layer.
        """
    )

    with st.expander(" 1. Train the RNN model (save as sine_rnn_model.h5)", expanded=True):
        st.code(
            """
# train_rnn.py
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense

# Generate sine wave
t = np.arange(0, 1000, 0.1)
data = np.sin(t)
seq_len = 20
X, y = [], []
for i in range(len(data) - seq_len):
    X.append(data[i:i+seq_len])
    y.append(data[i+seq_len])
X = np.array(X).reshape(-1, seq_len, 1)
y = np.array(y)

# Train/test split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build RNN
model = Sequential([
    SimpleRNN(32, activation='tanh', input_shape=(seq_len, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_split=0.2)

model.save('sine_rnn_model.h5')
print("Model saved as sine_rnn_model.h5")
            """,
            language="python"
        )

    with st.expander("2. Streamlit app (app_rnn.py)", expanded=False):
        st.code(
            """
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

st.set_page_config(page_title="Sine Wave Predictor", page_icon="")
st.title("Sine Wave Next‑Step Predictor (Vanilla RNN)")
st.markdown("The RNN sees the last 20 points of a sine wave and predicts the next value.")

t = np.arange(0, 10, 0.1)
data = np.sin(t)
seq_len = 20

if st.button("Predict Next Value"):
    model = load_model('sine_rnn_model.h5')
    last_seq = data[-seq_len:].reshape(1, seq_len, 1)
    pred = model.predict(last_seq)[0][0]
    fig, ax = plt.subplots()
    ax.plot(t, data, label='Sine wave')
    ax.scatter(t[-1] + 0.1, pred, color='red', label='RNN prediction', zorder=5)
    ax.legend()
    st.pyplot(fig)
    st.success(f"Predicted next value: {pred:.4f}")
            """,
            language="python"
        )
    st.info("Run with: `streamlit run app_rnn.py`")
    st.markdown("---")

    # 4. LSTM – LONG SHORT‑TERM MEMORY
    st.header("4. LSTM – Long Short‑Term Memory (Long Sequences)")
    st.write(
        """
        LSTM solves the vanishing gradient problem with **gates** (forget, input, output) that control the flow of information.  
        It can remember patterns over hundreds of steps – perfect for long time series, paragraphs, and conversation history.
        """
    )
    with st.expander("When to use LSTM", expanded=False):
        st.markdown(
            """
            - Machine translation (entire paragraphs)  
            - Stock price forecasting (long‑term trends)  
            - Chatbots (maintaining context over many turns)  
            - Airline passenger prediction (yearly seasonality)  
            """
        )

    st.subheader("End‑to‑End Project: Airline Passenger Forecast")
    st.write(
        """
        **Problem:** Predict the number of international airline passengers for the next month based on the last 12 months.  
        **Dataset:** Airline passengers dataset (1949‑1960, monthly).  
        **Model:** LSTM with 50 memory units.
        """
    )

    with st.expander("1. Train the LSTM model (save as airline_lstm_model.h5)", expanded=True):
        st.code(
            """
# train_lstm.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url, usecols=[1])
data = df.values.astype('float32')

# Normalise
scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Create sequences: 12 months -> next month
seq_len = 12
X, y = [], []
for i in range(len(data_scaled) - seq_len):
    X.append(data_scaled[i:i+seq_len])
    y.append(data_scaled[i+seq_len])
X = np.array(X).reshape(-1, seq_len, 1)
y = np.array(y)

# Train/test split
split = int(0.8 * len(X))
X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Build LSTM
model = Sequential([
    LSTM(50, activation='relu', input_shape=(seq_len, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=100, batch_size=16, validation_split=0.1, verbose=1)

# Save model and scaler
model.save('airline_lstm_model.h5')
import joblib
joblib.dump(scaler, 'airline_scaler.pkl')
print("Model saved as airline_lstm_model.h5")
            """,
            language="python"
        )

    with st.expander("2. Streamlit app (app_lstm.py)", expanded=False):
        st.code(
            """
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import joblib

st.set_page_config(page_title="Air Passenger Forecast", page_icon="")
st.title(" Airline Passenger Forecast (LSTM)")
st.markdown("Predicts next month's passengers based on the last 12 months of data.")

url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
df = pd.read_csv(url)
data = df['Passengers'].values.astype('float32')

model = load_model('airline_lstm_model.h5')
scaler = joblib.load('airline_scaler.pkl')
seq_len = 12

if st.button("Forecast Next Month"):
    last_12 = data[-seq_len:].reshape(1, seq_len, 1)
    pred_scaled = model.predict(last_12)[0][0]
    pred = scaler.inverse_transform([[pred_scaled]])[0][0]
    fig, ax = plt.subplots()
    ax.plot(df['Month'][-24:], data[-24:], marker='o', label='Historical')
    next_month = pd.date_range(start=df['Month'].iloc[-1], periods=2, freq='M')[1]
    ax.scatter(next_month, pred, color='red', s=100, label='LSTM Forecast', zorder=5)
    ax.legend()
    st.pyplot(fig)
    st.success(f"Forecasted passengers for {next_month.strftime('%Y-%m')}: **{int(pred)}**")
            """,
            language="python"
        )
    st.info("Run with: `streamlit run app_lstm.py`")
    st.markdown("---")

    # 5. SUMMARY – DIFFERENCES AT A GLANCE
    st.header("Summary: ANN vs CNN vs RNN vs LSTM")
    diff_df = pd.DataFrame({
        "Feature": ["Best data type", "Memory", "Handles order?", "Vanishing gradient", "Training speed", "Example project"],
        "ANN": ["Tabular", "None", "❌ No", "N/A", "Fast", "House price"],
        "CNN": ["Images (spatial)", "None", "❌ No", "N/A", "Medium (GPU helps)", "Fashion MNIST"],
        "RNN (vanilla)": ["Short sequences", "Short‑term (fades)", "✅ Yes (limited)", "❌ Suffers", "Slow", "Sine wave"],
        "LSTM": ["Long sequences", "Long‑term (gates)", "✅ Yes (excellent)", "✅ Solved", "Slow (more params)", "Airline forecast"]
    })
    st.dataframe(diff_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 6. GREAT RESOURCES
    st.header("Resources")
    st.write(
        """
        Here is where to learn more.
        """
    )
    res_df = pd.DataFrame({
        "Category": ["Interactive Courses", "Video Lectures", "Written Tutorials", " Practice & Code"],
        "Recommendations": [
            "fast.ai – Practical Deep Learning for Coders\nGoogle's ML Crash Course\nDeepLearning.AI (Coursera)",
            "Andrej Karpathy's 'Neural Networks: Zero to Hero'\n3Blue1Brown – Deep Learning series",
            "d2l.ai – Dive into Deep Learning (free book)\nChris Olah's blog (LSTM explanations)",
            "Kaggle competitions\nHugging Face\nPyTorch Tutorials"
        ]
    })
    st.dataframe(res_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
         
        - Replace the sine wave dataset with real stock data.  
        - Add data augmentation to the CNN for better accuracy.  
        - Try GRU (simpler than LSTM) for the airline forecast.  
        - Deploy your Streamlit apps to Streamlit Cloud or Hugging Face Spaces.

        Deep learning is a superpower. Now go build something amazing! 
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Deep Learning from Scratch – 4 complete projects.")