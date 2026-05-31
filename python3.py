def solve(s):
    words = s.split(' ')
    result = []
    
    for word in words:
        if word:
            result.append(word[0].upper() + word[1:])
        else: 
            result.append(word)
            
    return ' '.join(result)