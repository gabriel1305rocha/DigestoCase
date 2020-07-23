import sys
from webCrawler import WebCrawler
from dictionary import Dictionary
from files import GenerateFiles

class ReadPage():
    
    def decisionGenerateFileNode(self, genFiles):
        decision = int(input("Digite: \n1 para exibir os resultados na tela\n2 para salvar os dados em formato JSON\n3 para salvar os dados no formato CSV\n\n:"))              
        if decision == 1:
            print (findFormated)
        elif decision == 2:
            genFiles.generateJson(findFormated)
        elif decision == 3:
            genFiles.generateCSV(findFormated)
            
            
if __name__ == "__main__":
    claw = WebCrawler()
    dic = Dictionary()
    genFiles = GenerateFiles()
    read = ReadPage()
    
    urls = ['https://www.digitalocean.com/pricing/#droplet', 'https://www.vultr.com/products/cloud-compute/']
    regularExpressions = [r'<td>(\w*?GB|\w*?vCPU|\w*?TB|\$\w.*?)</td>', r'<strong>(\w*?.GB|\w*?.CPU|\w*?.MB|..\w*?.TB|\w*?.GB|\$.*?)</strong>']
    headers = [['Memory', 'vCPUs', 'Transfer', 'SSD Disk', '$/HR', '$/MO'],['Storage', 'CPU', 'Memory', 'Bandwidth', 'Price']]
    whatUrl = int(input("Digite 1 para acessar a URL 'https://www.digitalocean.com/pricing/#droplet'\nou 2 para acessar a URL 'https://www.vultr.com/products/cloud-compute/'\n\n:"))
    
    if whatUrl == 1:
        find = claw.readPage(urls[0], regularExpressions[0])
        findFormated = dic.format_dict(find, headers[0])
        read.decisionGenerateFileNode(genFiles)
    elif whatUrl == 2:
        find = claw.readPage(urls[1], regularExpressions[1])
        findFormated = dic.format_dict(find, headers[1])
        read.decisionGenerateFileNode(genFiles)
    else:
        print("Desculpe opção nao encontrada tente novamente")
        pass
    