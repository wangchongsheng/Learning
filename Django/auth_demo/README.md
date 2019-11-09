### Auth模块
1. 创建超级用户  
python manage.py createsuperuser  
from django.contrib import auth  

2. auth.authenticate(username=username,password=password)  
验证用户名密码  
如果验证成功，得到的是一个用户对象  
如果验证失败，得到一个匿名用户  

3. auth.login(request,user)  
将验证过的用户 赋值给request.user属性  
   
4. auth.logout(request)  
request.session.flush()  
将session数据都删除，并且cookie也失效

### 扩展自带的auth_user表
1. 新建一个表，一对一的关联上面的auth_user表
2. 继承的方式
```
from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser):
    phone = models.CharField(max_length=11)
    addr = models.CharField(max_length=255)
    
    相当于对默认的auth_user表做了扩展，并且代替auth_user
    注意：
        在setting.py中一定要加  
            AUTH_USER_MODEL='APP名.类名'
```  