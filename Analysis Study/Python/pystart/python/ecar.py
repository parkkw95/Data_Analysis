#!/usr/bin/env python
# coding: utf-8

# In[1]:

class Tesla(): # 클래스 기반의 속성과 메서드로 작업
    lno=2 # 프로퍼티 / 속성

    def __init__(self,modelName='m1'): #  초기화 메서드, 
        self.model=modelName
    def poweron(self): # 메서드,객체 함수
        print(self.model+'의 라이트가 켜졌습니다.')

# In[ ]:




