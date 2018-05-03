# Responderpot

A simple honeypot that will make SMB connections to non-existent machines and alert if anything responds.

## Usage

```
python3 -m pip install -r requirements.txt
python3 responderpot.py --domain TARGET-DOMAIN --throttle SECONDS-BETWEEN-REQUESTS
```

## Example

```
HOST:Responder bkoffel$ sudo ./Responder.py -I en0 -i 127.0.0.1
[+] Listening for events...
[SMB] NTLMv2-SSP Client   : 127.0.0.1
[SMB] NTLMv2-SSP Username : WORKGROUP\8gN35y
[SMB] NTLMv2-SSP Hash     : 8gN35y::WORKGROUP:a8ffc71d20bb98df:8AEF23C87C7CCA49CF4C...
[+] Exiting...

HOST:responderpot bkoffel$ python3 responderpot.py 
2018-05-03 23:28:42.839680 INFO SUSPICIOUS_SMB_RESPONSE 127.0.0.1 445
2018-05-03 23:28:52.853893 INFO SUSPICIOUS_SMB_RESPONSE 127.0.0.1 445
2018-05-03 23:29:02.864046 INFO SUSPICIOUS_SMB_RESPONSE 127.0.0.1 445
```

## References

- https://github.com/lgandx/Responder
