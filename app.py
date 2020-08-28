import re
import pyperclip

#creating regex pattern
matcherPhone = re.compile(r'''(
(\d{3}|\(\d{3}\))? 
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4}) 
(\s*(ext|x|ext.)\s*(\d{2,5}))?                         
)
''', re.VERBOSE)

matcherEmail = re.compile(r'''(
 [a-zA-Z0-9._%+-]+
 @
 [a-zA-Z0-9.-]+
 (\.[a-zA-Z]{2,4})
 )''', re.VERBOSE)

# text from clipboard
text = str(pyperclip.paste())
matches = []

for groups in matcherPhone.findall(text):
    number = groups[0]
    matches.append(number)

for groups in matcherEmail.findall(text):
    matches.append(groups[0])

# copy to clipboard
if matches:
    pyperclip.copy('\n'.join(matches))
    print('\n'.join(matches))
else:
    print('no output')