# Wallet-Balance-Checker

# 🕵️ Ethereum Wallet & Network Monitor

A Python-based tool for checking real-time Ethereum wallet balances and monitoring network health (Gas Prices). Built for Linux environments using `Web3.py`.

## 🚀 Features
* **Multi-Node Connection:** automatically tries multiple RPC providers (LlamaRPC, Flashbots, Cloudflare) to ensure a stable connection.
* **Wallet Inspector:** Converts "Wei" to "Ether" to show human-readable balances.
* **Trading Signal (Gas Price):** Monitors network congestion (Gwei) to help decide when to trade.
* **Vitalik Mode:** Defaults to checking Vitalik Buterin's wallet if no input is provided.

## 🛠️ Prerequisites
You need **Python 3** installed on your system.
This project was built and tested on **Linux Lite**.

## 📦 Installation
1. Open your terminal.
2. Install the required Web3 library:
   ```bash
   pip3 install web3
