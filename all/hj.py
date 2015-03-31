# -*- coding: cp936 -*- 
import os,sys 
base = [str(x) for x in range(10)] + [ chr(x) for x in range(ord('A'),ord('A')+6)] 

def bin2dec(string_num): 
	return str(int(string_num, 2)) 

def hex2dec(string_num): 
	return str(int(string_num.upper(), 16)) 

def dec2bin(string_num): 
	num = int(string_num) 
	mid = [] 
	while True: 
		if num == 0: 
			break 
		num,rem = divmod(num, 2) 
		mid.append(base[rem]) 
		return 
		''.join([str(x) for x in mid[::-1]]) 

def dec2hex(string_num): 
	num = int(string_num) 
	mid = [] 
	while True: 
		if num == 0: 
			break 
		num,rem = divmod(num, 16) mid.append(base[rem]) return ''.join([str(x) for x in mid[::-1]]) def hex2bin(string_num): return dec2bin(hex2dec(string_num.upper())) def buchong(x,y): while len(x) pde index:', print '0x'+bin2hex(f1), print ' pde contents:', if pde_1[0]=='1': print '(valid 1, pfn', tt = pde_1[1:8] print '0x'+bin2hex(tt)+')' pte = data[int(bin2dec(tt))] print ' --> pte index:', print '0x'+pte[int(bin2dec(f2))], pte_1= hex2bin(pte[int(bin2dec(f2))]) pte_1 = buchong(pte_1,8) if pte_1[0]=='1': print 'pte contents:(valid 1, pfn', tt = pte_1[1:8] print '0x'+bin2hex(tt)+')' print ' --> Translates to Physical Address', print '0x'+bin2hex(tt+f3), ans = data[int(bin2dec(tt))] #print ans,f3 ans_1= hex2bin(ans[int(bin2dec(f3))]) print '--> Value:' , print bin2hex(ans_1) else: print 'pte contents:(valid 0, pfn', tt = pte_1[1:8] print '0x'+bin2hex(tt)+')' print ' --> Fault (page table entry not valid)' else: print '(valid 0, pfn 0x', tt = pde_1[1:8] print bin2hex(tt), print ')' print ' --> Fault (page directory entry not valid)' print '' load() question =['6c74','6b22', '03df', '69dc', '317a', '4546', '2c03', '7fd7', '390e', '748b'] for i in question: work(i) 