import sys
s = input()


while True:
    if s == ".":
        break
    stack = []
    ans = "yes"
    for i in range(len(s)):
        if "(" == s[i]:
            stack.append("(")
        elif "[" == s[i] :
            stack.append("[")
        elif ")" == s[i]:
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    ans = "no"
                    break
            else:
                ans = "no"
                break
        elif "]"  == s[i]:
            if stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    ans = "no"
                    break
            else:
                 ans = "no"
                 break
    if stack:
        ans = "no"
    print(ans)
    s = input()
