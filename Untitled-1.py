'''
Функция которая принимает строку и возврощает ее же 
но с устоновленным первым символом в верхний регистр.
'''
def first_big(stringa):
  bs = "QWERTYUIOPASDFGHJKLZXCVBNM"
  sm = "qwertyuiopasdfghjklzxcvbnm"
  new_str = ""
  for i in stringa:
    if i == stringa[0] and i in sm:
      new_str += bs[sm.index(i)]
    else:
        new_str += i
  return new_str
print(first_big("hello"))
        
      
    