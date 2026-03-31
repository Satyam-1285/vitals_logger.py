import psutil
import csv
import time
from datetime import datetime
import os

def setup_csv(filename):
    """Creates the CSV file and writes the header if it doesn't exist."""
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            # Writing the column headers
            writer.writerow(['Timestamp', 'CPU_Usage(%)', 'RAM_Usage(%)', 'Battery(%)'])
    return filename

def log_system_vitals(filename, duration_seconds=60, interval=5):
    """Logs system hardware stats for a set duration."""
    print(f"Starting hardware logging for {duration_seconds} seconds...")
    print("Press Ctrl+C to stop early.\n")
    
    start_time = time.time()
    
    try:
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            while (time.time() - start_time) < duration_seconds:
                # 1. Get Timestamp
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                
                # 2. Read Hardware Sensors
                cpu_usage = psutil.cpu_percent(interval=1)
                ram_usage = psutil.virtual_memory().percent
                
                # Handle desktop computers that might not have a battery
                battery = psutil.sensors_battery()
                battery_percent = battery.percent if battery else "N/A"
                
                # 3. Log the Data
                writer.writerow([current_time, cpu_usage, ram_usage, battery_percent])
                print(f"Logged -> CPU: {cpu_usage}% | RAM: {ram_usage}% | Battery: {battery_percent}%")
                
                # Wait before the next reading
                time.sleep(interval - 1) # Subtracting 1 because cpu_percent takes 1 second
                
    except KeyboardInterrupt:
        print("\nLogging stopped manually.")
        
    print(f"\n✅ Data successfully saved to {filename}")

if __name__ == "__main__":
    # Define the output file
    log_file = "system_logs.csv"
    
    # Setup the file and start logging (Runs for 1 minute, checking every 5 seconds)
    setup_csv(log_file)
    log_system_vitals(log_file, duration_seconds=60, interval=5)
