# 🤖 Project: Crypto Prophet AI - A Reinforcement Learning Trading Agent

<p align="center">
  <img src="https://raw.githubusercontent.com/dylanatl15/Crypto-Prophet-AI/main/assets/backtest_results_BTC_USDT_run0006_lr5e-05.png" alt="Graph comparing the AI agent's portfolio growth against a simple buy-and-hold strategy."/>
</p>

### The 10-Year Learning Curve, Solved in Hours.

A professional day trader might take a decade to become profitable, learning through massive losses and thousands of hours staring at charts. They're limited by emotion, fatigue, and the sheer volume of data they can process.

This project asks: what if an AI could do it better? What if it could compress 10 years of market data into a single training session, learning minute-by-minute without sleep or breaks? What if it could execute trades with perfect mathematical risk management, no tunnel vision, and no fear?

This is that agent.

---

## ✨ Key Features

* 🧠 **Reinforcement Learning Core:** Built using **Stable-Baselines3** and a custom **Gymnasium** environment, the agent learns through trial and error over millions of steps.
* ⚡ **High-Frequency Analysis:** Every minute, the agent analyzes a 4-hour window of market data, allowing it to react quickly to market changes.
* 📊 **Indicator-Driven Decisions:** The agent's decisions are based on a suite of proven technical indicators, including **RSI**, **MACD**, and **Bollinger Bands**.
* 📈 **Proven Performance:** In a controlled backtest on a full year of never-before-seen BTC/USD data, the agent achieved an impressive **31.9% profit**.
* 🔌 **Flexible Data Pipeline:** Uses the `ccxt` library to pull data directly from the **Binance API**, allowing it to train a specialized agent for any asset.

---

## 🚀 The Results: 31.9% Return on BTC/USD

Did it work? The numbers speak for themselves.

A backtest was conducted on a full year of **BTC/USD** data that the AI had **never seen** during its training phase. The result was a definitive outperformance of a traditional "buy and hold" strategy.

<p align="center">
  <strong>Total Profit: <span style="color: #2e7d32;">31.9%</span></strong>
</p>

**The Fine Print:** This result was achieved in an idealized, controlled environment to purely test the agent's decision-making core. This simulation assumes:
* No transaction fees or slippage.
* Instantaneous order execution.
* Take-profit and stop-loss levels were managed by the backtesting algorithm, not the agent itself.

The goal was to isolate and validate the agent's core intelligence. The conclusion is clear: the agent learned to consistently identify profitable trading opportunities in unseen data.

---

## 🛠 How It Works

The project is built around a custom reinforcement learning loop. The agent is rewarded for profitable trades and penalized for losses, allowing it to build an intuition for market dynamics over millions of iterations.

1.  **Data Ingestion:** The environment pulls 4 years of 1-minute historical data for a specified asset from Binance. *(Note: This 4-year window was a limitation imposed by the development hardware's RAM, not a limitation of the agent itself. With more powerful hardware, it could process decades of data.)*
2.  **Feature Engineering:** Raw price data (OHLC) is enriched with the following indicators using `pandas_ta`:
    * RSI (14)
    * MACD (12, 26, 9) suite (MACD, MACDh, MACDs)
    * Bollinger Bands (20, 2.0) suite (BBL, BBM, BBU, BBB, BBP)
3.  **Training Loop:** The agent is unleashed on the data. For millions of steps, it makes a choice (`BUY`, `SELL`, or `HOLD`) and its internal neural network is adjusted based on the outcome.
4.  **Validation:** Once trained, the agent's performance is tested on a separate dataset it has never encountered.

---

## 💻 Tech Stack & Environment

* **Primary Language:** Python
* **Core Libraries:**
  * **ML/RL:** `stable-baselines3`, `gymnasium`, `numpy`
  * **Data Handling:** `pandas`, `pandas_ta`, `ccxt`
  * **Utilities:** `argparse`, `tqdm`, `datetime`, `os`
* **Data Source:** Binance API
* **Training Hardware:** NVIDIA RTX 4050 (Laptop GPU), leveraging CUDA for accelerated training.

---

## 🔮 Future Development

This project serves as a powerful proof-of-concept with massive potential. The next steps are clear:

- [ ] **Test Expanded Indicator Set:** Fully backtest the agent with additional indicators that have already been integrated: `AO`, `STOCH`, `ADX`, `Vortex`, `ATR`, and `OBV`.
- [ ] **Develop a Multi-Asset Agent:** Explore techniques to either merge the "knowledge" of individually trained agents or create a single, robust agent that can trade multiple assets by recognizing broader market patterns.
- [ ] **Integrate Realistic Market Conditions:** Factor in transaction costs and slippage to train a more robust and realistic agent.
- [ ] **Grant Agent Full Control:** Allow the agent to learn its own optimal take-profit and stop-loss strategies instead of having them preset by the environment.
- [ ] **Deploy for Live Paper Trading:** The ultimate test. Deploy the agent in a live market environment with paper money to assess its performance in real-time.
