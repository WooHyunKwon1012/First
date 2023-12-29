import csv
f=open("202311_202311_연령별인구현황_월간.csv")
data=csv.reader(f)
data_seoul=[]
data_busan=[]
data_daegu=[]
data_inch=[]
data_gang=[]
data_ulsan=[]
data_daegn=[]
data_sae=[]
data_ggi=[]
data_gangwn=[]
data_chbook=[]
data_chnam=[]
data_gksang=[]
data_zunbk=[]
data_zunnam=[]


for view in data:
    if '서울특별시  (1100000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_seoul.append(int(i))
    if '부산광역시  (2600000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_busan.append(int(i))
    if '대구광역시  (2700000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_daegu.append(int(i))
    if '인천광역시  (2800000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_inch.append(int(i))
    if '광주광역시  (2900000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_gang.append(int(i))
    if '대전광역시  (3000000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_daegn.append(int(i))
    if '울산광역시  (3100000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_ulsan.append(int(i))
    if '세종특별자치시  (3600000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_sae.append(int(i))
    if '경기도  (4100000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_ggi.append(int(i))
    if '강원특별자치도  (5100000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_gangwn.append(int(i))
    if '충청북도  (4300000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_chbook.append(int(i))
    if '충청남도  (4400000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_chnam.append(int(i))
    if '전라북도  (4500000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_zunbk.append(int(i))
    if '전라남도  (4600000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_zunnam.append(int(i))
    if '경상북도  (4700000000)' in view[0]:
        for i in view[3:]:
            i=i.replace(',','')
            data_gksang.append(int(i))
print('서울특별시',data_seoul)
print('부산광역시',data_busan) 
print('대구광역시',data_daegu)
print('인천광역시',data_inch)
print('광주광역시',data_gang)
print('대전광역시',data_daegn)
print('울산광역시',data_ulsan)
print('세종특별자치시',data_sae)
print('경기도',data_ggi)
print('강원특별자치도',data_gangwn)
print('충청북도',data_chbook)
print('전라북도',data_zunbk)   
print('전라남도',data_zunnam)
print('경상북도',data_gksang)                                        
f.close()


import numpy as np
import matplotlib.pyplot as plt
x=np.arange(11)

ages1=list(range(0,110,10))

ages2=["0대","10대","20대","30대","40대","50대","60대","70대","80대","90대","100대"]
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('인구 구조 비교')
plt.plot(data_seoul,'r',label='서울광역시')
plt.plot(data_busan,'g',label='부산광역시')
plt.plot(data_daegu,'b',label='대구광역시')
plt.plot(data_inch,'lightcoral',label='인천광역시')
plt.plot(data_gang,'c',label='광주광역시')

plt.xticks(x,ages2)
plt.legend()

plt.show()
