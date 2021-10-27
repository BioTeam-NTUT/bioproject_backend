import pytaxonkit

class SearchTaxonomy():
    def __init__(self):
        pass
    def GetFamily(self, taxID):
        result = pytaxonkit.lineage([str(taxID)], formatstr = '{f}')
        result.columns
        family = result['Lineage'][0]
        print(family)
        return family
    def GetGenus(self, taxID):
        result = pytaxonkit.lineage([str(taxID)], formatstr = '{g}')
        result.columns
        genus = result['Lineage'][0]
        print(genus)
        return genus
    def GetChild(self, taxID, rank):
        # rank = genus, species, no rank
        result = pytaxonkit.list([taxID])
        for taxon, tree in result:
            if len(tree) != 0:
                subtaxa = [t for t in tree.traverse]
            else:
                subtaxa = []
            print(f'Top level result: {taxon.name} ({taxon.taxid}); {len(subtaxa)} related taxa')
        child = []
        for i, taxon in enumerate(subtaxa):
            # print(i)
            if(rank == ""):
                child.append(str(taxon.name))
            if(taxon.rank == rank and not self.isUnclassified(taxon.taxid)):
                child.append(str(taxon.name))
        return child
    def GetTaxID(self, name):
        answer = pytaxonkit.name2taxid([name])
        return int(answer["TaxID"][0])
    def isUnclassified(self, taxID):
        taxa = pytaxonkit.lineage([str(taxID)])
        data = taxa['FullLineage'][0]
        if("unclassified" in data):
            return True
        else:
            return False