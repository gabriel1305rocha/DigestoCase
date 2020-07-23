class Dictionary():
    
    def format_dict(self, find, headers):
        headers = ['Memory', 'vCPUs', 'Transfer', 'SSD Disk', '$/HR', '$/MO']
        contHeader = 0
        contDict = 0
        pricingDict = [{}]
        for data in find:
            if contHeader >= 6:
                contHeader = 0
                contDict+=1
                pricingDict.append({})
            pricingDict[contDict].update({headers[contHeader]: data})
            contHeader+=1
        return pricingDict