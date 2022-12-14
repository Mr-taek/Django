import re

# st="imhome/12345"
# s=re.match(r"^imhome/(?P<year>\d{4,10})?",st)
# print(s,s.group("year"))


st="imhome/1992/15-32/12"
s=re.match(r"^imhome/(?P<year>\d{4})/(?P<time>\d+[-/]\d+([/-]\d+)?)",st)
print(s,s.group("year"),s.group("time"))