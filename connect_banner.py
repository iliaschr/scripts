# TODO: Reconnect when connection drops, since some smtp servers disconnect after a few failed queries
# TODO: Make this a multithreaded scanner (Maybe.)

import socket
import argparse


# Parse command line arguments
parser = argparse.ArgumentParser(description="A script that connects to a port and prints the banner")
parser.add_argument("target", help="Target IP or hostname")
parser.add_argument("port", type=int, help="Target Port")
parser.add_argument("--wordlist", required=True, help="Path to wordlist")
args = parser.parse_args()


def check_user(s, wordlist):
    print("[*] Starting user enumeration using VRFY...")
    with open(wordlist) as f:
        for user in f:
            user = user.strip()
            s.sendall(f"VRFY {user}\r\n".encode())
            resp = s.recv(1024).decode(errors="ignore")
            print(f"[>] {user}: {resp.strip()}")


def main():
    s = socket.socket()
    s.settimeout(5) # Wait a maximum of 5 secs before giving up
    s.connect((args.target, args.port))

    banner = s.recv(1024).decode(errors="ignore")
    print("[+] Banner:", banner.strip())

    if args.port == 25:
        check_user(s, args.wordlist)

    s.close()

if __name__ == "__main__":
    main()

