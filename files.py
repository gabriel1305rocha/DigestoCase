import json, csv
class GenerateFiles():
    
    def generateJson(self, findFormated):
        try:
            with open('dados.json', 'w') as json_file:
                json.dump(findFormated, json_file, indent=4)
            print("JSON gerado com sucesso!")
        except:
            print("Encontramos problemas ao gerar o JSON")
        
    def generateCSV(self , findFormated):
        try:
            with open('dados.csv', 'w') as csv_file:
                columns = list(findFormated[0].keys())
                write = csv.DictWriter(csv_file, fieldnames=columns, delimiter=';', lineterminator='\n')
                write.writeheader()
                for find in findFormated:
                    write.writerow(find)
            print("CSV gerado com sucesso!")
        except:
            print("Encontramos problemas ao gerar o arquivo CSV")
    
    