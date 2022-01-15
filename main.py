import speedtest

test= speedtest.Speedtest()

print("Server Loading...")

test.get_servers()

print("Choosing ideal server...")

ideal= test.get_best_server()

print(f"Ideal Server: {ideal} ")

print("Excuting download server...")

download_outcome = test.download()

upload_outcome = test.upload()
ping_outcome= test.results.ping
print(download_outcome)
print(upload_outcome)
print(ping_outcome)

print(f"Download Speed: {download_outcome/1024/1024: .3f} Mbps")
print(f"Upload Speed: {upload_outcome/1024/1024: .3f} Mbps")
print(f"Ping: {ping_outcome: .3f}ms")