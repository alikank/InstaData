
![Logo](https://camo.githubusercontent.com/7418028f345a3f3893a97912b5596c6aabcc716618ba17df0d76a78a562a64d1/68747470733a2f2f692e6962622e636f2f323768633843522f426c61636b2d436c65616e2d616e642d4d696e696d616c6973742d50726f6a6563742d4f766572766965772d446f63732d42616e6e65722e706e67)

    

    
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



| Yöntem | Durum     | Açıklama                |
| :-------- | :------- | :------------------------- |
| `insta.login()` | `zorunlu` | giriş işlemini gerçekleştirir. |
| `insta.getFollowers()` |  | takipçi listesini elde eder. |
| `insta.getFollowing()` |  | takip edilen listesini elde eder. |
| `InstaData.getUnfollowers(data,data2)` | `data : followers, data2 : following` | sizi takip etmeyenleri elde eder. |



  
## 

```bash
  alikan.com.tr
```

  
