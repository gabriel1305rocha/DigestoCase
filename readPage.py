import sys
from webClawler import WebClawler
from dictionary import Dictionary
from files import GenerateFiles

if __name__ == "__main__":
    claw = WebClawler()
    dic = Dictionary()
    genFiles = GenerateFiles()
    urls = ['https://www.digitalocean.com/pricing/#droplet', 'https://www.vultr.com/products/cloud-compute/']
    regularExpressions = [r'<td>(\w*?GB|\w*?vCPU|\w*?TB|\$\w.*?)</td>']
    whatUrl = int(input("Digite 1 para acessar a URL 'https://www.digitalocean.com/pricing/#droplet'\nou 2 para acessar a URL 'https://www.vultr.com/products/cloud-compute/'\n\n:"))
    if whatUrl == 1:
        headers = ['Memory', 'vCPUs', 'Transfer', 'SSD Disk', '$/HR', '$/MO']
        find = claw.readPage(urls[0], regularExpressions[0])
        findFormated = dic.format_dict(find, headers)
        decision = int(input("Digite: \n1 para exibir os resultados na tela\n2 para salvar os dados em formato JSON\n3 para salvar os dados no formato CSV\n\n:"))              
        if decision == 1:
            print (findFormated)
        elif decision == 2:
            genFiles.generateJson(findFormated)
        elif decision == 3:
            genFiles.generateCSV(findFormated)
    elif whatUrl == 2:
        try:
            pass
        except:
            print("Dados não encontratos:", sys.exc_info()[0])
    else:
        print("Desculpe opção nao encontrada tente novamente")
        pass