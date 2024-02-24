import asyncio
from bleak import BleakClient, discover
from datetime import datetime

# Modify this variable with the name of the device you want to connect to
device_name = "Emi"

async def connect_and_disconnect(device_name):
    # Discovering nearby Bluetooth devices
    devices = await discover()

    # Finding the device with the specified name
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device is None:
        print(f"Device '{device_name}' not found.")
        return

    try:
        print(f"Connecting to {device_name}...")

        print(f"Connected to {device_name}")
        await BleakClient(target_device).connect()
        await BleakClient(target_device).disconnect()
        print(f"Disconnected from {device_name}")

    except Exception as e:
        print(f"An error occurred while connecting to {device_name}: {e}")

async def main():
    while True:
        await connect_and_disconnect(device_name)
        await asyncio.sleep(30)  # Pause for 30 seconds before the next iteration

# Running the program
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
