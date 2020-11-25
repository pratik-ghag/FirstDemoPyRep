f = open('Image1.jpg', 'rb')

f1 =  open('MyPic.jpg', 'wb')

for i in f:
    f1.write(i)