import asyncio
from bleak import BleakClient, discover
import time
from datetime import datetime

# Modify this variable with the name of the device you want to connect to
device_name = "Emi"

device_data = {}

async def connect_and_disconnect(device_name):
    global device_data

    # Discovering nearby Bluetooth devices
    devices = await discover()

    # Finding the device with the specified name
    target_device = None
    for device in devices:
        if device.name == device_name:
            target_device = device
            break

    if target_device is None:
        print(f"Device '{device_name}' not found.")
        return

    try:
        print(f"Connecting to {device_name}...")
        client = BleakClient(target_device)
        await client.connect()
        print(f"Connected to {device_name}")
        connected_time = datetime.now()
        
        # Here you can collect any other data from the Bluetooth connection
        # For example, you can read characteristics or perform other operations
        
        await client.disconnect()
        print(f"Disconnected from {device_name}")
        
        # Store data in a dictionary
        device_data[device_name] = {
            "connected_time": connected_time,
            # Add other data as needed
        }
        
        # Print or send device data to a database
        print("Device Data:", device_data)

    except Exception as e:
        print(f"An error occurred while connecting to {device_name}: {e}")

async def main():
    while True:
        await connect_and_disconnect(device_name)
        await asyncio.sleep(30)  # Pause for 30 seconds before the next iteration

# Running the program
asyncio.run(main())
