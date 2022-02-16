import psycopg2



#establishing the connection
conn = psycopg2.connect(
database="postgres", user='postgresadmin', password='admin123', host='192.168.43.18', port= '30193')#Creating a cursor object using the cursor() method
cursor = conn.cursor()
