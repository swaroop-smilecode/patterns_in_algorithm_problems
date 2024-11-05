### Problem
```python
tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the dog park!'
```
### Approach
![image](https://github.com/user-attachments/assets/2f61508a-718f-4ef0-ac93-f19fd964a4eb)

![image](https://github.com/user-attachments/assets/d4aaf3b7-9f0d-435f-9eba-d8e918fa5dc6)

- Step 1</br>
  It's an extension of `token_replace` problem.</br>
  So, let's write `token_replace` code first.</br>
  ```python
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
              key = s[i: j + 1]
              output.append(tokens[key])
              i = j + 1
              j = i + 1
  
      return ''.join(output)
  ```
- Step 2</br>
As of now, we are getting the value to be replaced from dictionary & then appennding it to the result.</br>
Will do an elegant change here.</br>
Will treat this `value` as input once again & pass it to the `token_transform` function.</br>
By doing so, will keep replacing the nested tokens & at the end get the final value to be replaced `for that particular word`.</br>
  ```python
  else:
      key = s[i: j + 1]
      value = tokens[key]
      evaluated_value = token_transform(value, tokens)
      tokens[key] = evaluated_value
      output.append(evaluated_value)
  ```

  ```python
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
              key = s[i: j + 1]
              value = tokens[key]
              evaluated_value = token_transform(value, tokens)
              output.append(evaluated_value)
              i = j + 1
              j = i + 1
      return ''.join(output)
  ```
- Step 3</br>
  Let's implement `Memoization`</br>
  ```python
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
              key = s[i: j + 1]
              value = tokens[key]
              evaluated_value = token_transform(value, tokens)
              tokens[key] = evaluated_value # This is memoization
              output.append(evaluated_value)
              i = j + 1
              j = i + 1
      return ''.join(output)
  ```
