n = 3
motor = [0]*n
def add(num, mov):
    motor[num] = mov
def move():
    print(motor)
    vr = ["1010", "0110", "0101", "1001"]
    while True:
        for j in range(4):
            st = []
            stop = 0
            for i in range(n):
                if motor[i] == 0:
                    st.append("0000")
                    stop += 1
                else:
                    st.append(vr[j])
                    motor[i] = motor[i]-1
            if stop == n:
                print("stop")
                return
            print(st)


add(0, 10)
add(1, 5)

move()