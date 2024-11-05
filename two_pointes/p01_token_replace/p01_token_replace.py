def token_replace(s, tokens):
    output = []
    i = 0
    j = 1
    while i < len(s):
        if s[i] != '$':
            output += s[i]
            i += 1
            j = i + 1
        elif s[j] != '$':
            j += 1
        else:
            key = s[i: j + 1]
            output.append(tokens[key])
            i = j + 1
            j = i + 1 
    return ''.join(output)

        
tokens = {
  '$LOCATION$': 'park',
  '$ANIMAL$': 'dog',
}
print(token_replace('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
# -> 'Walk the dog in the park!'