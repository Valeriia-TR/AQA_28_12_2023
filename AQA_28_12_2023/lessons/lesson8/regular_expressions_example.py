import re

demostring = "date1 = 25-January-2024 date2 = 25-06-2024"
pattern = r"(\d{2})[-\.](\d{2}|\w+)[-\.](\d{4}|\d{2})"
pattern2 = r"[0-9]+.\w+.[0-9]+"
result = re.findall(pattern2, demostring)
print(result)


import re


'''
[]
[abc] ->a|b|c->[a-c]->[a-zA-Z]
\d->[0-9]
\D->[^0-9]      ^ means NOT
\s->[\t\n]
\S->[^\t\n]
\w->[a-zA-Z0-9_]
\W->[^a-zA-Z0-9_]

. any element
$ - ends due to pattern
*    >=0 matches
+    >=1 matches
?    0-1 matches
{n}  n matches



pattern = re.compile('abc')
print(pattern)

res = pattern.match('abcdf')
print(res)
res = pattern.match('bacdf')
print(res)
res = pattern.match('bacdfabc')
print(res)

pattern2 = re.compile('msg')
res = pattern2.search('msg1')
print(res)
res = pattern2.search('another msg1')
print(res)
res = pattern2.search('another msg1 msg')
print(res)
pattern3 = re.compile('msg')
res = pattern3.findall('another msg1 msg')
print(res)
res = pattern3.finditer('another msg1 msg')
print(res)
for i in res:
    print(i.span())
    print(i.group())
    print(i.start())
    print(i.end())

pattern = re.compile('\W')
result = pattern.split('this is test string')
print(result)
result = pattern.split('this is test string',2)
print(result)
result=re.split('\W', 'this is test string', 2)
print(result)

pattern=re.compile('(blue|red|yellow)')
res = pattern.sub('color', 'one red two yellow three green')
print(res)
res = re.sub('(blue|red|yellow)', 'color', 'one red two yellow three green')
print(res)
res2= re.sub('two', 'no defenitely three', res)
print(res2)


#pattern = re.subn('(blue|red|yellow)', 'color', 'one red two yellow three green', 1)
#print(pattern)

pattern = 'a'
demo_str = 'This is a demo string to count a'
result = re.findall(pattern,demo_str)
print(len(result))

demo_str = 'test string to find test'
res = re.search('test$', demo_str)
print(res)
res = re.search('^test', demo_str)
print(res)
res = re.search('(^test.+test$)', demo_str)
print(res)
res = re.search('(^test|test$)', 'string to find test')
print(res)
res = re.search('(^test|test$)', demo_str)
print(res)

res = re.search('[0-9]+', 'this is demo string 11')
print(res)
res = re.search('.*[0-9]*', 'this is demo string 1')
print(res)
res = re.search('.*[0-9]?', 'this is demo string 1')
print(res)

demo = "https://site.com"
pattern = "^https://.*\.([a-z]{3}|[a-z]{2})"
result = re.search(pattern, demo)
print(result)
result = re.search(pattern, 'https://sgdsfhdsghsfhsf.com fhjdghjsgh')
print(result)
'''
demo_str = "date1 = 25-01-2024 date2 = 25.06.2024"
pattern = '\d{2}[-\.]\d{2}[-\.]\d{4}'
result = re.findall(pattern, demo_str)
print(result)
demo_str = "date1 = 25-January-24 date2 = 25.06.2024"
pattern = '\d{2}[-\.](\d{2}|\w{7})[-\.](\d{4}|\d{2})'
pattern2 = '(\d{2})[-\.](\d{2}|\w+)[-\.](\d{4}|\d{2})'
pattern3 = '[0-9]+.\w+.[0-9]+'
result = re.findall(pattern3, demo_str)
for i in result:
    print(i, type(i))

#'(-|\.)'