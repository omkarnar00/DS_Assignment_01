 
string = "eedyyoooda"
index = -1
fn = ""
for i in string:
    if string.count(i) == 1:
        fn+= i
        break
    else:
        index += 1
if index == 1:
    print("Either all characters are repeating or string is empty")
else:
    print("First non-repeating character is", fn)