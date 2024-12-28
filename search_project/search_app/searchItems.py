import requests

class SearchItems():
    def __init__(self):
        self.rakuten = Rakuten()
        self.yahoo = Yahoo()
    
    def search(self, keyword, genreId):
        rakuten_result = self.rakuten.items_search(keyword, genreId)
        yahoo_result = self.yahoo.items_search(keyword, genreId)
        return rakuten_result, yahoo_result

class Rakuten():
    def __init__(self):
        self.url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20220601?"
        self.appricationId = "1080638618593042114"
        self.affiliateId = "432a33ac.e1f30558.432a33ad.de61e252"
    
    def items_search(self, keyword, genreId):
        params = {
            "applicationId": self.appricationId,
            "keyword": keyword,
            "genreId": genreId,
            "format": "json",
            "formatVersion": 1,
            "affiliateId": self.affiliateId
        }
        res = requests.get(self.url, params=params)
        result = res.json()
        return result
    
class Yahoo():
    def __init__(self):
        self.url = "https://shopping.yahooapis.jp/ShoppingWebService/V3/itemSearch"
        self.appricationId = "dj00aiZpPU9hRTdUS0p3TGNDNCZzPWNvbnN1bWVyc2VjcmV0Jng9NTQ-"
        self.affiliateId = "432a33ac.e1f30558.432a33ad.de61e252"
    
    def items_search(self, keyword, genreId):
        params = {
            "appid": self.appricationId,
            "query": keyword,
            "genre_category_id": genreId,
        }
        res = requests.get(self.url, params=params)
        result = res.json()
        return result
    
class Amazon():
    def __init__(self):
        self.url = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.appricationId = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        self.affiliateId = "XXXXXXXX.e1f30558.432a33ad.de61e252"

    def items_search(self, keyword, genreId):
        params = {
            "appid": self.appricationId,
            "query": keyword,
            "genre_category_id": genreId,
        }
        res = requests.get(self.url, params=params)
        result = res.json()
        return result