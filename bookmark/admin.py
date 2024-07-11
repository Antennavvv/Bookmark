from django.contrib import admin

from .models import Bookmark    ##admin.py는 모델을 관리자 페이지에 등록해 관리할 수 있도록 하는 역할과 관리자
                                # 페이지에서 보이는 내용의 변경, 기능 추가 등을 할 수 있도록 코드를 입력하는 파일입니다.

admin.site.register(Bookmark)   #from .models import Bookmark구문은 현재 폴더에 있는 models.py 파일에서
                                # Bookmark라는 모델을 불러오겠다 라는 의미입니다. 이렇게 불러온 모델을
#                               admin.site.register 구문을 이용해 등록하면 관리자 페이지에서 해당 모델을
#                               관리할 수 있습니다.

