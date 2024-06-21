import re

str1 = "转向架备件\
        Bogie spare parts"
pattern = r'[\u4e00-\u9fa5]+'   

a = re.findall(pattern, str1)
print(a)

