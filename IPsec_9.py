import hashlib
def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()
data=input("Enter Data To Send:")
hash_value=generate_hash(data)
print("Generated Hash:",hash_value)
received_data=input("Enter Received data:")
received_hash=generate_hash(received_data)
if received_hash==hash_value:
    print("Integrity Verified:Data not modified")
else:
     print("Integrity Failed:Data modified")