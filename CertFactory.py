def getPrivateKeyForAddr(addr):
    with open(addr) as f:
        Private_key = f.read()
    return Private_key

def getCertificateForAddr(addr):
    with open(addr) as f:
        Public_key = f.read()
    return Public_key

def getRootCert(addr):
    with open(addr) as f:
        RootCert = f.read()
    return RootCert

if __name__=='__main__':
    private_key = getPrivateKeyForAddr("/Users/runjiezhang/Desktop/public&private_key/Server/key.pem")
    public_key = getCertificateForAddr("/Users/runjiezhang/Desktop/public&private_key/Server/certificate.pem")
    print(public_key)
    