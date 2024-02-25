import asyncio
import aiomysql
from datetime import datetime, timedelta
import subprocess

# Database connection parameters
db_params = {
    'host': 'localhost',
    'port': 3306,
    'user': 'Smartcollar_PROD',
    'password': 'Smartcollar',
    'db': 'smartcollar_db'
}

# Modify this list with the names of the devices you want to track
device_names = ["Emi", "Butch"]

# Time threshold (in seconds) before considering the device out of range
time_threshold = 60 * 2  # 2 minutes

async def get_last_connected_time(conn, device_name):
    async with conn.cursor() as cur:
        await cur.execute("SELECT MAX(connected_time) FROM device_data WHERE device_name = %s", (device_name,))
        result = await cur.fetchone()
        if result[0]:
            return result[0]
        else:
            return None

async def check_device_status(device_name):
    while True:
        try:
            # Connect to the database
            async with aiomysql.create_pool(**db_params) as pool:
                async with pool.acquire() as conn:
                    # Retrieve the last connected time of the device
                    last_connected_time = await get_last_connected_time(conn, device_name)

                    # Calculate the time difference since the last connection
                    if last_connected_time:
                        current_time = datetime.now()
                        time_difference = current_time - last_connected_time

                        # Check if the device is out of range based on the time threshold
                        if time_difference.total_seconds() >= time_threshold:
                            try:
                                # Run the curl command and capture its output
                                reset_timer_command = f"curl localhost:5000/reset_timer/{device_name}"
                                subprocess.check_output(reset_timer_command, shell=True, text=True)
                                print(f"The device '{device_name}' is out of range.")
                            finally:
                                pass
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
    tasks = [check_device_status(device_name) for device_name in device_names]
    await asyncio.gather(*tasks)

# Run the asyncio event loop
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
