h_s, m_s = map(int, input().split(':'))
h_e, m_e = map(int, input().split(':'))

def calc(h_s, h_e, m_s, m_e):
    diff_h = h_e - h_s
    diff_e = m_e - m_s

    if diff_h != 0:
        min = diff_h * 60
    else:
        min = 0
    min += diff_e 
    return min // 2

def converter(h_s, m_s, min):
    for _ in range(min // 60):
        h_s = shift_h(h_s)
        min -= 60
    min %= 60
    m_s += min
    min = 0
    if m_s >= 60:
        m_s = min % 60
        h_s = shift_h(h_s)
        
    return h_s, m_s


def shift_h(h_s):
    h_s += 1
    if h_s > 23:
        h_s = 0
    return h_s

def print_(h, m):
    h = '0'+str(h) if len(str(h)) == 1 else str(h)
    m = '0'+str(m) if len(str(m)) == 1 else str(m)
    print(h+':'+m)

min = calc(h_s, h_e, m_s, m_e)
h, m = converter(h_s, m_s, min)
print_(h,m)

