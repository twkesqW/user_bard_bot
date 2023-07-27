from bardapi import Bard

token = 'ZQipZ361GGSFXERAbI3xUiSAprHlJY0BEfMExRt4lpygIuUEK-9Mmxn2X85_qQTO4jfpiQ.'
bard = Bard(token_from_browser=True)

def get_ans(txt):
    ans =  bard.get_answer(txt)['content']
    print(ans)
    return ans
