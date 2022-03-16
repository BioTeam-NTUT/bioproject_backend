import requests


class SearchCommonName:
    def __init__(self):
        self.searchUrl = "https://www.itis.gov/ITISWebService/jsonservice/searchForAnyMatchPaged?"

    def getCommonName(self, species):
        postUrl = "&pageSize=1&pageNum=1&ascend=true"
        preUrl = "srchKey=" + species
        url = self.searchUrl + preUrl + postUrl
        data = requests.get(url).json()
        if len(data["anyMatchList"][0]["commonNameList"]["commonNames"]) == 0:
            print("Common name not Found")
        else:
            return data["anyMatchList"][0]["commonNameList"]["commonNames"][0][
                "commonName"
            ]
