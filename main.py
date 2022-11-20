import requests
import os
from fpdf import FPDF

def download():
    chapture = [1,2,3,4,5,6]
    page = 2
    count=0
    for i in chapture:
        status=0
        count=0
        while(status!=1):
            url = f'https://www.daanbest.com/addons/junsion_exercises/books/jizhi3/{i}/{str(page).zfill(3)}.jpg'
            page+=1
            headers = {
                'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'
            }

            resp = requests.get(url=url,headers=headers)

            if resp.status_code == 200:
                print(url)
                with open(rf'E:\Desktop\Python\AnswerStar\img\{i}-{page}.jpg','wb') as f:
                    f.write(resp.content)
            elif count==3:
                print('failed')
                status = 1
                page=page-count-1
                continue
            else:
                count+=1

def image2pdf():
    pdf = FPDF()
    pdf.set_auto_page_break(0)         # 自动分页设为False

    path = r"E:\Desktop\Python\AnswerStar\img"
    imagelist = [i for i in os.listdir(path)]


    for image in sorted(imagelist):
        pdf.add_page()
        pdf.image(os.path.join(path, image), w=190, h=270)      # 指定宽高

    pdf.output(os.path.join(path, "数值计算方法-习题答案.pdf"), "F")

if __name__=='__main__':
    download()
    image2pdf()