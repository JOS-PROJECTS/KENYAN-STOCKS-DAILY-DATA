import json
import requests
from bs4 import BeautifulSoup

r = requests.get('https://live.mystocks.co.ke/m/pricelist', stream=True)
page_lines=[]
for line in r.iter_lines():

    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode('utf-8')
        page_lines.append(json.dumps(decoded_line))

raw_data=page_lines[45:201]
#print(raw_data)

stocks=[]
stock_name=[]
stock_price=[]
entry=[]
stocks_all={}
for i in raw_data:
    html_doc=i
    soup = BeautifulSoup(html_doc, 'html.parser')
    val=soup.get_text()
    if "head" in i:
        title=val
        entry=[]
        continue
    elif val:
        entry.append(val)
        stocks_all[title]=entry
        continue
print(stocks_all)


#CODE TO CHECK LINE NUMBERS FOR DATA
"""c=0
toppers_table=[]
titles=["class=head", "row r0", "row r1", "class=nm"]
for i in page_lines:
    if any(x in i for x in titles):
        s=(i, "line no.", c)
        toppers_table.append(s)
    c=c+1
print(page_lines[41:201])
#print(toppers_table)
"""

#CODE TO CHECK FOR MATCHES IN PAGE LINES LIST
"""matches = ["BAMB","EABL","SASINI LTD"]
l=["SASN","NCBA","SCOM","WTK","EVRD","KCB","ABSA","CTUM","UMME","SLAM","SGL","SCBK","LKL","LBTY","ABSA","KCB","Military Expenditure","Inflation Rate MoM","Inflation Rate","Producer Prices Index YoY","Food Inflation YoY","Consumer Price Index"]

for i in page_lines:
    if any(x in i for x in matches):
        print(i)
    else:
        continue
"""

    
