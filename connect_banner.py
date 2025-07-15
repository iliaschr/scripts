import socket
import argparse


# Parse command line arguments
parser = argparse.ArgumentParser(description="A script that connects to a port and prints the banner")
parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("port", type=int, help="Target Port")
args = parser.parse_args()

def send_command(s):
    s.sendall(b"VRFY root\r\n")
    resp = s.recv(1024).decode(error="ignore")
    print("[+] Response:", resp.strip())

def main():
    s = socket.socket()
    s.settimeout(5) # Wait a maximum of 5 secs before giving up
    s.connect((args.target, args.port))

    banner = s.recv(1024).decode(errors="ignore")
    print("[+] Banner:", banner.strip())

    if args.port == 25:
        send_command(s)

    s.close()

if __name__ == "__main__":
    main()

