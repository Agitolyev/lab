from datetime import datetime
import urllib2
bla = {1:'24', 2:'25', 3:'05', 4:'06', 5:'27', 6:'23', 7:'26', 8:'07', \
       9:'11', 10:'13', 11:'14', 12:'15', 13:'16', 14:'17', 15:'18', 16:'19', \
       17:'21', 18:'22', 19:'08', 20:'09', 21:'10', 22:'01', 23:'02', 24:'03', 25:'04'}
for i in range(1,3):
    url="http://www.star.nesdis.noaa.gov/smcd/emb/vci/gvix/G04/ts_L1/ByProvince/Mean/L1_Mean_UKR.R" + bla[i] + ".txt"
    vhi_url = urllib2.urlopen(url)
    a = datetime.strftime(datetime.now(), "%Y.%m.%d.%H:%M:%S")
    out = open('vhi_id_'+str(i)+'_'+ a +'.csv','wb')
    out.write(vhi_url.read())
    out.close()
    print "VHI is downloaded..."

import pandas as pd
df = pd.read_csv('vhiThu Mar 24 22:36:19 2016.csv',index_col=False, header=1)
print list(df.columns.values)
print df[:1]
print df.VHI[df['year']==1981]
print df.VHI[:]

print df.VHI[df['week']>51]

print min(df.VHI[df['year'] == 1981])
print df.shape
df = df[df.VHI>0]
print df.shape


print df.year[df['VHI'] == min(df.VHI)]
