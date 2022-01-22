
#Template string

from string import Template

name = 'all'
language ='python'

temp = Template('Hello $name! I am learning $language.')

print(temp.substitute(name= name,language=language))

