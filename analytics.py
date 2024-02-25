import asyncio
import aiomysql
from datetime import datetime, timedelta

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': 3306,
    'user': 'Smartcollar_PROD',
    'password': 'Smartcollar',
    'db': 'smartcollar_db'
}

# Modify this variable with the name of the device you want to track
device_name = "Emi"

# Time threshold (in seconds) before considering the device out of range
time_threshold = 10  # 5 minutes

async def get_last_connected_time(conn):
    async with conn.cursor() as cur:
        await cur.execute("SELECT MAX(connected_time) FROM device_data WHERE device_name = %s", (device_name,))
        result = await cur.fetchone()
        if result[0]:
            return result[0]
        else:
            return None

async def check_device_status():
    while True:
        try:
            # Connect to the database
            async with aiomysql.create_pool(**db_params) as pool:
                async with pool.acquire() as conn:
                    # Retrieve the last connected time of the device
                    last_connected_time = await get_last_connected_time(conn)

                    # Calculate the time difference since the last connection
                    if last_connected_time:
                        current_time = datetime.now()
                        time_difference = current_time - last_connected_time

                        # Check if the device is out of range based on the time threshold
                        if time_difference.total_seconds() >= time_threshold:
                            print(f"The device '{device_name}' is out of range.")
                        else:
                            print(f"The device '{device_name}' is in range.")

                    else:
                        print(f"No records found for the device '{device_name}'.")

        except Exception as e:
            print(f"An error occurred while checking device status: {e}")

        # Pause for a specified interval before checking again
        await asyncio.sleep(30)  # Check every 30 seconds

# Running the program
async def main():
    await check_device_status()

# Run the asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
