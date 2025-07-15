# TODO: Make this a multithreaded scanner (Maybe.)

import socket
import argparse
import time


# Parse command line arguments
parser = argparse.ArgumentParser(description="A script that connects to a port and prints the banner")
parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("port", type=int, help="Target Port", default=25)
parser.add_argument("--wordlist", required=True, help="Path to wordlist")
args = parser.parse_args()

def connect():
    """Creates and returns a fresh SMTP socket connection"""
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((args.target, args.port))
        banner = s.recv(1024).decode(errors="ignore")
        print(f"[+] Connected: {banner.strip()}")
        return s
    except Exception as e:
        print(f"[-] Connection failed: {e}")
        return None
    


def check_user(wordlist_path):
    print("[*] Starting user enumeration using VRFY...")

    with open(wordlist_path) as f:
        usernames = [line.strip() for line in f if line.strip()]

    i = 0
    s = connect()
    while i < len(usernames):
        user = usernames[i]
        try:
            s.sendall(f"VRFY {user}\r\n".encode())
            resp = s.recv(1024).decode(errors="ignore").strip()
            if resp.startswith("252") or resp.startswith("250"):
                print(f"[VALID] {user}: {resp}")
            i += 1  # Only move to next user if request was successful
        except Exception as e:
            print(f"[!] Lost connection during {user}, reconnecting... ({e})")
            try:
                s.close()
            except:
                pass
            time.sleep(1)
            s = connect()

def main():
    check_user(args.wordlist)

if __name__ == "__main__":
    main()

