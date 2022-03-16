import time
from SearchTaxonomy import SearchTaxonomy
from SearchPubMed import SearchPubMed
from SearchCommonName import SearchCommonName
from SearchAccession import SearchAccession

import ssl

class MainSearch():
    def __init__(self):
        ssl._create_default_https_context = ssl._create_unverified_context
        self.search = SearchPubMed()
        self.searchTaxon = SearchTaxonomy()
        self.searchName = SearchCommonName()
        self.searchAccession = SearchAccession()
    def GetAncestor(self, targetID):
        genusDictionary = {}
        # targetID = 99486
        family = self.searchTaxon.GetFamily(targetID)
        genus = self.searchTaxon.GetChild(self.searchTaxon.GetTaxID(family), "genus")
        start = time.time()
        data = []
        for child in genus:
            genusDictionary[child] = {}
            result = self.searchTaxon.GetChild(self.searchTaxon.GetTaxID(child), "species")
            for specie in result:
                genusDictionary[child][specie] = {}
            data.append(result)
        end = time.time()
        print(end - start)
        return genusDictionary

    def isMatchHost(self, keywordsA, keywordsB):
        searchRelation = self.search.search(keywordsA, keywordsB)
        print("number of related paper: %d" %len(searchRelation))
        if(len(searchRelation) > 0):
            return True
        else:
            return False

    def GetAccessionDictionary(self, targetID, hostID):
        # data = [['Black beetle virus', 'Boolarra virus', 'Flock House virus', 'Nodamura virus', 'Pariacoto virus'], ['Striped jack nervous necrosis virus', 'Barfin flounder nervous necrosis virus', 'Redspotted grouper nervous necrosis virus', 'Tiger puffer nervous necrosis virus']]
        # genusDictionary = {'Betanodavirus': {'Striped jack nervous necrosis virus': {}, 'Barfin flounder nervous necrosis virus': {}, 'Redspotted grouper nervous necrosis virus': {}, 'Tiger puffer nervous necrosis virus': {}}, 'Alphanodavirus': {'Black beetle virus': {}, 'Boolarra virus': {}, 'Flock House virus': {}, 'Nodamura virus': {}, 'Pariacoto virus': {}}}
        # hostID = 323802
        genusDictionary = self.GetAncestor(targetID)
        hostGenus = self.searchTaxon.GetGenus(hostID)
        commonName = self.searchName.getCommonName(hostGenus)
        for genusKey in genusDictionary:
            for speciesKey in genusDictionary[genusKey]:
                if(commonName != None and self.isMatchHost([speciesKey], [hostGenus, commonName]) or self.isMatchHost([speciesKey], [hostGenus])):
                    speciesChild = self.searchTaxon.GetChild(self.searchTaxon.GetTaxID(speciesKey), "")
                    if(len(speciesChild) == 0):
                        result = [speciesKey]
                    else:
                        result = speciesChild

                    for organism in result:
                        if(len(organism) >= 50):
                            continue
                        if self.searchAccession.Run(organism, True) == 0:
                            self.searchAccession.Run(organism, False)
                        organismKey = str(self.searchTaxon.GetTaxID(organism)) + "_" + organism
                        accession = self.searchAccession.GetAccession()
                        if(accession != None):
                            genusDictionary[genusKey][speciesKey][organismKey] = accession
        return genusDictionary
