from Bio import Entrez

class SearchPubMed():
    def __init__(self):
        self.email = "test@example.com"
    
    def search(self, SpeciesList, BacterialOrVirusList):       
        searchList = []
        idList = self.getIdList(SpeciesList, BacterialOrVirusList)
        if(len(idList) != 0):
            summaryList = self.getSummaryList(idList)
            for summary in summaryList:
                searchList.append(self.getTitleAndUrl(summary))
        return searchList
    
    def getSummaryList(self, idList):
        idString = ""
        for id in idList:
            if not idString:
                idString = id
            idString = idString + "," + id
        Entrez.email = self.email
        handle = Entrez.esummary(db="pubmed", id=idString)
        record = Entrez.read(handle)
        return record

    def getTitleAndUrl(self, summary):
        dictionary = {}
        dictionary["title"] = summary["Title"]
        dictionary["url"] = "https://pubmed.ncbi.nlm.nih.gov/" + summary["Id"]
        return dictionary

    def getKeyword(self, SpeciesList, BacterialOrVirusList):
        species = ""
        bacterialOrVirus = ""

        for element in SpeciesList:
            if not species:
                species = element
            else:
                species = "{} OR {}".format(species, element)
        print(species)
        for element in BacterialOrVirusList:
            if not bacterialOrVirus:
                bacterialOrVirus = element
            else:
                bacterialOrVirus = "{} OR {}".format(bacterialOrVirus, element)
        # print(bacterialOrVirus)
        return "(({}) AND ({}))".format(species, bacterialOrVirus)
    
    def getIdList(self, SpeciesList, BacterialOrVirusList):
        keyword = self.getKeyword(SpeciesList, BacterialOrVirusList)
        Entrez.email = self.email
        handle = Entrez.esearch(db="pubmed", term=keyword, sort="relevance")
        record = Entrez.read(handle)
        return record["IdList"]

    def SetEmail(self, email):          
        self.email = email