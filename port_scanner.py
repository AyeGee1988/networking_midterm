import socket
import time
from datetime import datetime

def scan_port(host, port, timeout=1):
    """Attempts to connect to a single port. Returns True if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)       # Don't wait forever on closed ports
            result = s.connect_ex((host, port))
            return result == 0          # 0 means connection successful (open)
    except socket.gaierror:
        raise ValueError(f"Cannot resolve hostname: {host}")
    except socket.error as e:
        print(f"  [ERROR] Socket error on port {port}: {e}")
        return False

def scan_range(host, start_port, end_port, delay=0.05):
    """Scans a range of ports on the target host."""
    # Validate port range
    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
        raise ValueError("Ports must be between 1 and 65535")
    if start_port > end_port:
        raise ValueError("Start port must be less than or equal to end port")

    # Print scan header with timestamp
    print(f"\n{'='*50}")
    print(f"  Port Scanner")
    print(f"  Date/Time : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Target    : {host}")
    print(f"  Range     : {start_port} - {end_port}")
    print(f"{'='*50}")

    open_ports = []

    for port in range(start_port, end_port + 1):
        is_open = scan_port(host, port)
        status = "OPEN  <---" if is_open else "closed"
        print(f"  Port {port:5d}: {status}")

        if is_open:
            open_ports.append(port)

        time.sleep(delay)  # Ethical delay between scan attempts

    # Print summary
    print(f"\n{'='*50}")
    print(f"  SCAN COMPLETE")
    print(f"  Open ports found: {open_ports if open_ports else 'None'}")
    print(f"{'='*50}\n")
    return open_ports

def main():
    print("=" * 50)
    print("       Python Port Scanner")
    print("=" * 50)
    print("Authorized targets only:")
    print("  - localhost / 127.0.0.1")
    print("  - scanme.nmap.org")
    print("=" * 50)

    # Get target host from user
    host = input("\nEnter target host: ").strip()

    # Check if target is authorized
    authorized = ['localhost', '127.0.0.1', 'scanme.nmap.org']
    if host not in authorized:
        print(f"\n[WARNING] '{host}' is not an authorized target!")
        confirm = input("Continue anyway? (yes/no): ").strip().lower()
        if confirm != 'yes':
            print("Scan cancelled.")
            return

    # Get port range from user
    try:
        start = int(input("Enter start port: "))
        end   = int(input("Enter end port:   "))
        scan_range(host, start, end)

    except ValueError as e:
        print(f"\n[ERROR] Invalid input: {e}")
    except KeyboardInterrupt:
        print("\n\n[SCANNER] Scan interrupted by user.")

if __name__ == "__main__":
    main()
