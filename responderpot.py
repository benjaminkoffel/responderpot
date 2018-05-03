import argparse
import random
import string
import time
import traceback
import smb
from smb.SMBConnection import SMBConnection

def randchars(mn, mx):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(random.randint(mn, mx)))

def connect(domain, username, password, client, server):
    conn = SMBConnection(username, password, client, server, domain=domain, use_ntlm_v2=True, is_direct_tcp=True)
    conn.connect('0.0.0.0', 445)
    shares = conn.listShares()
    for share in shares:
        if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
            sharedfiles = conn.listPath(share.name, '/')
            for sharedfile in sharedfiles:
                print(sharedfile.filename)
    conn.close()

def main(domain, throttle):
    while True:
        try:
            connect(domain, randchars(6, 12), randchars(6, 12), randchars(6, 12), randchars(6, 12))
        except smb.smb_structs.ProtocolError as e:
            print("ALERT: UNEXPECTED RESPONSE DETECTED")
        except ConnectionRefusedError as e:
            pass
        except Exception as e:
            print(traceback.format_exc())
        time.sleep(throttle)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', '-d', help='target domain for monitoring')
    parser.add_argument('--throttle', '-t', type=int, default=10, help='throttle requests in seconds')
    args = parser.parse_args()
    main(args.domain, args.throttle)
