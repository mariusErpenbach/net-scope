import subprocess
import socket

def check_connection():
    """
    Checks the network connection by pinging Google's public DNS server.
    Returns a tuple: (status, latency_or_error_message, local_ip)
    """
    try:
        # Ping Google's DNS to check connectivity
        response = subprocess.run(
            ["ping", "-c", "1", "8.8.8.8"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Simulate a connection to an external server to get local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))  # This sends a UDP packet to get the local IP
        local_ip = s.getsockname()[0]
        s.close()

        if response.returncode == 0:
            output = response.stdout.decode()
            latency = extract_latency(output)
            return "Connected", latency, local_ip
        else:
            return "Not connected", "-", local_ip
        
    except Exception as e:
        return "Error", str(e), None

def extract_latency(ping_output):
    """
    Extracts the latency from the ping command's output.
    Returns the latency in milliseconds as a string, or "-" if not found.
    """
    for line in ping_output.splitlines():
        if "time=" in line:
            return line.split("time=")[-1].split(" ")[0]
    return "-"
    