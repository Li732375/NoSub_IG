import instaloader

cre = input("[帳 密]:").split()

L = instaloader.Instaloader()

L.login(cre[0], cre[1])

# 載入 Session 使用
#L.load_session_from_file('')
    

selfname = instaloader.Profile.own_profile(L.context).username
profile = instaloader.Profile.from_username(L.context, selfname)
print(f"追蹤數： {profile.followees}")
print(f"粉絲數： {profile.followers}")
print(f"合計差異數為 {profile.followees - profile.followers}")

# followings > followers
followings = []
followers = []

for i in profile.get_followees():
    followings.append(i.username)

for i in profile.get_followers(): # 這裡直接空撈，還不報錯
    followers.append(i.username)

# 儲存 Session 供下次使用
L.save_session_to_file()

followings_set = set(followings)
followers_set = set(followers)
print(f"取得的追蹤清單數量： {len(followings_set)}")
print(f"取得的追蹤者清單數量： {len(followers_set)}")

# 求出兩名單之間的差異帳號
delta_set = followings_set - followers_set

# 讀取例外帳號名單
otherFile = open("IGOtherList.txt", 'r')
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

file = open("IGNoSubList.txt", 'w')

for i in delta_sortList:
    file.write(f"{i}\n")

file.close()

print(f"登陸檔案完成，排除 {len(other)} 個例外，合計帳號 {len(delta_set)} 個未回追")
