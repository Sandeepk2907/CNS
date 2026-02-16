import hashlib
def  sign_data(data):
    return hashlib.sha256(data.encode()).hexdigest()
OG=input("Enter Original Domain Name:")
sign=sign_data(OG)
print("\n Generated DNS Signature:",sign)
received=input("\n Enter Received Domain Name:")
verify=sign_data(received)
if verify==sign:
    print("\n DNSSEC Verification Successful:Data is Authentic.")
else:
    print("\n DNSSEC Verification Failed:Data has been Modified.")
