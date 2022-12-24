import urllib.request

import requests
from bs4 import BeautifulSoup
import json
def genRPKM(name, count):
    gene_id = getGeneID(name)
    url = "https://www.ncbi.nlm.nih.gov/gene/" + str(gene_id) + "/?report=expression"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    scripts = soup.find_all('script')
    originData = scripts[6].text
    # print(originData)
    tag = 0
    flag = True
    content = ''
    for i in range(len(originData)):
        if flag:
            if tag > 0:
                content += originData[i]
                if originData[i] == '{':
                    tag += 1
                elif originData[i] == '}':
                    tag -= 1
                    if tag == 0:
                        flag = False
            elif originData[i] == '{':
                tag += 1
                content += '{'
            else:
                continue
        else:
            break

    content = content.replace("'", '"')
    origin_data = json.loads(content)
    result = name + ', ' + str(origin_data.get('testis').get("exp_rpkm")) + ", " + str(count)
    print(result)
    # print(origin_data.get('appendix'))

def getGeneID(name):
    url = "https://www.ncbi.nlm.nih.gov/gene/?term=" + name
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    originData = soup.text
    begin = originData.find("Gene ID: ")
    count = 9
    gene_id = ""
    for i in range(100):
        if originData[begin + count + i] >= "0" and originData[begin + count + i] <= "9":
            gene_id += originData[begin + count + i]
        else:
            break
    return gene_id


# genRPKM(getGeneID('ZIC5'))
# genRPKM(85416)
name_list = []
with open("16samples_filter.anno.txt", 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        name_list.append(line)
for i in range(len(name_list)):
    try:
        genRPKM(name_list.__getitem__(i), i)
    except Exception:
        i -= 1
# for name in name_list:
#     genRPKM(getGeneID(name))