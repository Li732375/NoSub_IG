import instaloader

cre = input("[帳 密]:").split()

L = instaloader.Instaloader()

L.login(cre[0], cre[1])

selfname = instaloader.Profile.own_profile(L.context).username
profile = instaloader.Profile.from_username(L.context, selfname)

# followings > followers
followings = []
followers = []

for i in profile.get_followees():
    followings.append(i.username)
    
for i in profile.get_followers():
    followers.append(i.username)

followings_set = set(followings)
followers_set = set(followers)

print(f"current followings: {profile.followees}")
print(f"current followers: {profile.followers}")

# 求出兩名單之間的差異帳號
delta_set = followings_set - followers_set

# 讀取例外帳號名單
otherFile = open("OtherList.txt", 'r')
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

file = open("NoSubList.txt", 'w')

for i in delta_sortList:
    file.write(f"{i}\n")

file.close()

print(f"登陸檔案完成，排除 {len(other)} 個例外，合計帳號 {len(delta_set)} 個未回追")
