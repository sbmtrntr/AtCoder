S = input() #文字列Sを受け取ります

ans = "" #文字列型の変数ansを作っておきます

for i in range(len(S)): #len()で文字列の長さ取得
    if S[len(S)-i-1] == "6":
        ans += "9"
    elif S[len(S)-i-1] == "9":
        ans += "6"
    else:
        ans += S[len(S)-i-1]

print(ans)
