def token_transform(s, tokens):
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
            key = s[i:j + 1]
            value = tokens[key]
            evaluated_value = token_transform(value, tokens)
            tokens[key] = evaluated_value
            output.append(evaluated_value)
            i = j + 1
            j = i + 1
    return ''.join(output)


tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
print(token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens))
# -> 'Walk the dog in the dog park!'