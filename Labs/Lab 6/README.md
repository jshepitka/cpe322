# Lab 6 - Node.js and Pystache

## Lab 6A: Node.js

-Node.js already installed (used for senior design)

Programs from IoT Repository Lesson6

```node hello-world.js```: 
![image](https://user-images.githubusercontent.com/37707211/236648693-08d30ad7-1266-4d80-b149-d4b2b801e05f.png)


```node hello.js```:
-showed "Hello World!" like previous screenshot on port 8080.

```node http.js```:
-Displayed "THis page was refreshed _ times!" and counted up every time page refreshed. used same port as previous program (8080). Count also shown in console.

---
## Lab 6B: Pystache

```$ pip install pystache``` installed pystache.

Example code:
```
$ cat say_hello.mustache
Hello, {{to}}!
```

```
$ cat say_hello.py
# https://github.com/defunkt/pystache
import pystache
print(pystache.render('Hi {{person}}!', {'person': 'Alexa'}))

# Create dedicated view classes to hold view logic
class SayHello(object):
    def to(self):
        return "World"
hello = SayHello()

# Use template in say_hello.mustache
renderer = pystache.Renderer()
print(renderer.render(hello))

# Pre-parse a template
parsed = pystache.parse('Hey {{#who}}{{.}}!{{/who}}')
print(parsed)
print(renderer.render(parsed, {'who': 'Google'}))
print(renderer.render(parsed, {'who': 'Siri'}))
```

```
$ python say_hello.py
Hi Alexa!
Hello, World!

['Hey ', _SectionNode(key='who', index_begin=12, index_end=18, parsed=[_EscapeNode(key='.'), '!'])]
Hey Google!
Hey Siri!
```
