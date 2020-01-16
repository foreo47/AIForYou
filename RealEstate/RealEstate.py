from urllib.request import urlopen
import pandas as pd
from bs4 import BeautifulSoup
from html_table_parser import parser_functions as parser
 
 
def collect_land_sale(ym,lawd_cd):
 
    API_KEY = "(자신의 API키를 넣는다)"
    url="http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcLandTrade"
 
    url=url+"?LAWD_CD="+lawd_cd+"&DEAL_YMD="+ym+"&serviceKey="+API_KEY
 
    resultXML = urlopen(url)
    result = resultXML.read()
    xmlsoup = BeautifulSoup(result, 'lxml-xml')
 
    te=xmlsoup.findAll("item")
    sil=pd.DataFrame()
 
    for t in te:
        price = t.find("거래금액").text
        size = t.find("거래면적").text
        year=t.find("년").text
        dong=t.find("법정동").text
        gu = t.find("시군구").text
        yd = t.find("용도지역").text
        month=t.find("월").text
        day=t.find("일").text
        jimock=t.find("지목").text
        lawd_cd=t.find("지역코드").text
 
        temp = pd.DataFrame(([[price,size,year,dong,gu,yd,month,day,jimock,lawd_cd]]),
                            columns=["price","size","year","dong","gu","month","day","size","jimock","lawd_cd"])
        sil=pd.concat([sil,temp])
 
    sil=sil.reset_index(drop=True)
 
    return sil
 
if __name__=="__main__":
 
    data=collect_land_sale("201502","11110")
