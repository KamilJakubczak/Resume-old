def returnPass(){

    passData =  {                                                                   
    'default': {                                                                
        'ENGINE': 'django.db.backends.postgresql',                              
        'NAME': 'my_web',
        'USER': 'noxiss',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '5432'
        }
    }
    return passData
    }
