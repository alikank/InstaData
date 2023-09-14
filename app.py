from account import username,password,chromeDriverPath
from selenium import webdriver
import time

class InstaData:
    def __init__(self,username,password,path):
        self.driver = webdriver.Chrome(path)
        self.username = username
        self.password = password

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)
        self.driver.find_element_by_css_selector("input[type='text']").send_keys(self.username)
        self.driver.find_element_by_css_selector("input[type='password']").send_keys(self.password)
        self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button").click()
        time.sleep(3)

    def getFollowers(self):
        time.sleep(3)
        self.followers = []
        self.driver.get("https://www.instagram.com/"+self.username)
        time.sleep(3)
        self.driver.find_element_by_css_selector("a.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz._alvs._a6hd").click()
        time.sleep(2)
        users = self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")       
        followerCount = len(users)
        
        while True:
            self.driver.execute_script("document.querySelector('div._aano').scrollTo(0, document.querySelector('div._aano').scrollHeight);")
            time.sleep(2)
            newCount = len(self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if(newCount==followerCount):
                break
            else:
                followerCount = newCount
                time.sleep(2)

        users = self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in users:
            nickname = user.find_element_by_css_selector("span._aacl._aaco._aacw._aacx._aad7._aade").text
            self.followers.append(nickname)
        return self.followers
    
    def getFollowing(self):
        time.sleep(3)
        self.following = []
        self.driver.get("https://www.instagram.com/"+self.username+"/following")       
        time.sleep(5)
        users = self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")        
        followingCount = len(users)
        
        while True:
            self.driver.execute_script("document.querySelector('div._aano').scrollTo(0, document.querySelector('div._aano').scrollHeight);")
            time.sleep(2)
            newCount = len(self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3"))
            if(newCount==followingCount):
                break
            else:
                followingCount = newCount
                time.sleep(2)

        users = self.driver.find_elements_by_css_selector("div.x1dm5mii.x16mil14.xiojian.x1yutycm.x1lliihq.x193iq5w.xh8yej3")
        for user in users:
            nickname = user.find_element_by_css_selector("span._aacl._aaco._aacw._aacx._aad7._aade").text
            self.following.append(nickname)
        return self.following
    
    @staticmethod
    def getUnfollowers(followers,following):
        return set(following)-set(followers)


insta = InstaData(username,password,chromeDriverPath)
insta.login()
data = insta.getFollowers() # takipçi listesi
data2 = insta.getFollowing() # takip edilen listesi

print(len(data),len(data2)) # takipçi sayısı, takip edilen sayısı
print(InstaData.getUnfollowers(data,data2)) # sizi takip etmeyenler listesi
