# resource_check 값에 따라 Toffoli / 분해 / AND Gate 버전으로 나뉨
# mode == False --> AND dag
def toffoli_gate(eng, a, b, c, mode=True):
    if(resource_check ==1):
        Tdag | a
        Tdag | b
        H | c
        CNOT | (c, a)
        T | a
        CNOT | (b, c)
        CNOT | (b, a)
        T | c
        Tdag | a
        CNOT | (b, c)
        CNOT | (c, a)
        T | a
        Tdag | c
        CNOT | (b, a)
        H | c
    elif resource_check == "quantum_AND":
        if mode:
            quantum_and(eng, a, b, c)
        else:
            quantum_and_dag(eng, a, b, c)
    else:
        Toffoli | (a, b, c)