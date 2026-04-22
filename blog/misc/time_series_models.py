import streamlit as st
import pandas as pd

TITLE = "Time Series Forecasting: From ARIMA to LSTMs"
CATEGORY = "misc"
KEYWORDS = ["time series", "forecasting", "ARIMA", "LSTM", "stationarity", "differencing", "seasonality", "resampling", "sliding window", "multivariate forecasting", "deep learning"]


def show():

    st.title("Time Series Forecasting: From ARIMA to LSTMs")
    st.caption("Category: time_series | Level: Intermediate")
    st.markdown("---")
    
    # INTRO
    st.write(
        """
        If you’ve been working in data science for a while, chances are you’ve encountered time series problems. 
        They’re everywhere—sales forecasts, server metrics, stock prices, and IoT sensor streams. While classical 
        models like ARIMA still power many production systems, deep learning approaches like LSTMs are now serious 
        contenders when you have enough data and non‑linear patterns to model.
        
        This guide walks you through essential concepts, practical code snippets, and the key trade‑offs you’ll face—
        from basic datetime wrangling to building univariate and multivariate LSTMs. It’s written for someone who’s 
        already comfortable with Python, pandas, and scikit‑learn, but wants to level up their time series game.
        """
    )
    
    # ============================================
    # SECTION: What Exactly Is a Time Series?
    # ============================================
    st.header("What Exactly Is a Time Series?")
    
    st.write(
        """
        At its core, a time series is a sequence of data points recorded at successive, equally‑spaced timestamps. 
        Every time series can be thought of as a combination of several underlying components:
        
        - **Trend** – the long‑term direction (upward, downward, or flat).
        - **Seasonality** – repeating patterns at fixed intervals (daily, weekly, yearly).
        - **Cyclic** – fluctuations without a fixed period, such as economic booms and busts.
        - **Noise** – the random leftover variation after removing the first three.
        
        For an intermediate data scientist: always decompose your series before modelling. It will save you from 
        many silly mistakes and help you choose the right tools.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Datetime Conversion and Indexing
    # ============================================
    st.header("Getting Your Data Ready: Datetime Conversion and Indexing")
    
    st.write(
        """
        Pandas is your best friend here. Most raw data comes with date strings, and the first thing you should do 
        is convert them to a proper datetime type and set the column as the index.
        """
    )
    
    st.code(
        """
import pandas as pd

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d %H:%M:%S')
df.set_index('date', inplace=True)
        """,
        language="python"
    )
    
    st.write(
        """
        Once the index is a `DatetimeIndex`, magic happens. You can select data using familiar string notation:
        """
    )
    
    st.code(
        """
df.loc['2023-01-01']          # single timestamp
df.loc['2023-01']              # all of January 2023
df.loc['2023-01-01':'2023-01-31']  # slice between dates
        """,
        language="python"
    )
    
    st.info("**Pro tip**: Always make a copy before slicing if you plan to modify the data – chained indexing can lead to unexpected behaviour.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Time-Based Filtering and Slicing
    # ============================================
    st.header("Time‑Based Filtering and Slicing")
    
    st.write(
        """
        Beyond simple indexing, you can use boolean conditions or the `.between` method to filter your data:
        """
    )
    
    st.code(
        """
# After a certain date
df[df.index > '2023-06-01']

# Between two dates (inclusive)
df['2023-01-01':'2023-06-30']

# Using .between on the index (converted to a series)
df[df.index.to_series().between('2023-01-01', '2023-06-30')]
        """,
        language="python"
    )
    
    st.write("For production pipelines, explicit `.loc` with clear start and end dates is more readable and less error‑prone.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Resampling
    # ============================================
    st.header("Resampling: Changing the Observation Frequency")
    
    st.write(
        """
        Resampling is essential when your raw data is too granular (seconds or minutes) or too sparse. 
        You can either **downsample** (reduce frequency) or **upsample** (increase frequency).
        """
    )
    
    st.code(
        """
# Downsample – reduce frequency
monthly_avg = df.resample('M').mean()   # monthly average
yearly_sum  = df.resample('Y').sum()    # yearly sum

# Upsample – increase frequency (requires filling)
hourly_filled = df.resample('H').ffill()   # forward fill
        """,
        language="python"
    )
    
    st.write(
        """
        Common offset aliases: `'D'` (daily), `'H'` (hourly), `'W'` (weekly), `'M'` (month end), `'Q'` (quarter), `'Y'` (year). 
        When upsampling, `ffill` or `interpolate` are your go‑to methods – avoid `bfill` unless you have a very good reason.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Real-Life Examples
    # ============================================
    st.header("Real‑Life Examples You’ll Recognise")
    
    st.write(
        """
        Time series problems come in many flavours. Here are a few you’ve likely encountered:
        
        - **Temperature** – hourly readings from a weather station, typically showing trend and strong daily seasonality.
        - **Energy usage** – minute‑level smart meter data with weekly and daily patterns, often affected by holidays.
        - **Sales** – daily transactions of an online store, influenced by promotions and day‑of‑week effects.
        - **Web traffic** – number of visits per hour, which can spike after marketing campaigns.
        - **Alerts** – system log counts per minute, often bursty and requiring anomaly detection.
        
        These will appear again when we talk about LSTM applications.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Plotting Time Series
    # ============================================
    st.header("Plotting Time Series (Don’t Skip This)")
    
    st.write("Always, always visualise first. Matplotlib works perfectly with datetime indices.")
    
    st.code(
        """
import matplotlib.pyplot as plt

plt.figure(figsize=(12,4))
plt.plot(df.index, df['value'])
plt.title('My Time Series')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)
plt.show()
        """,
        language="python"
    )
    
    st.write("For multiple columns or a quick inspection, you can use pandas’ built‑in plot method:")
    
    st.code(
        """
df[['temp', 'humidity']].plot(subplots=True, figsize=(12,6))
        """,
        language="python"
    )
    
    st.info("**Intermediate insight**: Overlaying rolling statistics (e.g., a rolling mean) helps you spot non‑stationarity instantly.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Stationarity and Differencing
    # ============================================
    st.header("Stationarity and the Concept of Differencing")
    
    st.write(
        """
        A **stationary** series has constant mean, variance, and autocorrelation over time. Most classical models 
        (including ARIMA) require stationarity because predicting a non‑stationary series is like trying to hit a 
        moving target – your coefficients won’t generalise.
        
        **Differencing** is the primary technique for removing trend and seasonality:
        
        - First difference: `y_t' = y_t - y_{t-1}`
        - Seasonal difference: `y_t' = y_t - y_{t-m}` (where `m` is the season length, e.g., 12 for monthly data)
        """
    )
    
    st.code(
        """
df['diff_1'] = df['value'].diff()          # first order
df['diff_12'] = df['value'].diff(12)       # seasonal difference
        """,
        language="python"
    )
    
    st.write("After differencing, always replot and re‑test for stationarity.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Checking Stationarity
    # ============================================
    st.header("How to Check for Stationarity")
    
    st.write(
        """
        **Visual inspection** is your first line of defence. Plot the raw series along with its rolling mean 
        and rolling standard deviation. If they vary wildly, the series is likely non‑stationary.
        
        For a more rigorous test, use the **Augmented Dickey‑Fuller (ADF) test**. Its null hypothesis is that 
        the series is **non‑stationary**, so a low p‑value (below 0.05) is what you want.
        """
    )
    
    st.code(
        """
from statsmodels.tsa.stattools import adfuller

result = adfuller(df['value'])
print(f'ADF statistic: {result[0]:.3f}')
print(f'p-value: {result[1]:.3f}')
if result[1] <= 0.05:
    print("Reject H0 → series is stationary")
else:
    print("Cannot reject H0 → non‑stationary, try differencing")
        """,
        language="python"
    )
    
    st.warning("**Warning**: The ADF test can be sensitive to strong seasonal components. If you see clear seasonality, apply seasonal differencing before testing.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: ARIMA Model Steps
    # ============================================
    st.header("ARIMA Model: Steps to Build One")
    
    st.write(
        """
        ARIMA(p,d,q) stands for **AutoRegressive Integrated Moving Average**. The three parameters control:
        
        - **p** – number of autoregressive lags (using past values of the series)
        - **d** – degree of differencing needed to achieve stationarity
        - **q** – number of moving average lags (using past forecast errors)
        
        Here’s a step‑by‑step workflow:
        
        1. **Visualise** the series – plot it, look for trend and seasonality.
        2. **Make it stationary** – apply differencing `d` and confirm with the ADF test.
        3. **Identify p and q** using ACF and PACF plots:  
           - ACF cuts off after lag `q` → MA(q)  
           - PACF cuts off after lag `p` → AR(p)
        4. **Fit the model** using `statsmodels`:
        """
    )
    
    st.code(
        """
from statsmodels.tsa.arima.model import ARIMA
model = ARIMA(df['value'], order=(p,d,q))
fitted = model.fit()
print(fitted.summary())
        """,
        language="python"
    )
    
    st.write(
        """
        5. **Diagnose residuals** – they should look like white noise (no autocorrelation, zero mean). Use the Ljung‑Box test.
        6. **Forecast**:
        """
    )
    
    st.code(
        """
forecast = fitted.forecast(steps=12)
        """,
        language="python"
    )
    
    st.info("**Intermediate note**: For seasonal data, use **SARIMA** – it adds seasonal `(P,D,Q,m)` parameters. If you don’t want to manually search over parameters, libraries like `pmdarima` offer auto‑ARIMA functionality, but always sanity‑check the results with visual inspection.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Forecasting Principles
    # ============================================
    st.header("Forecasting Principles You Should Live By")
    
    st.write(
        """
        - **Not all series are forecastable** – too much noise or structural breaks will ruin any model.
        - **Always do out‑of‑sample evaluation** – split your data chronologically into training, validation, and test sets (e.g., 70/15/15).
        - **Backtest** – simulate historical forecasts to see how your model would have performed in the past.
        - **Choose error metrics wisely** – MAE, RMSE, MAPE, and sMAPE all have their pros and cons. MAPE is popular but fails when values are near zero.
        - **Provide prediction intervals** – a point forecast without uncertainty is almost useless in production.
        - **Incorporate domain knowledge** – holidays, promotions, and weather often matter more than model complexity.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Real-Life Applications Table
    # ============================================
    st.header("Real‑Life Applications of Forecasting")
    
    app_data = {
        "Domain": ["Temperature", "Energy usage", "Sales", "Web traffic", "Alerts"],
        "Example": ["Next‑day max temperature", "Hourly load for next 24h", "Weekly product demand", "Requests per minute next hour", "Error log count in next 5 minutes"],
        "Typical Model Choice": ["SARIMA, Prophet, LSTM", "LSTM (multivariate), SARIMAX", "ARIMA + holiday dummies, LightGBM", "LSTM, TBATS, Prophet", "LSTM, Poisson GLM, Hawkes processes"]
    }
    df_apps = pd.DataFrame(app_data)
    st.dataframe(df_apps, use_container_width=True)
    
    st.write("Beyond this list, you’ll find time series forecasting in finance (volatility), healthcare (patient vitals), transportation (traffic flow), and manufacturing (predictive maintenance).")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Concept of Seasonality
    # ============================================
    st.header("Concept of Seasonality (It’s More Than “Repeats”)")
    
    st.write(
        """
        Seasonality is a fixed‑period pattern that repeats at regular intervals. You can detect it by:
        
        - **Seasonal subseries plots** – group by hour, day, or month and plot each group.
        - **Autocorrelation function (ACF)** – look for peaks at lags that are multiples of the season length (e.g., lag 24 for hourly data with daily seasonality).
        - **Decomposition** – additive or multiplicative:
        """
    )
    
    st.code(
        """
from statsmodels.tsa.seasonal import seasonal_decompose
decomp = seasonal_decompose(df['value'], model='additive', period=24)
decomp.plot()
        """,
        language="python"
    )
    
    st.write("**Handling seasonality** in models: seasonal differencing, dummy variables, Fourier terms, or seasonal ARIMA (SARIMA). LSTMs can learn seasonality automatically if you feed them enough cycles.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: LSTM Intuition
    # ============================================
    st.header("LSTM Models – The Intuition")
    
    st.write(
        """
        Long Short‑Term Memory (LSTM) is a type of recurrent neural network designed to avoid the vanishing gradient problem. 
        It maintains a **cell state** that acts like a memory highway, with three gates controlling the flow of information:
        
        - **Forget gate** – decides what to discard from the previous state.
        - **Input gate** – decides what new information to store.
        - **Output gate** – decides what to output based on the current cell state.
        
        **Why use LSTM over ARIMA?**  
        - It handles non‑linear patterns naturally.  
        - It can learn long dependencies (e.g., a weekly pattern from 7 days of hourly data).  
        - It supports multivariate inputs seamlessly.  
        - It works well with irregular patterns if you have enough data.
        
        But LSTM is not magic: you need **more data**, careful hyperparameter tuning, and proper normalisation to get good results.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Sequence Modeling
    # ============================================
    st.header("Sequence Modeling with LSTMs")
    
    st.write(
        """
        Sequence modelling is the task of predicting the next element(s) given previous ones. For time series, 
        you typically use a **sliding window** approach:
        
        - **Many‑to‑one** forecasting: input `[x_{t-w}, x_{t-w+1}, ..., x_{t-1}]` → output `x_t`
        - **Many‑to‑many** forecasting: input a window → output a vector of future steps `[x_t, x_{t+1}, ..., x_{t+k-1}]`
        
        In Keras/TensorFlow, the shape convention is `(batch_size, timesteps, n_features)`.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Normalisation
    # ============================================
    st.header("Normalise Time Series Data")
    
    st.write(
        """
        Neural networks hate unscaled inputs. Always normalise **inside the training data only** to avoid data leakage. 
        Common choices:
        
        - **Min‑Max scaling** (to [0,1] or [-1,1]) – good when the distribution is bounded.
        - **Standardisation** (zero mean, unit variance) – robust to outliers.
        """
    )
    
    st.code(
        """
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0,1))
df['scaled'] = scaler.fit_transform(df[['value']])
        """,
        language="python"
    )
    
    st.info("**Pro tip**: For multivariate series, fit separate scalers per feature, or use a single scaler on the whole matrix if the features are on similar scales. Remember to inverse‑transform your predictions for interpretation.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Sliding Windows
    # ============================================
    st.header("Implement Sliding Windows (The Workhorse of LSTM Prep)")
    
    st.write("Convert your time series into supervised learning samples with a simple function:")
    
    st.code(
        """
import numpy as np

def create_sequences(data, window_size):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

window = 24   # use past 24 hours to predict next hour
X, y = create_sequences(df['scaled'].values, window)

# Reshape for LSTM: (samples, timesteps, features)
X = X.reshape((X.shape[0], X.shape[1], 1))
        """,
        language="python"
    )
    
    st.write("For multivariate data, your `data` array should already have shape `(samples, window_size, n_features)` – you can stack multiple columns before calling the function.")
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Build and Train LSTM
    # ============================================
    st.header("Build and Train Univariate and Multivariate LSTM Models")
    
    st.subheader("Univariate LSTM (single input series)")
    
    st.code(
        """
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(50, activation='relu', input_shape=(window, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)
        """,
        language="python"
    )
    
    st.subheader("Multivariate LSTM")
    
    st.write(
        """
        Suppose you have features `['temp', 'humidity', 'hour_sin', 'hour_cos']` and you want to predict `temp` next hour.
        """
    )
    
    st.code(
        """
# X_train shape: (samples, window, n_features)
# y_train shape: (samples, 1) – target is still the variable you care about

model = Sequential([
    LSTM(64, activation='relu', input_shape=(window, n_features)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.1)
        """,
        language="python"
    )
    
    st.write(
        """
        **Training tips for intermediate users**:
        
        - Use **early stopping** (`keras.callbacks.EarlyStopping`) to avoid overfitting.
        - Add **dropout** (e.g., `LSTM(64, dropout=0.2)`) for regularisation.
        - If your validation loss plateaus, reduce the learning rate with `ReduceLROnPlateau`.
        - For multi‑step forecasting (e.g., next 24 hours), you can use a `Dense(24)` output layer or a sequence‑to‑sequence architecture.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Two End-to-End Projects
    # ============================================
    st.header("Two End‑to‑End Projects to Clone and Learn From")
    
    st.write(
        """
        Theory is important, but nothing beats building something yourself. Here are two complete projects 
        you can clone, run, and adapt to your own use cases.
        """
    )
    
    st.subheader("Project 1: Weather Forecast with Custom PyTorch LSTM")
    st.write(
        """
        **Repository:** [WeatherForecast](https://github.com/Runoi/WeatherForecast) by Runoi
        
        This project implements a full **end‑to‑end pipeline** for collecting, storing, analysing, and forecasting 
        weather data. It demonstrates how to build a production‑ready solution from scratch, starting with a custom 
        parallel web scraper and ending with a tournament of three forecasting models.
        
        **What makes this project stand out:**
        
        - **Industrial‑grade web scraper** – built with `requests` and `ThreadPoolExecutor`, featuring retry mechanisms 
          with exponential backoff and direct parsing from embedded JavaScript objects.
        - **Advanced feature engineering** – cyclic encoding (sine/cosine transformation for day of year, month, wind direction) 
          and lag features based on ACF/PACF analysis.
        - **Model tournament** – compares ARIMA, N‑BEATS, and a custom PyTorch LSTM.
        - **Professional training loop** – learning rate scheduler and early stopping.
        
        **The results:** The custom LSTM dramatically outperformed both ARIMA and N‑BEATS, achieving a Mean Absolute Error 
        of around **2.9°C** compared to **10.0–11.3°C** for ARIMA.
        
        **Why this project is valuable:** It shows how proper feature engineering and a well‑implemented LSTM can outperform 
        both classical models and off‑the‑shelf deep learning solutions.
        """
    )
    
    st.subheader("Project 2: Demand Forecasting with Prophet and N‑Beats")
    st.write(
        """
        **Repository:** [Demand Forecasting App](https://github.com/Sid3503/Demand-Forecasting) by Sid3503
        
        This project is a **Streamlit‑based web application** for demand forecasting that combines the strengths of 
        two powerful models – Prophet and N‑Beats – and even integrates Gemini AI for intelligent pattern detection.
        
        **Key features:**
        
        - **Multi‑model forecasting** – Prophet (automatic seasonality detection, holiday effects) and N‑Beats (deep neural architecture).
        - **Interactive analysis** – upload a CSV with `Date` and `Sales` columns, select a forecast horizon, and view interactive charts.
        - **AI‑powered insights** – a Gemini bot provides image‑based trend analysis and data‑based Q&A.
        - **Export options** – download forecasts as CSV and save visualisations.
        
        **Why this project is valuable:** It’s a complete, deployment‑ready application that showcases how to wrap time series 
        models into a user‑friendly interface, making your forecasts accessible to non‑technical stakeholders.
        
        **Getting started:** Clone the repo, install dependencies from `requirements.txt`, set up a `.env` file with your Google 
        API key (optional), and run `streamlit run multipage.py`.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # SECTION: Online Resources
    # ============================================
    st.header("Online Resources")
    
    st.markdown(
        """
        - **[StatsForecast End‑to‑End Walkthrough](https://github.com/Nixtla/statsforecast)** – Step‑by‑step guide to building 
          production‑ready forecasting pipelines for multiple time series, including cross‑validation and model selection.
        - **[Nixtla’s Documentation](https://nixtla.github.io/statsforecast/)** – Tutorials on scaling forecasts to millions of series, 
          handling multiple seasonalities, and using exogenous variables.
        """
    )
    
    st.markdown("---")
    
    # ============================================
    # CONCLUSION
    # ============================================
    st.header("Summary")
    
    st.write(
        """
        You’ve now got a mental map: from cleaning timestamps and checking stationarity, through ARIMA’s structured steps, 
        to LSTM’s sequence modelling power. The key is to match the method to the problem – classical statistics for 
        interpretability and small data, deep learning for large, non‑linear, multivariate series.
        
        Whenever you start a new forecasting project, remember: **visualise, decompose, baseline, then iterate**. 
        And always, always validate on out‑of‑sample data.
        
        Now go forth and forecast – just don’t forget the prediction intervals. 
        """
    )
    
    st.markdown("---")
    
    # Optional: add a footer
    st.caption("This article is part of the Time Series series. For more, visit the online resources above.")