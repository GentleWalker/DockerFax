import http.client
import json

conn = http.client.HTTPSConnection("127.0.0.1", 8088)
payload = json.dumps({
  "ime": "Luka",
  "prezime": "Stankovic",
  "username": "lstankovic16",
  "smer": "RM",
  "predmeti": [
    {
      "ime": "OperativniSistemi",
      "espb": "8"
    },
    {
      "ime": "DigitalneKomunikacije",
      "espb": "8"
    },
    {
      "ime": "PrimenjeniDistribuiraniSistemi",
      "espb": "6"
    },
    {
      "ime": "DigitalnaObradaSignala",
      "espb": "6"
    }
  ]
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/users", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))