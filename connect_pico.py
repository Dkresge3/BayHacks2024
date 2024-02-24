import asyncio
import aiomysql
from bleak import BleakClient, discover
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)  # Set logging level to DEBUG

# Modify this variable with the name of the device you want to connect to
device_name = "Emi"

async def connect_and_disconnect(device_name, pool):
    # Discovering nearby Bluetooth devices
    devices = await discover()

    # Finding the device with the specified name
    target_device = next((device for device in devices if device.name == device_name), None)

    if target_device is None:
        logging.error(f"Device '{device_name}' not found.")
        return

    try:
        logging.info(f"Connecting to {device_name}...")
        async with BleakClient(target_device) as client:
            await client.connect()
            logging.info(f"Connected to {device_name}")
            connected_time = datetime.now()
            await client.disconnect()
            logging.info(f"Disconnected from {device_name}")

            async with pool.acquire() as conn:
                async with conn.cursor() as cur:
                    # Insert device data into MySQL database
                    await cur.execute("INSERT INTO device_data (device_name, connected_time) VALUES (%s, %s)", (device_name, connected_time))
                    await conn.commit()
    except Exception as e:
        logging.exception(f"An error occurred while connecting to {device_name}: {e}")

async def main():
    # Create a connection pool to MySQL database
    pool = await aiomysql.create_pool(host='Smartcollar', port=3306,
                                      user='Smartcollar_PROD', password='Smartcollar',
                                      db='smartcollar_db', loop=loop)

    while True:
        await connect_and_disconnect(device_name, pool)
        await asyncio.sleep(30)  # Pause for 30 seconds before the next iteration

# Running the program
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
