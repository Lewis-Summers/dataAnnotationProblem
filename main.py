def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    pyramid = []
    for line in lines:
        number, word = line.strip().split()
        pyramid.append((int(number), word))

    pyramid_sorted = sorted(pyramid, key=lambda x: x[0])

    index = 0
    increment = 2

    decoded_message = ""
    while index < len(pyramid_sorted):
        decoded_message = decoded_message + " " +pyramid_sorted[index][1]
        index += increment
        increment += 1

    return decoded_message

decoded_message = decode("file.txt")
print(decoded_message)
