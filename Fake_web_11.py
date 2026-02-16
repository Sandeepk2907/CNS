import hashlib
trusted_dns_record={
    "google.com":hashlib.sha256("google.com".encode()).hexdigest(),
    "amazon.com":hashlib.sha256("amazon.com".encode()).hexdigest(),
    "facebook.com":hashlib.sha256("facebook.com".encode()).hexdigest()
}
user_domain=input("Enter Website Name:")
if user_domain in trusted_dns_record:
    user_hash=hashlib.sha256(user_domain.encode()).hexdigest()
    if user_hash==trusted_dns_record[user_domain]:
        print("\n Website is Authentic(Not fake).")
        print("DNSSEC Verification Successful")
    else:
        print("\n Warning! Website Data Modified.")
        print("DNSSEC Verification Failed")
else:
    print("Fake Website Detected")
    print("Domain Name Not Found in trusted DNS records.")