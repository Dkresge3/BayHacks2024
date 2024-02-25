import asyncio
import aiomysql
from bleak import BleakClient, discover
from datetime import datetime

# Modify this variable with the name of the device you want to connect to
device_name = "Emi"

async def connect_and_disconnect(device_name, pool):
    # Discovering nearby Bluetooth devices
    devices = await discover()

    # Finding the device with the specified name
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device is None:
        print(f"Device '{device_name}' not found.")
        return

    try:
        print(f"Connecting to {device_name}...")
        try:
            await BleakClient(target_device).disconnect()
        finally:
            await BleakClient(target_device).connect()
            print(f"Connected to {device_name}")
            connected_time = datetime.now()
            await BleakClient(target_device).disconnect()
            print(f"Disconnected from {device_name}")

            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    # Insert device data into MySQL database
                    await cur.execute("INSERT INTO device_data (device_name, connected_time) VALUES (%s, %s)", (device_name, connected_time))
                    await conn.commit()
    except Exception as e:
        print(f"An error occurred while connecting to {device_name}: {e}")


async def main():
    # Create a connection pool to MySQL database
    pool = await aiomysql.create_pool(host='localhost', port=3306,
                                      user='Smartcollar_PROD', password='Smartcollar',
                                      db='smartcollar_db', loop=loop)

    while True:
        await connect_and_disconnect(device_name, pool)
        await asyncio.sleep(30)  # Pause for 30 seconds before the next iteration

# Running the program
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
