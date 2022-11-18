import ibm_db

try:
    conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=824dfd4d-99de-440d-9991-629c01b3832d.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30119;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=pkz96094;PWD=LhSkZlezmEjCYhw2;", "", "")
    print("connection succesfull...")

except:
    print("Error connecting to database")