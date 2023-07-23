import random
import string

message = input("Enter your message")
words = message.split(" ")
nwords = []


def encode():
    # message = input("Enter your message")
    # words = message.split(" ")
    # nwords = []
    for word in words:
        if (len(word) > 3):
            first_letter = word[0]
            # print(first_letter)
            new_message = word[1:]
            new_message1 = new_message+first_letter
            # print(new_message1)
            num_chars = 3
            random_chars1 = ''.join(random.choices(
                string.ascii_letters, k=num_chars))
            random_chars2 = ''.join(random.choices(
                string.ascii_letters, k=num_chars))
            # print(random_chars)
            encode_mess = random_chars1+new_message1+random_chars2
            # print(encode_mess)
            # return encode_mess
            nwords.append(encode_mess)
        else:
            encode_mess = word[::-1]
            # return encode_mess
            nwords.append(encode_mess)
    return (" ".join(nwords))


def decode():
    # message = input("Enter your message")
    # words = message.split(" ")
    # nwords = []
    for word in words:
        if (len(word) < 3):
            decode_mess = word[::-1]
            # return decode_mess
            nwords.append(decode_mess)
        else:
            new_message = word[3:]
            # print(new_message)
            new_message1 = new_message[:-3]
            # print(new_message1)
            last_letter = new_message1[-1]
            # print(last_letter)
            remove_last = new_message1[:-1]
            decode_mess = last_letter+remove_last
            # return decode_mess
            nwords.append(decode_mess)
    return (" ".join(nwords))


x = int(input("Enter 0 if you want to encode message or enter 1 if you want to decode message"))

if (x == 0):
    encoded = encode()
    print(encoded)
elif (x == 1):
    decoded = decode()
    print(decoded)
else:
    print("Invalid Number")
