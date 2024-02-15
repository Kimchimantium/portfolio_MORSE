class Morse:

    def __init__(self):
        # list of morse symbols
        self.letter_morse_list = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
            "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
            "..-", "...-", ".--", "-..-", "-.--", "--.."  # a to z
        ]
        self.number_morse_list = [
            "-----", ".----", "..---", "...--", "....-",
            ".....", "-....", "--...", "---..", "----."  # 0 to 9
        ]
        # making dict of {char: morse}
        self.letter_morse_dict = {chr(n): self.letter_morse_list[n - 97] for n in range(97, 123)}
        self.number_morse_dict = {chr(n): self.number_morse_list[n - 48] for n in range(48, 58)}
        self.morse_dict = {**self.letter_morse_dict, **self.number_morse_dict}

    # logic function
    def morse_crypt(self, arg, return_list=False):
        arg = arg.replace("'", '').replace(",", '').replace("[", '').replace("]", '')
        morse_code = False
        result_morse, result_sentence = [], []
        if any(char in arg for char in ['/', '.', '-']):
            morse_code = True
        if not morse_code:
            for char in arg:
                if char == ' ':
                    result_morse.append('/')
                    result_morse.append(' ')
                else:
                    char = char.lower()
                    if char in self.morse_dict:
                        result_morse.append(self.morse_dict[char])
                        result_morse.append(' ')
            if return_list:
                return result_morse
            else:
                return ''.join(result_morse)
        else:
            # arg = arg.replace(' ', '')
            arg_list = arg.split(' ')
            for i in arg_list:
                if i == '/':
                    result_sentence.append(' ')
                else:
                    for key, value in self.morse_dict.items():
                        if value == i:
                            result_sentence.append(key)
            if return_list:
                return result_sentence
            else:
                return ''.join(result_sentence)