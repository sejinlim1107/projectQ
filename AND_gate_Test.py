# AND gate Test
# ClassicalSimulator는 토폴리 분해 및 AND gate에 사용되는 T, H gate를 지원 X
eng = MainEngine() # MainEngine의 실제 양자컴퓨터 시뮬레이터 사용. (30큐빗 정도의 제한)
n = 1 # bit length

a = eng.allocate_qubit()
b = eng.allocate_qubit()
c = eng.allocate_qubit()

round_constant_XOR(1, a, n)
round_constant_XOR(1, b, n)
round_constant_XOR(0, c, n)

print_vector(eng,a,n)
print_vector(eng,b,n)
print_vector(eng,c,n)

quantum_and(eng,a,b,c)

print_vector(eng,a,n)
print_vector(eng,b,n)
print_vector(eng,c,n)

quantum_and_dag(eng,a,b,c)

print_vector(eng,a,n)
print_vector(eng,b,n)
print_vector(eng,c,n)

eng.flush()