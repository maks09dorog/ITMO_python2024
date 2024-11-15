#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html.

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

template1= ''


for key, val in page.items():
    if key in template:
        template1 += template[:template.index('?')] + val
        template = template[template.index('?') + 1:]
print(template1)
        # + template[:template.index('?')+1])



# for key, val in page.items():
#         if key in template:
#                 template.replace('?', val, 1)
# print(template)

# while page.items() != 0:
#         for key, val in page.items():
#             if key in template:
#                 template1 += template[:template.index('?')] + page.pop(key)
#                 print(template1)
#                 # + template[:template.index('?')+1])
