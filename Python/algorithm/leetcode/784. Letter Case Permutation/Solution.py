class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = [S.lower()]  # 소문자로 바꾼 값을 결과에 넣어준다.

        for i in range(len(S)):
            # 문자열을 돌면서 해당 인덱스 값이 문자인 경우,
            if not S[i].isdigit():
                # 대문자로 치환해준 후 결과에 넣어준다.
                res.append(S[:i] + S[i].upper() + S[i+1:])                
                
                # 결과를 돌면서 모든 결과에 현재 인덱스를 대문자로 바꾼 값을 추가해 준다.
                for item in res: 
                    tmp = item[:i] + item[i].upper() + item[i+1:]
                    if tmp not in res:
                        res.append(tmp)
                        
        return list(set(res))
            