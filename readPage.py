from webClawler import WebClawler
from dictionary import Dictionary

if __name__ == "__main__":
    claw = WebClawler()
    dic = Dictionary()
    urls = ['https://www.digitalocean.com/pricing/#droplet', 'https://www.vultr.com/products/cloud-compute/']
    whatUrl = int(input("Digite 1 para acessar a URL 'https://www.digitalocean.com/pricing/#droplet'\nou 2 para acessar a URL 'https://www.vultr.com/products/cloud-compute/'\n\n:"))
    if whatUrl == 1:
        headers = ['Memory', 'vCPUs', 'Transfer', 'SSD Disk', '$/HR', '$/MO']
        find = claw.readPage('https://www.digitalocean.com/pricing/#droplet', r'<td>(\w*?GB|\w*?vCPU|\w*?TB|\$\w.*?)</td>')
        findFormated = dic.format_dict(find, headers)              
        print (findFormated)
    elif whatUrl == 2:
        pass