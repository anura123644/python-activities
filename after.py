class StringReverser:
    def __init__(self, sentence):
        # Encapsulating the sentence variable
        self.__sentence = sentence

    # Getter method to access the reversed string
    def get_reversed_sentence(self):
        # Splitting, reversing the words, and joining them back
        return ' '.join(reversed(self.__sentence.split()))

# Usage
sentence = "Encapsulation and Special Functions are cool"
revers