### Problem
![image](https://github.com/user-attachments/assets/c6ffe909-8c66-4f0e-b795-5e8babdc3f64)

### Approach
Let's apply `Two pointer approach`.</br>
First pointer `i` pointing to the opening `$` & the second pointer `j` pointing to the closing `$`.

Will understand the approach through an example.

- At starting, `i` & `j` will be at the locations mentioned below.</br>
  ```python
  Walk the $ANIMAL$ in the $LOCATION$!<
  ij
  ```
- Step 1:</br>
  Initiate `i` & `j` next to each other.
  ```python
  def token_replace(s, tokens):  
      i = 0
      j = 1
  ```
- Step 2:</br>
  Think only about `i`.
  You need to do 2 things related to `i`.
  1. Checking the value at `i`
  2. Incrementing `i`
  ```python
  def token_replace(s, tokens):  
      i = 0
      j = 1  
      result = []
      while i < len(s):
          if s[i] != "$":
              result.append(s[i])
              i += 1
  ```
- Step 3:</br>
  At this point of time, you did whatever can be done with `i`.</br>
  Just makesure that `j` is immediatly next to `i`.
  ```python
  def token_replace(s, tokens):
      i = 0
      j = 1
      result = []
      while i < len(s):
          if s[i] != "$":
              result.append(s[i])
              i += 1
              j += 1
  ```
- Step 4:</br>
  At this point of time, `i` & `j` are at the below mentioned positions.</br>
  ```python
  Walk the $ANIMAL$ in the $LOCATION$!<
           ij
  ```
  From now onwards the code inside the `if` block stops executing.
  It's time to increment `j` until you find the next `$`,</br>
  so that, you can find the word between two `$` symbols.</br>
  Will achieve through this `elif` block, because the code inside the `elif`</br>
  block should execute only `if` block code is not getting executed.
  ```python
  def token_replace(s, tokens):
      i = 0
      j = 1
      
      result = []
      while i < len(s):
          if s[i] != "$":
              result.append(s[i])
              i += 1
              j += 1
          elif s[j] != "$":
              j += 1
  ```
  Once `j` is at the `$` symbol, the execution of code inside the `elif` block stops.</br>
  Beaware that, as of now;</br>
  code inside the `if` block won't execute</br>
  code inside the `elif` block won't execute</br>
  And, the position of `i` & `j` is as follows</br>
  ```python
  Walk the $ANIMAL$ in the $LOCATION$!<
           i      j
  ```
  Now, we have the word present between the `$` symbols. Find the corresponding token & append to result</br>
  ```python
  def token_replace(s, tokens):
      output = []
      i = 0
      j = 1
      while i < len(s):
          if s[i] != '$':
              output.append(s[i])
              i += 1
              j = i + 1
          elif s[j] != '$':
              j += 1
          else:
              key = s[i: j + 1]
              output.append(tokens[key])
  ```
  Now, Let's make the pointers position as follows so that will start things a fresh
    ```python
  Walk the $ANIMAL$ in the $LOCATION$!<
                   ij
  ```
  ```python
  def token_replace(s, tokens):
      output = []
      i = 0
      j = 1
      while i < len(s):
          if s[i] != '$':
              output.append(s[i])
              i += 1
              j = i + 1
          elif s[j] != '$':
              j += 1
          else:
              key = s[i: j + 1]
              output.append(tokens[key])
              i = j + 1
              j = i + 1
  ```
### Complete program:
```python
def token_replace(s, tokens):
    output = []
    i = 0
    j = 1
    while i < len(s):
        if s[i] != '$':
        output.append(s[i])
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
```
  
