def pig_it(text):
    words = text.split()
    result = []
    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            result.append(new_word)
        else:
            result.append(word)

    return ' '.join(result)

print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
