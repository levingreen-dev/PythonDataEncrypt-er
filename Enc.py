import rsa

while True:
    message = input("Enter words to be encrypted: ")
    if message == 'break':
        break
    publicKey, privateKey = rsa.newkeys(4096)

    print(str(publicKey))
    print(str(privateKey))

    encMessage = rsa.encrypt(message.encode(),
                             publicKey)

    print("original string: ", message)
    print("encrypted string: ", encMessage)

    decMessage = rsa.decrypt(encMessage, privateKey).decode()

    print("decrypted string: ", decMessage)

    encMessage_str = encMessage.hex()

    file_object = open('Encryption.txt', 'w')
    file_object.write(str(encMessage))
