import requests
# url="http://v1-tt.ixigua.com/0b57557ba010dc3b3f2e8891c2b80ba1/5a211f82/video/m/2209f50d550c3fa425dbbedcee7e33a953811529e910000e0831f910633/"
# word="welcome"
# data={
# 'from': 'en',
# 'to': 'zh',
# 'query': word,
# 'transtype': 'translang',
# 'simple_means_flag': '3'
# }
# response=requests.post(url)
# data=response.json()
# means=data['dict_result']['simple_means']['symbols'][0]['parts']
# with open('mv.mp4','wb') as f:
#     for item in means:
#         f.write(item['part']+' '.join(item['means'])+'\n')
url="http://v3-tt.ixigua.com/652ff73b6e6cac842dd955bdc92e3d7e/5a73e423/video/m/220851bd08d74a64969886ccfdd36e758c61154010a000020a685d01c9f/"
# url="http://v1-tt.ixigua.com/0b57557ba010dc3b3f2e8891c2b80ba1/5a211f82/video/m/2209f50d550c3fa425dbbedcee7e33a953811529e910000e0831f910633/"
response=requests.get(url)
data=response.content
with open('mv.mp4','wb') as f:
    f.write(data)
