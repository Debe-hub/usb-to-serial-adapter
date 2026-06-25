import serial
import time
import sys

# Configuration
PORT = '/dev/tty.usbserial'  # Mac default - change to COM3 etc for Windows
BAUD_RATE = 9600
TIMEOUT = 1

def test_serial_connection(port, baud_rate):
    """Test USB to Serial adapter with loopback test."""
    print(f"Attempting to connect on {port} at {baud_rate} baud...")
    
    try:
        # Open serial connection
        ser = serial.Serial(port, baud_rate, timeout=TIMEOUT)
        print(f"Connected successfully on {port}")
        
        # Send test message
        test_message = b"Hello from CP2102N!"
        ser.write(test_message)
        print(f"Sent: {test_message.decode()}")
        
        # Read response
        time.sleep(0.1)
        response = ser.read(len(test_message))
        
        if response == test_message:
            print(f"Received: {response.decode()}")
            print("Loopback test PASSED")
        else:
            print("Loopback test FAILED — check TX/RX jumper")
            
        ser.close()
        
    except serial.SerialException as e:
        print(f"Connection failed: {e}")
        print("Check that the adapter is connected and port is correct")
        sys.exit(1)

def simulate_mode():
    """Run simulation without hardware for demonstration."""
    print("Running in simulation mode (no hardware required)")
    print("-" * 40)
    
    test_message = "Hello from CP2102N!"
    print(f"Simulating send: {test_message}")
    time.sleep(0.5)
    print(f"Simulating receive: {test_message}")
    time.sleep(0.5)
    print("Loopback test PASSED (simulated)")
    print("-" * 40)
    print("To run with hardware:")
    print("1. Connect USB to Serial adapter")
    print("2. Short TX and RX pins on FTDI header")
    print(f"3. Update PORT variable to your port")
    print("4. Run: python serial_test.py --hardware")

if __name__ == "__main__":
    if "--hardware" in sys.argv:
        test_serial_connection(PORT, BAUD_RATE)
    else:
        simulate_mode()
