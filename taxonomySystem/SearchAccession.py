import requests, sys
class SearchAccession():
    def __init__(self):
        self.requestCoatURL = "https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=100&protein=Coat%20protein&organism="
        self.requestCapsidURL = "https://www.ebi.ac.uk/proteins/api/proteins?offset=0&size=100&protein=Capsid%20protein%20alpha&organism="
        self.result = []
    def Run(self, organism, mode):
        data = organism.split(' ')
        requestOrganism = ""
        for i, word in enumerate(data):
            if(i != 0):
                requestOrganism += "%20"
            requestOrganism += word
        if(mode):
            requestURL = self.requestCapsidURL
        else:
            requestURL = self.requestCoatURL
        url = requestURL + requestOrganism
        r = requests.get(url, headers={ "Accept" : "application/json"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        responseBody = r.json()
        self.result = responseBody
        return(len(responseBody))
    def GetAccession(self):
        for temp in self.result:
            if(temp["proteinExistence"] != "Protein uncertain"):
                return temp["accession"]