import subprocess
import socket

def check_connection():
    """
    Prüft die Netzwerkverbindung durch einen Ping zu Googles DNS.
    Gibt ein Tuple zurück: (status, latency_or_error_message, local_ip)
    """
    try:
        # Ping zu Googles DNS
        response = subprocess.run(
            ["ping", "-c", "1", "8.8.8.8"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        # Lokale IP ermitteln
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
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
    Extrahiert die Latenzzeit aus der Ping-Ausgabe.
    Gibt die Latenz in Millisekunden zurück oder "-" falls nicht gefunden.
    """
    for line in ping_output.splitlines():
        if "time=" in line:
            return line.split("time=")[-1].split(" ")[0]
    return "-"

def scan_devices():
    """
    Scannt Geräte im lokalen Netzwerk mithilfe von 'arp'.
    Gibt eine Liste von Strings (IP-Adressen oder Gerätedetails) zurück.
    """
    try:
        # ARP-Tabellen-Befehl ausführen
        result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        if result.returncode != 0:
            return ["Error: ARP command failed"]

        # Ausgabe verarbeiten
        devices = []
        for line in result.stdout.splitlines():
            if "at" in line:  # Beispielhafter Filter
                devices.append(line.strip())
        return devices
        

    except FileNotFoundError:
        # ARP-Tool nicht gefunden
        return ["Error: 'arp' tool not found. Please install it."]
    except Exception as e:
        # Allgemeiner Fehler
        return [f"Unexpected error: {e}"]
