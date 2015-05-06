problem = ['6c74', '6b22', '03df','69dc', '317a', '4546','2c03', '7fd7', '390e', '748b']
data = []

def compute(problem):
	base = data[17]
	print('Virtual Address ' + str(hex(problem)))
	pde_content = int(base[int(problem/1024)],16)
	pde_valid = int(pde_content/128);
	pdepfn = int(pde_content - pde_valid*128)
	print(' --> pde index:'+ str(hex(int(problem/1024))) + \
		'  pde contents:(valid '+str(pde_valid)+', pfn '+str(hex(pdepfn))+')')
	problem = problem%1024
	if pde_valid == 0:
		print('   --> Fault (page directory entry not valid)')
		return
	pte_data = data[pdepfn]
	pte_content = int(pte_data[int(problem/32)],16)
	pte_valid = int(pte_content / 128);
	ptepfn = pte_content - pte_valid*128
	print('   --> pte index:'+str(hex(int(problem/32))) + \
		'  pte contents:(valid '+str(pte_valid)+', pfn '+str(hex(ptepfn)+')'))
	problem = problem%32
	if pte_valid == 0:
		print('     --> Fault (page directory entry not valid)')
		return

	final_data = data[ptepfn]
	final_content = final_data[problem]
	final = ptepfn * 32 + problem
	print('      --> Translates to Physical Address ' + str(hex(final)) + '--> Value: ' + final_content)

fread = open('data.txt','r')
data_ = fread.read().split('\n')
fread.close()
for one in data_:
	data.append(one.split())
for one in problem:
	compute(int(one,16))




