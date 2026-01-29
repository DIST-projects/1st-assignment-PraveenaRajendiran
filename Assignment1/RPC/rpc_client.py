import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://54.252.136.93:8000/")

print("Addition:", proxy.add(5, 3))
print("Multiplication:", proxy.multiply(4, 6))