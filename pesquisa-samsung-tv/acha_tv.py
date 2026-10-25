import socket, json, ipaddress, urllib.request
from concurrent.futures import ThreadPoolExecutor

# descobre a rede do computador
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80)); meu_ip = s.getsockname()[0]; s.close()
rede = ipaddress.ip_network(meu_ip + "/24", strict=False)
print("Procurando na rede", rede)

def testa(ip):
    ip = str(ip)
    try:
        with socket.create_connection((ip, 8001), timeout=0.5):
            pass
        dados = json.load(urllib.request.urlopen(f"http://{ip}:8001/api/v2/", timeout=3))
        d = dados.get("device", {})
        return ip, d.get("name"), d.get("modelName"), d.get("model"), d.get("developerMode")
    except Exception:
        return None

with ThreadPoolExecutor(64) as ex:
    achou = [r for r in ex.map(testa, rede.hosts()) if r]

for ip, nome, modelo, codigo, dev in achou:
    print(f"TV encontrada: {ip} | nome: {nome} | modelo: {modelo} | codigo: {codigo} | modo desenvolvedor: {dev}")
if not achou:
    print("Nenhuma TV Samsung respondeu. Confira se ela esta ligada e no mesmo Wi-Fi.")
