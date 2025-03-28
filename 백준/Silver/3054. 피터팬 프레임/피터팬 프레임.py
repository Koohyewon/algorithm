import sys
input=sys.stdin.readline

word = input().strip()
n=len(word)

frame=[['.']*(4*n+1) for _ in range(5)]

for i, char in enumerate(word):
    idx=4*i+2   #문자 중앙배치 인덱스
    
    if(i+1)%3==0:   #웬디 프레임
        frame[0][idx]='*'
        frame[1][idx-1]=frame[1][idx+1]="*"        
        frame[2][idx-2]=frame[2][idx+2]="*"  
        frame[2][idx]=char
        frame[3][idx-1]=frame[3][idx+1]="*"        
        frame[4][idx]="*"
    else:   #피터팬 프레임
        frame[0][idx]='#'
        frame[1][idx-1]=frame[1][idx+1]="#"                    
        frame[2][idx+2]="#"  
        frame[2][idx]=char
        frame[3][idx-1]=frame[3][idx+1]="#"        
        frame[4][idx]="#"
        
        #웬디프레임이랑 겹치는 경우
        if frame[2][idx-2]!="*":
            frame[2][idx-2]="#"

for i in frame:
    print(''.join(i))                