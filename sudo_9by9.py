
import sys
sys.getrecursionlimit()
sys.setrecursionlimit(10000)
global bt_flag

bt_flag=0


def dom_find(puz,i,j):

	dom=[]
	f_dom=[]
	t_puz=[]
	t_puz=puz
	fl_dom=[]
	#print(t_puz)

	univ_dom=[1,2,3,4,5,6,7,8,9]
	for k in univ_dom:
		flag1=0
		for c in [0,1,2,3,4,5,6,7,8]:
			if (k==t_puz[i][c]):
				flag1=1
				break
		if(flag1==0):
			dom.append(k)

	for l in dom:
		flag2=0
		for r in [0,1,2,3,4,5,6,7,8]:
			if (l==t_puz[r][j] and r!=i):
				flag2=1
				break
		if (flag2==0):		
			f_dom.append(l)

	if (i<=2 and i>=0):
		if(j<=2 and j>=0):
			s=0
			t=0
		if(j<=5 and j>=3):
			s=0
			t=3
		if(j<=8 and j>=6):
			s=0
			t=6
	if(i<=5 and i>=3):
		if(j<=2 and j>=0):
			s=3
			t=0
		if(j<=5 and j>=3):
			s=3
			t=3
		if(j<=8 and j>=6):
			s=3
			t=6
	if(i<=8 and i>=6):
		if(j<=2 and j>=0):
			s=6
			t=0
		if(j<=5 and j>=3):
			s=6
			t=3
		if(j<=8 and j>=6):
			s=6
			t=6

	x=s+2
	y=t+2
	
	for q in f_dom:
		flag3=0
		for a in [s,s+1,s+2]:
			for b in [t,t+1,t+2]:
				if (q==t_puz[a][b]):
					flag3=1
					break
		if (flag3==0):
			fl_dom.append(q)


	return fl_dom;


#Enter the Sudoku Table
#print("Enter the sudoku table")
#puz=[]
#for i in [1,2,3,4]:
#	row=[]
#	for j in [1,2,3,4]:
#		row.append(int(input()))
#	puz.append(row)

puz=[[1, 6, 0, 4, 0, 0, 3, 0, 0],[2, 0, 8, 9, 6, 0, 0, 4, 5],[0, 0, 0, 0, 8, 3, 1, 9, 0],[0, 0, 0, 0, 0, 9, 6, 0, 7],[0, 5, 7, 0, 3, 2, 0, 0, 1],[6, 4, 0, 5, 0, 0, 0, 3, 0],[7, 0, 2, 8, 0, 0, 0, 6, 0],[0, 9, 0, 0, 1, 5, 8, 0, 2],[3, 0, 5, 7, 0, 0, 9, 0, 4]]
print("Problem :")
print(puz)


def back_track(puz,prob,k):
	global bt_flag
	(i,j)=prob[k]
	#print(puz)
	if bt_flag==1:
		t=puz[i][j]
		puz[i][j]=0
		dom=dom_find(puz,i,j)
		#print(dom," ", k)
		if len(dom)==1:
			back_track(puz,prob,k-1)
		else:
			bt_flag=0
			for m in dom:
				if t==m:
					continue
				puz[i][j]=m
				if k<len(prob)-1:
					back_track(puz,prob,k+1)
				return
	else:
		dom=dom_find(puz,i,j)
		if len(dom)==0:
			bt_flag=1
			back_track(puz,prob,k-1)
		else:
			puz[i][j]=dom[0]
			if k<len(prob)-1:
				back_track(puz,prob,k+1)
			else:
				return


def sudoku_solver(puz):
	prob=[]
	que=[]

	for i in [0,1,2,3,4,5,6,7,8]:
		for j in [0,1,2,3,4,5,6,7,8]:
			if puz[i][j]==0:
				prob.append((i,j))
	#print(prob)
	back_track(puz,prob,0)
	print("Solution :")
	print(puz)




sudoku_solver(puz)





#Sudoku Solver Fuction Using BackTracking Search
