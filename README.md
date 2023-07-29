# InstaData

Bu proje herhangi bir api kullanmadan instagram hesabınızdaki takipçi listesi, takip ettiğiniz kullanıcıların listesi ve sizi takip etmeyenlerin listesini selenium yardımıyla gösterir.


## Gereksinimler

- Python
- Selenium
- Chrome Web Driver

  
## Projeyi Çalıştırmak

Bu projeyi çalıştırmak için account.py dosyasındaki aşağıdaki değişkenleri düzenlemeniz gerek.

`username="your_instagram_username"`

`password="your_instagram_password"`

`chromeDriverPath = "C:/Users/chromedriver-win32/chromedriver.exe"`

Daha sonrasında komut satırına :

```bash
  python app.py
```

  
## Method Kullanımı



| Yöntem | Argüman     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `insta.login()` |  | giriş işlemini gerçekleştirir. |
| `insta.getFollowers()` |  | takipçi listesini elde eder. |
| `insta.getFollowing()` |  | takip edilen listesini elde eder. |
| `InstaData.getUnfollowers(data,data2)` | `data : followers, data2 : following` | sizi takip etmeyenleri elde eder. |



  
## 

```bash
  alikan.com.tr
```

  
