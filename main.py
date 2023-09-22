import subprocess

hostorjoin = input("Host a Server or Connect (H to Host, C to Connect): ")

if hostorjoin == "H":
	subprocess.call(["python", "server.py"])
	hostorjoin = "C"
if hostorjoin == "C":
	subprocess.call(["python", "client.py"])
