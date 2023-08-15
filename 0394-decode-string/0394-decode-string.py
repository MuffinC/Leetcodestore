class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        
        for x in range(len(s)):
            if s[x] !=']':
                stack.append(s[x])
            else:
                substring=""
                while stack[-1] != '[':
                    substring=stack.pop() +substring
                stack.pop()

                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop() + k

                stack.append(int(k) *substring )

        return "".join(stack)