k=9
m="kajex"
a =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
message_decode = []
for i in list(m.strip()):
    index_code=a.index(i)
    index_decode=index_code-9
    lettre_decode=a[index_decode%len(a)]
    message_decode.append(lettre_decode)
message_decode_str=''.join([str(i) for i in message_decode])
print(message_decode_str)
