import json, csv
class GenerateFiles():
    
    def generateJson(self, findFormated):
        with open('dados.json', 'w') as json_file:
            json.dump(findFormated, json_file, indent=4)