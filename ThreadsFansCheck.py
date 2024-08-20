from threadspy import ThreadsAPI

cre = input("[帳 密]:").split()

api = ThreadsAPI(
      username = cre[0],
      password = cre[1]
      )

# api.user_id


# followings > followers
followings = []
followers = []

#print(api.get_user_id_from_username(api.username))
#print(api.user_id)
print(api.get_followings(api.user_id))
#print('=' * 20)
#print(api.get_followers(api.user_id))

followings.append(i['full_name'] for i in api.get_followings(
    api.user_id)['users'])
followers.append(i['full_name'] for i in api.get_followings(
    api.user_id)['users'])


followings_set = set(followings)
followers_set = set(followers)
print(f"追蹤數： {len(followings_set)}")
print(f"粉絲數： {len(followers_set)}")

# 求出兩名單之間的差異帳號
delta_set = followings_set - followers_set

# 讀取例外帳號名單
otherFile = open("ThreadOtherList.txt", 'r')
other = otherFile.readlines()

for i in range(len(other)):
    other[i] = other[i].replace('\n', '')
    
otherFile.close()

other = set(other)

# 排除例外名單
delta_set = delta_set - other

delta_sortList = []
# 排序後寫入檔案
for i in delta_set:
    delta_sortList.append(i)
    
delta_sortList.sort()

file = open("ThreadNoSubList.txt", 'w', encoding = 'utf-8')
# =============================================================================
# 錯誤 UnicodeEncodeError: 'cp950' codec can't encode character '\U0001f36d' 
# 表示程式在嘗試寫入包含 Unicode 字符（例如 \U0001f36d，這是巧克力餅乾的表情符號
#  🍭）的文本時遇到問題。這是因為預設編碼 'cp950'（主要用於繁體中文 Windows 系
#  統）無法處理這些字符。
# =============================================================================

for i in delta_sortList:
    file.write(f"{i}\n")

file.close()

print(f"登陸檔案完成，排除 {len(other)} 個例外，合計帳號 {len(delta_set)} 個未回追")
