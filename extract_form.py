import urllib.request
import re

url = "https://docs.google.com/forms/d/e/1FAIpQLSeaYL4eieWfLOFLeyHZuV2Ii2nt2_qcrjyueltKfutczfDMXA/viewform?usp=header"
html = urllib.request.urlopen(url).read().decode("utf-8")

# Extract the questions and their entry IDs
# Look for structures like: [136531317,"Nama Lengkap",null,0,[[575191060,null,1]
import json
matches = re.findall(r'(\d+),"([^"]+)",null,\d+,\[\[(\d+)', html)

print("FOUND FIELDS:")
for m in matches:
    print(f"Title: {m[1]} -> entry.{m[2]}")
