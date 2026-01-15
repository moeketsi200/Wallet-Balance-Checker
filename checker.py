from web3 import Web3
import time

# 1. The "Master Key" Connection List
rpc_list = [
    "https://eth.llamarpc.com",
    "https://rpc.flashbots.net",
    "https://1rpc.io/eth",
    "https://cloudflare-eth.com"
]

connected = False
web3 = None

print("--------------------------------")
print("🚀 CONNECTING TO ETHEREUM...")
print("--------------------------------")

# 2. Connection Loop
for url in rpc_list:
    try:
        web3 = Web3(Web3.HTTPProvider(url))
        if web3.is_connected():
            print(f"✅ Connected via {url}")
            connected = True
            break
    except:
        continue

if connected:
    # 3. INTERACTIVE: Ask the user for an address
    # You can paste Vitalik's address again or any other
    user_input = input("\n🔎 Paste an Ethereum Address (or press Enter for Vitalik): ")
    
    # If user presses Enter without typing, use Vitalik's address
    if user_input == "":
        target_address = "0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045"
    else:
        target_address = user_input

    # Clean the address format
    try:
        checksum_address = web3.to_checksum_address(target_address)
        
        # 4. GET DATA
        # Balance
        balance_wei = web3.eth.get_balance(checksum_address)
        balance_eth = web3.from_wei(balance_wei, 'ether')
        
        # Gas Price (The cost to trade)
        gas_wei = web3.eth.gas_price
        gas_gwei = web3.from_wei(gas_wei, 'gwei') # Traders measure Gas in "Gwei"
        
        # Latest Block (The "Time")
        block_number = web3.eth.block_number

        # 5. THE DASHBOARD
        print("\n📊 --- LIVE NETWORK DATA ---")
        print(f"Target:      {checksum_address}")
        print(f"💰 Balance:  {balance_eth:.4f} ETH")
        print(f"⛽ Gas Price: {gas_gwei:.2f} Gwei (Low is < 15, High is > 50)")
        print(f"📦 Block #:   {block_number}")
        print("--------------------------------")
        
    except Exception as e:
        print(f"❌ Invalid Address: {e}")

else:
    print("❌ Could not connect to any node.")
