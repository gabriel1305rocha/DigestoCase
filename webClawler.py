import requests as req
import re
class WebClawler():

    def readPage(self, url, regex):
        r = req.get(url)
        find  = re.findall(regex, str(r.content))
        return find
        #r = req.get('https://www.digitalocean.com/pricing/#droplet')
        #find  = re.findall(r'<td>(\w*?GB|\w*?vCPU|\w*?TB|\$\w.*?)</td>', str(r.content))