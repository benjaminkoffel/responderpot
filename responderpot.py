import argparse
import datetime
import random
import string
import sys
import time
import traceback
import smb
from smb.SMBConnection import SMBConnection

def randchars(mn, mx):
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(random.randint(mn, mx)))

def connect(domain, username, password, client, server):
    try:
        conn = SMBConnection(username, password, client, server, domain=domain, use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect('0.0.0.0', 445)
        ip, port = conn.sock.getpeername()
        conn.close()
        print('{} INFO SUSPICIOUS_SMB_RESPONSE {} {}'.format(str(datetime.datetime.now()), ip, port))
    except smb.smb_structs.ProtocolError as e:
        ip, port = conn.sock.getpeername()
        conn.close()
        print('{} INFO SUSPICIOUS_SMB_RESPONSE {} {}'.format(str(datetime.datetime.now()), ip, port))
    except ConnectionRefusedError as e:
        pass
    except Exception as e:
        sys.stderr.write('{} ERROR {}'.format(str(datetime.datetime.now()), traceback.format_exc()))

def monitor(domain, throttle):
    while True:
        connect(domain, randchars(6, 12), randchars(6, 12), randchars(6, 12), randchars(6, 12))
        time.sleep(throttle)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--domain', '-d', default='WORKGROUP', help='target domain for monitoring')
    parser.add_argument('--throttle', '-t', type=int, default=10, help='throttle requests in seconds')
    args = parser.parse_args()
    monitor(args.domain, args.throttle)
