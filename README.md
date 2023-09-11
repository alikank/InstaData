# InstaData

Bu proje herhangi bir api kullanmadan instagram hesabınızdaki takipçi listesi, takip ettiğiniz kullanıcıların listesi ve sizi takip etmeyenlerin listesini selenium yardımıyla gösterir.


## Gereksinimler

- Python
- selenium==4.0.0b3
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
| `login()` |  | giriş işlemini gerçekleştirir. |
| `getFollowers()` |  | takipçi listesini elde eder. |
| `getFollowing()` |  | takip edilen listesini elde eder. |
| `getUnfollowers(data,data2)` | `data : followers, data2 : following` | sizi takip etmeyenleri elde eder. |



  
## 

```bash
  alikan.com.tr
```

  
