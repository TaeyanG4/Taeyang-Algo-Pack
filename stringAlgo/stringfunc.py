s = 'ABCdefgABC123345FDGHDGBdefgsh'
print(f'upper : {s.upper()}') # 문자열을 모두 대문자로
print(f'lower : {s.lower()}') # 문자열을 모두 소문자로
print(f'capitalize : {s.capitalize()}') # 문자열의 첫 글자만 대문자로
print(f'title : {s.title()}') # 문자열의 각 단어의 첫 글자만 대문자로
print(f'swapcase : {s.swapcase()}') # 대문자는 소문자로, 소문자는 대문자로
print(f'casefold : {s.casefold()}') # 모든 문자열을 소문자로 변환
print(f'center : {s.center(50)}') # 문자열을 중앙 정렬
print(f'center : {s.center(50, "*")}') # 문자열을 중앙 정렬, 공백은 *로 채움
print(f'count : {s.count("ABC")}') # 문자열의 개수를 반환
print(f'count : {s.count("ABC", 4, 10)}') # 문자열의 개수를 반환, 0~10번째 인덱스에서
print(f'find : {s.find("ABC")}') # 문자열의 인덱스를 반환, 없으면 -1
print(f'rfind : {s.rfind("ABC")}') # 문자열의 인덱스를 반환, 뒤에서부터 찾음
print(f'index : {s.index("ABC")}') # 문자열의 인덱스를 반환, 없으면 에러
print(f'rindex : {s.rindex("ABC")}') # 문자열의 인덱스를 반환, 뒤에서부터 찾음
print(f'isalnum : {"ABC123".isalnum()}') # 문자열이 알파벳 또는 숫자로만 구성되어 있는지
print(f'isalpha : {"ABC".isalpha()}') # 문자열이 알파벳으로만 구성되어 있는지
print(f'isdecimal : {"123".isdecimal()}') # 문자열이 10진수로만 구성되어 있는지
print(f'isdigit : {"123".isdigit()}') # 문자열이 숫자로만 구성되어 있는지
print(f'isnumeric : {"123".isnumeric()}') # 문자열이 숫자로만 구성되어 있는지 (숫자 표현도 포함 "Ⅳ", "四" )
print(f'isidentifier : {"123".isidentifier()}') # 문자열이 식별자로 사용할 수 있는지
print(f'islower : {"abc".islower()}') # 문자열이 소문자로만 구성되어 있는지
print(f'isupper : {"ABC".isupper()}') # 문자열이 대문자로만 구성되어 있는지
print(f'isspace : {" ".isspace()}') # 문자열이 공백으로만 구성되어 있는지
print(f'istitle : {"Abc".istitle()}') # 문자열이 title 형식으로 구성되어 있는지
print(f'join : {"_".join(["A", "B", "C"])}') # 문자열을 합침
print(f'ljust : {"ABC".ljust(10)}') # 문자열을 왼쪽 정렬
print(f'ljust : {"ABC".ljust(10, "*")}') # 문자열을 왼쪽 정렬, 공백은 *로 채움
print(f'rjust : {"ABC".rjust(10)}') # 문자열을 오른쪽 정렬
print(f'rjust : {"ABC".rjust(10, "*")}') # 문자열을 오른쪽 정렬, 공백은 *로 채움
print(f'zfill : {"ABC".zfill(10)}') # 문자열을 오른쪽 정렬, 공백은 0으로 채움
print(f'partition : {"ABCDEF".partition("CDE")}') # 문자열을 기준으로 나눔
print(f'rpartition : {"ABCDEF".rpartition("CDE")}') # 문자열을 기준으로 나눔, 뒤에서부터 찾음
print(f'replace : {"ABCDEF".replace("CDE", "cde")}') # 문자열을 바꿈
print(f'split : {"ABC DEF".split()}') # 문자열을 나눔
print(f'split : {"ABC DEF".split(" ")}') # 문자열을 나눔

text = "ABC\nDEF"
print(f'splitlines : {text.splitlines()}') # 문자열을 나눔
print(f'splitlines : {text.splitlines(True)}') # 문자열을 나눔, True면 \n도 포함
print(f'strip : {" abc ".strip()}') # 문자열의 양쪽 공백을 제거
print(f'lstrip : {" abc ".lstrip()}') # 문자열의 왼쪽 공백을 제거
print(f'rstrip : {" abc ".rstrip()}') # 문자열의 오른쪽 공백을 제거

text = "ABC\tDEF"
print(f'expandtabs : {text.expandtabs()}') # 문자열의 탭을 공백으로 바꿈
print(f'expandtabs : {text.expandtabs(2)}') # 문자열의 탭을 공백으로 바꿈, 공백은 2칸
print(f'expandtabs : {text.expandtabs(4)}') # 문자열의 탭을 공백으로 바꿈, 공백은 4칸
print(f'starstwith : {"ABCDEF".startswith("ABC")}') # 문자열이 특정 문자열로 시작하는지
print(f'endswith : {"ABCDEF".endswith("DEF")}') # 문자열이 특정 문자열로 끝나는지

text1 = "ABC\nDEF"
text2 = r"ABC\nDEF"
print(text1)
print(text2) # r을 붙이면 raw string으로 인식



