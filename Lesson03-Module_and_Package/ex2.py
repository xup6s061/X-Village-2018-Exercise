def set_answer():
    an=str(input('enter four numbers'))
    x=0
    y=0
    return x,y,an
def judge_guess():
    xj=x
    yj=y
    for i in range(0,4):
        if an[i]==ra[i]:
            xj+=1
        elif an[i]==an[i-1] or an[i]==an[i-2] or an[i]==an[i-3]:
            yj+=1
    return xj,yj

ra='1234'
xj=0
while xj!=4:
    r=set_answer()
    [x,y,an]=r
    t=judge_guess()
    [xj,yj]=t
    print(xj,'A',yj,'B')
print('correct')
