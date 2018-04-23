# Caesar Encrypt
import key_generate

key = key_generate.v1_sum % 26

print 'Key generated from the matrices (v_sum % 26): '+str(key)

newtext = ''
text = raw_input('Enter your message to be encrypt: ');
    
for x in text:
    x = ord(x)
    #if it's small
    if(x >= 97 and x <= 122):
        x = x + int(key)
        if (x > 122):
            newtext += chr ( ( x % 122) + 96 )
        else:
            newtext += chr( x )
    # if CAPITAL    
    elif (x >= 65 and x <= 90):
        x = x + int(key)
        if (x > 90):
            newtext += chr ( ( x % 90) + 64 )
        else:
            newtext += chr ( x )
    else:
        newtext += chr (x)
        
print 'Encrypted message: '+newtext