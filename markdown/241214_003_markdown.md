# Markdown Quick Start

## 주석

`<!-- 주석 -->`

## \# heading text

h1 #  
h2 ##  
h3 ###  
h4 ####  
h5 #####  
h6 ######

## \<p> 문단 \</p>

안녕하세요  
문장 끝에 스페이스 두번은 줄바꿈\<br>

## 순서가 없는 아이템

- item 1
- item 2
  - item 2-1
  - item 2-2
    - item 2-2-1
  - item 2-3
- item 3

## 순서가 있는 아이템

1. order 1
2. order 2
   1. order 2-1
   2. order 2-2
3. order 3
   - item 3-1
   - item 3-2

## 하이퍼텍스트

`[google](https://www.google.com/)`

[google](https://www.google.com/)

## 이미지

`![alt text](img src)`

## 강조표기

```md
_italic_, **bold**, ~~취소선~~, `mono`
```

## 코드블록

` ```[python] code``` `


python

```python
print('hello')
```

cpp

```cpp
#include <iostream>

int main()
{
    std::cout << "Hello" << std::endl
    return 0;
}
```