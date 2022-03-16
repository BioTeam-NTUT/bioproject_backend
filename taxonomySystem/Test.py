import requests
from SearchCommonName import SearchCommonName
from SearchAccession import SearchAccession
# url = "https://www.itis.gov/ITISWebService/jsonservice/searchForAnyMatchPaged?srchKey=Epinephelus&pageSize=1&pageNum=1&ascend=true"
# data = requests.get(url).json()
# print(data["anyMatchList"][0]["commonNameList"]["commonNames"][0]["commonName"])
# Epinephelus


# tool = SearchCommonName()
# answer = tool.getCommonName("Tardigrades")
# print(answer)

tool = SearchAccession()

if (tool.Run("Japanese flounder nervous necrosis virus", True) == 0):
    tool.Run("Japanese flounder nervous necrosis virus", False)

tool.GetAccession()