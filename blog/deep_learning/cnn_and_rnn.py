import streamlit as st
import pandas as pd

TITLE = "CNN and RNN in Deep Learning"
CATEGORY = "deep_learning"
KEYWORDS = [
    "deep learning", "neural networks", "CNN", "RNN", "LSTM", "back propagation","backpropagation",
    "forward propagation", "regularization", "PyTorch", "computer vision", "NLP"
]

def show():
    st.title(TITLE)
    st.caption(f"Category: {CATEGORY} | Level: Beginner → Intermediate")
    st.markdown("---")

    # INTRODUCTION
    st.write(
        """
        Deep learning is a subfield of machine learning inspired by the structure and function of the human brain – specifically, neural networks with many layers. Over the past decade, it has revolutionized domains such as computer 
        vision, natural language processing, speech recognition, and robotics.
        
        Have you ever wondered how your phone recognizes your face, or how ChatGPT can talk like a human? The secret sauce behind these AI superpowers is **deep learning** – a type of machine learning that mimics how our brains work.  
        In this article, we will explore two of the most important deep learning concepts: **Convolutional Neural Networks (CNNs)** for images and **Recurrent Neural Networks (RNNs)** for sequences like text.  
        We will break down the concepts in plain English, show you how they work with simple diagrams, and even give you some code snippets to play with.  
        Whether you are a data analyst looking to level up your skills or just curious about how AI works, this guide is for you.

        In this guide, we will walk through the entire journey – from a single artificial neuron to building your own image recognizer and text generator. There are lots of examples, and working Python code you can actually run.

        **What you will learn:**  
        - How a neural network "thinks" and learns from its mistakes  
        - Why deep networks need special tricks like dropout and skip connections  
        - How CNNs see the world (and why they're amazing for images)  
        - How RNNs and LSTMs remember things (perfect for text and time series)  
        - Two complete demos: handwritten digit recognition & text generation  

        > Let's build some artificial brains! 
        """
    )
    st.markdown("---")

    # 1. INTRODUCTION TO DEEP LEARNING
    st.header(" Introduction to Deep Learning")
    col1, col2 = st.columns(2)
    with col1:
        st.write(
            """
            **What makes it "deep"?**  
            Traditional machine learning needs humans to tell it what features to look for (like "edges" or "corners").  
            Deep learning figures out those features by itself, layer by layer:

            - **Low layers** see simple things: edges, colours, textures  
            - **Middle layers** combine them into shapes: eyes, wheels, windows  
            - **High layers** recognize complete objects: cats, cars, faces  

            This automatic feature learning is the superpower of deep networks.
            """
        )
    with col2:
        st.write(
            """
            **A quick timeline:**  
            - 1950s: First artificial neurons  
            - 1980s: Back propagation (learning from mistakes)  
            - 2012: AlexNet wins ImageNet – deep learning explodes  
            - Today: Transformers, diffusion models, GPTs  

            **What you need to follow along:**  
            - Basic Python (loops, functions, lists)  
            - Curiosity and patience – deep learning is a journey, not a sprint!
            """
        )
    st.markdown("---")

    # 2. NEURAL NETWORKS & FORWARD PROPAGATION
    st.header(" Neural Networks & Forward Propagation")
    st.write(
        """
        A neural network is just a bunch of tiny calculators (neurons) connected together.  
        Each neuron takes several inputs, multiplies each by a **weight** (how important it is), adds them up, and then decides whether to "fire" using an **activation function**.
        """
    )
    # Table of activation functions (simple)
    act_df = pd.DataFrame({
        "Activation": ["ReLU", "Sigmoid", "Tanh", "Softmax"],
        "What it does": [
            "Outputs input if positive, otherwise zero. Very fast, no vanishing gradient.",
            "Squeezes numbers between 0 and 1 – great for probabilities.",
            "Squeezes between -1 and 1 – used in older networks.",
            "Turns outputs into probabilities that sum to 1 – used for multi‑class classification."
        ],
        "Most used in": ["Hidden layers (default)", "Output layer (binary classification)", "Rarely now", "Output layer (multi‑class)"]
    })
    st.dataframe(act_df, use_container_width=True, hide_index=True)

    st.write(
        """
        **Forward propagation** is the one‑way trip from input to output.  
        Imagine pixels flowing through layers, getting transformed at each step, until a prediction pops out.

        Why do we need **non‑linear** activation functions like ReLU?  
        Without them, stacking layers would be useless – the whole network would collapse into a single straight line. Non‑linearity lets it learn curves and complex shapes.
        """
    )
    st.markdown("---")

    # 3. BACKPROPAGATION & OPTIMIZATION
    st.header(" Backpropagation & Optimization – How Networks Learn")
    st.write(
        """
        When the network makes a wrong prediction, we need to tell it: *"Hey, you were wrong – please adjust your weights!"*  
        The algorithm that figures out **how much each weight contributed** to the mistake is called **backpropagation**.

        Think of it like this: you throw a dart and miss the bullseye. You don't move your arm randomly – you think backward: *"I aimed too high and too left, so next time I'll aim lower and right."*  
        Back propagation does exactly that for every weight in the network.
        """
    )
    st.info(
        """
        **Gradient descent** is the optimizer that actually changes the weights.  
        Imagine you're in a foggy valley and you want to reach the lowest point. You feel the slope under your feet and take a small step downhill.  
        - **Learning rate** = size of your step (too big → overshoot, too small → very slow)  
        - **Adam** is the most popular optimizer – it adapts the step size automatically.
        """
    )
    st.markdown("---")

    # 4. DEEP NETWORKS & REGULARIZATION
    st.header(" Deep Neural Networks & Regularization")
    st.write(
        """
        More layers = more power, but also more problems:
        - **Overfitting** – the network memorizes the training data instead of learning general rules  
        - **Vanishing gradients** – the error signal fades to nothing as it travels back through many layers  
        - **Slow training**

        Here's how we fix those issues.
        """
    )
    with st.expander(" Regularization Tricks", expanded=False):
        st.markdown(
            """
            - **Dropout:** Randomly turn off 50% of neurons during training. This forces the network to learn redundant, robust features – like practicing a sport with a handicap.  
            - **Early Stopping:** Keep an eye on validation loss. As soon as it stops improving, stop training. No point in over‑learning.  
            - **Data Augmentation:** Create more training data by flipping, rotating, or slightly changing images. A cat is still a cat upside‑down!  
            - **Batch Normalization:** Normalizes the outputs of each layer, making training faster and more stable. It's in almost every modern network.
            """
        )
    with st.expander(" Residual Networks (ResNets) – The Game Changer", expanded=False):
        st.write(
            """
            How do you train a network with 150 layers? The secret is **skip connections**.  
            Instead of learning a completely new transformation, a residual block learns only the **difference** between input and output – a small adjustment.  
            The gradient can flow directly through the shortcut, solving the vanishing gradient problem.  
            ResNets are still widely used today in computer vision.
            """
        )
    st.markdown("---")

    # 5. CONVOLUTIONAL NEURAL NETWORKS (CNN)
    st.header(" Convolutional Neural Networks – How AI Sees Images")
    st.write(
        """
        If you connect every pixel to every neuron, you get billions of parameters – impossible to train.  
        CNNs use three clever ideas to make image processing practical:

        1. **Local connectivity** – each neuron looks only at a small patch (like a 3×3 window)  
        2. **Weight sharing** – the same small pattern detector (filter) slides across the whole image  
        3. **Pooling** – shrink the image by taking the max or average in small regions (adds robustness to position changes)

        A typical CNN looks like:  
        **Input → [Conv + ReLU + Pool] repeated → Flatten → Fully Connected → Output**
        """
    )
    arch_df = pd.DataFrame({
        "Architecture": ["LeNet-5", "AlexNet", "VGG16", "ResNet", "Inception"],
        "Year": ["1998", "2012", "2014", "2015", "2015"],
        "Key Innovation": [
            "First practical CNN for digits",
            "ReLU, Dropout, GPU training – won ImageNet",
            "Very uniform, only 3×3 convolutions",
            "Skip connections – up to 152 layers",
            "Multi‑scale convolutions in parallel"
        ]
    })
    st.dataframe(arch_df, use_container_width=True, hide_index=True)
    st.markdown("---")

    # 6. CNN DEMO
    st.header(" CNN Demo: Handwritten Digit Recognition (MNIST)")
    st.write(
        """
        Let's build a real CNN that recognizes handwritten digits (0‑9).  
        We will use PyTorch – but the same ideas work in TensorFlow or even plain NumPy.
        """
    )
    with st.expander(" Full PyTorch Code for CNN Demo", expanded=True):
        st.code(
            """
import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

# Load and normalize MNIST
transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
train_set = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
train_loader = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)

# Define a simple CNN
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, padding=1)  # 1 input channel (grayscale)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 7 * 7, 128)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.pool1(self.relu1(self.conv1(x)))
        x = self.pool2(self.relu2(self.conv2(x)))
        x = x.view(x.size(0), -1)
        x = self.relu3(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Train for one epoch
model.train()
for images, labels in train_loader:
    optimizer.zero_grad()
    outputs = model(images)
    loss = criterion(outputs, labels)
    loss.backward()
    optimizer.step()
    print(f'Loss: {loss.item():.4f}', end='\\r')

print("\\nTraining complete!")

# Test on unseen data
model.eval()
test_set = torchvision.datasets.MNIST(root='./data', train=False, transform=transform)
test_loader = torch.utils.data.DataLoader(test_set, batch_size=64)
correct = total = 0
with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
print(f'Test accuracy: {100 * correct / total:.2f}%')
            """,
            language="python"
        )
    st.success("After 1 minute of training, you will get ~95% accuracy. After 5‑10 epochs, it reaches 99%+. Not bad for a few lines of code!")
    st.markdown("---")

    # 7. RECURRENT NEURAL NETWORKS (RNN)
    st.header(" Recurrent Neural Networks – Adding Memory")
    st.write(
        """
        CNNs are great for images, but what about sentences, music, or stock prices?  
        For sequences, you need **memory**. An RNN has a simple loop: at each time step, it looks at the current input **and** its own previous output – that previous output acts as short‑term memory.

        **The problem:** Simple RNNs forget quickly (vanishing gradient again). After about 10‑20 steps, the signal fades to nothing.
        """
    )
    st.subheader("LSTM & GRU – Long‑term Memory")
    st.write(
        """
        **LSTM** (Long Short‑Term Memory) has a clever internal "cell state" that acts like a conveyor belt.  
        Three little gates (forget, input, output) decide when to write new memories, erase old ones, or read them out.  
        This allows LSTMs to remember things for hundreds of steps.

        **GRU** is a simplified LSTM with only two gates – often works just as well and trains faster.
        """
    )
    st.markdown(
        """
        **Different RNN architectures:**  
        - One‑to‑many: image captioning (one image → sequence of words)  
        - Many‑to‑one: sentiment analysis (movie review → positive/negative)  
        - Many‑to‑many: machine translation (English sentence → French sentence)
        """
    )
    st.info(" **Note:** Since 2017, Transformers (like GPT) have taken over most NLP tasks, but RNNs/LSTMs are still great for small‑scale projects, real‑time applications, and learning the core concepts.")
    st.markdown("---")

    # 8. RNN DEMO
    st.header(" RNN Demo: Character‑Level Text Generator")
    st.write(
        """
        We'll train a small LSTM on a tiny Shakespeare snippet, then let it generate its own "Shakespeare‑like" text.  
        The network learns which characters tend to follow which – no understanding of words, just patterns!
        """
    )
    with st.expander(" PyTorch Code for Text Generation with LSTM", expanded=True):
        st.code(
            """
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Tiny Shakespeare snippet
text = "To be or not to be that is the question Whether it is nobler in the mind to suffer"
chars = sorted(list(set(text)))
char_to_idx = {ch: i for i, ch in enumerate(chars)}
idx_to_char = {i: ch for i, ch in enumerate(chars)}
vocab_size = len(chars)

# Hyperparameters
hidden_size = 128
num_layers = 2
seq_length = 25
learning_rate = 0.005
epochs = 100

class CharRNN(nn.Module):
    def __init__(self, vocab_size, hidden_size, num_layers):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, hidden_size)
        self.lstm = nn.LSTM(hidden_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, x, hidden=None):
        x = self.embedding(x)
        out, hidden = self.lstm(x, hidden)
        out = self.fc(out)
        return out, hidden

    def init_hidden(self, batch_size):
        return (torch.zeros(num_layers, batch_size, hidden_size),
                torch.zeros(num_layers, batch_size, hidden_size))

model = CharRNN(vocab_size, hidden_size, num_layers)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)

# Convert text to indices
data = torch.tensor([char_to_idx[ch] for ch in text], dtype=torch.long)

# Training
for epoch in range(epochs):
    hidden = model.init_hidden(batch_size=1)
    total_loss = 0
    for i in range(0, len(data) - seq_length, seq_length):
        inputs = data[i:i+seq_length].unsqueeze(0)
        targets = data[i+1:i+seq_length+1].unsqueeze(0)
        hidden = (hidden[0].detach(), hidden[1].detach())
        optimizer.zero_grad()
        output, hidden = model(inputs, hidden)
        loss = criterion(output.view(-1, vocab_size), targets.view(-1))
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), 5.0)
        optimizer.step()
        total_loss += loss.item()
    if epoch % 10 == 0:
        print(f'Epoch {epoch}, loss: {total_loss / ((len(data)-seq_length)/seq_length):.4f}')

# Generate text
def generate(model, start_char, length=100):
    model.eval()
    hidden = model.init_hidden(batch_size=1)
    input_idx = torch.tensor([[char_to_idx[start_char]]], dtype=torch.long)
    result = start_char
    for _ in range(length):
        output, hidden = model(input_idx, hidden)
        probs = torch.softmax(output[0, -1], dim=0).detach().numpy()
        next_idx = np.random.choice(range(vocab_size), p=probs)
        result += idx_to_char[next_idx]
        input_idx = torch.tensor([[next_idx]], dtype=torch.long)
    return result

print("\\nGenerated text (starting with 'T'):")
print(generate(model, 'T', length=150))
            """,
            language="python"
        )
    st.caption("Output (will vary each run): *'To be or not to be that is the question whether tis nobler in the mind to suffer and the mind...'*")
    st.markdown("---")

    # 9. GREAT RESOURCES
    st.header(" Great Resources")
    st.write(
        """
        You have made it to the end! Here are the best free resources to continue your deep learning journey.
        """
    )
    res_df = pd.DataFrame({
        "Category": ["Interactive Courses", " Video Lectures", " Written Tutorials", "Practice & Code", " Research & News"],
        "Recommendations": [
            "fast.ai – Practical Deep Learning for Coders\nGoogle's Machine Learning Crash Course\nDeepLearning.AI (Coursera) – free audit",
            "Andrej Karpathy's 'Neural Networks: Zero to Hero'\n3Blue1Brown – Deep Learning series\nYannic Kilcher – paper explanations",
            "d2l.ai – Dive into Deep Learning (free book)\nChris Olah's blog (understanding LSTMs)\nDistill.pub ",
            "Kaggle – Computer Vision & NLP competitions\nHugging Face – transformers library\nPyTorch Tutorials ",
            "arXiv (cs.LG / cs.CV / cs.CL)\nThe Gradient (magazine)\nPapers with Code"
        ]
    })
    st.dataframe(res_df, use_container_width=True, hide_index=True)

    st.markdown(
        """
        **Tips:**  
        - Start with small projects – don't try to train GPT from scratch!  
        - Use Google Colab for free GPUs.  
        - Join online communities: r/MachineLearning, Fast.ai forums, Hugging Face Discord.  
        - Reproduce one classic paper (e.g., LeNet-5 or AlexNet) to truly understand the details.
 
        """
    )
    st.markdown("---")
    st.caption("© 2026 | Deep Learning from Scratch – friendly, practical.")