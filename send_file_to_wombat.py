import argparse
import os
import subprocess
import sys

# --------------------------------------------------------------------------
# EDIT THESE DEFAULTS TO MATCH YOUR SETUP
# --------------------------------------------------------------------------
DEFAULT_FILEPATH = input("Enter the path to the file you are sending: ")
DEFAULT_HOST = "192.168.125.1"
DEFAULT_SSH_USER = "kipr"
DEFAULT_REMOTE_DIR = "/home/kipr/Documents/KISS/scripts"
DEFAULT_PORT = 22
DEFAULT_KEY = None
# --------------------------------------------------------------------------

def ensure_remote_dir(host, ssh_user, remote_dir, port, key=None):
    """SSH into the remote host and create remote_dir if it doesn't already exist."""
    ssh_cmd = ["ssh", "-p", str(port)]
    if key:
        ssh_cmd += ["-i", key]
    ssh_cmd += [f"{ssh_user}@{host}", f"mkdir -p '{remote_dir}'"]

    print(f"Ensuring remote directory exists: {' '.join(ssh_cmd)}")
    result = subprocess.run(ssh_cmd)

    if result.returncode != 0:
        print(f"Failed to create remote directory (ssh exited with code {result.returncode}).")
        sys.exit(result.returncode)

def transfer_file(local_path, host, ssh_user, remote_dir, port=22, key=None):
    if not os.path.isfile(local_path):
        print(f"Error: file not found: {local_path}")
        sys.exit(1)

    if key and not os.path.isfile(key):
        print(f"Error: key file not found: {key}")
        sys.exit(1)

    # Make sure the target directory exists
    ensure_remote_dir(host, ssh_user, remote_dir, port, key)

    filename = os.path.basename(local_path)
    destination = f"{ssh_user}@{host}:{remote_dir}/{filename}"

    scp_cmd = ["scp", "-P", str(port)]
    if key:
        scp_cmd += ["-i", key]
    scp_cmd += [local_path, destination]

    print(f"Running: {' '.join(scp_cmd)}")
    result = subprocess.run(scp_cmd)

    if result.returncode == 0:
        print(f"Success: copied to {destination}")
    else:
        print(f"Transfer failed (scp exited with code {result.returncode}).")
        sys.exit(result.returncode)

def main():
    parser = argparse.ArgumentParser(
        description="Transfer a file to a Raspberry Pi over SSH using scp."
    )
    parser.add_argument(
        "filepath", nargs="?", default=DEFAULT_FILEPATH,
        help="Path to the local file to transfer"
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="Raspberry Pi IP address or hostname")
    parser.add_argument("--ssh-user", default=DEFAULT_SSH_USER, help="SSH login username on the Pi")
    parser.add_argument(
        "--remote-dir",
        default=DEFAULT_REMOTE_DIR,
        help="Destination directory on the Pi",
    )
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="SSH port")
    parser.add_argument("--key", default=DEFAULT_KEY, help="Path to a private key file for key-based auth")

    args = parser.parse_args()

    transfer_file(
        local_path=args.filepath,
        host=args.host,
        ssh_user=args.ssh_user,
        remote_dir=args.remote_dir,
        port=args.port,
        key=args.key,
    )

if __name__ == "__main__":
    main()