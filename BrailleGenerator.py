
braille_dict = {
        'a': '100000',
        'b': '101000',
        'c': '110000',
        'd': '110100',
        'e': '100100',
        'f': '111000',
        'g': '111100',
        'h': '101100',
        'i': '011000',
        'j': '011100',
        'k': '100010',
        'l': '101010',
        'm': '110010',
        'n': '110110',
        'o': '100110',
        'p': '111010',
        'q': '111110',
        'r': '101110',
        's': '011010',
        't': '011110',
        'u': '100011',
        'v': '101011',
        'w': '011101',
        'x': '110011',
        'y': '110111',
        'z': '100111',
        ' ': '111111',
    }

def generateBrailleCode(text):
    braille_text = ""
    for char in text:
        braille_text += braille_dict.get(char.lower(), char)

    s = braille_text
    segment_length = len(s) // len(text)

    # Split the string into six segments using list comprehension
    segments = [s[i:i+segment_length] for i in range(0, len(s), segment_length)]

    # save to array 3X2
    arr = []
    for seg in segments:
        temp = []
        for i in range(0,6,2):
            temp2 = []
            temp2.append(seg[i])
            temp2.append(seg[i+1])
            temp.append(temp2)
        arr.append(temp)

    # print(segments)
    # for i in range(len(text)):
    #     print(text[i])
    #     for b in arr[i]:
    #         print(b)

    return arr
