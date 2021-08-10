from qiskit import QuantumCircuit,Aer,assemble
from qiskit.visualization import plot_histogram
from numpy import array
sim=Aer.get_backend('aer_simulator')
q=0
def conv(a,n):
r=array([0,0,0,0,0])
if a==1:
r[0]=1
for i in range(a):
if a>=1:
r[i]=a%2
a=a/2
i=i+1
return r
def sum(i):
qc.ccx(i,i+1,i+3)
qc.cx(i,i+1)
qc.ccx(i+1,i+2,i+3)
qc.cx(i+1,i+2)
return qc
n= int(input("Enter number of bits used:"))
a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
ar=conv(a,n)
br=conv(b,n)
qc=QuantumCircuit(3*n,n+1)
for i in range(n):
if ar[i]==1:
qc.x(q)
if br[i]==1:
qc.x(q+1)
q +=3
i +=1
i=0
qc.ccx(i,i+1,i+2)
qc.cx(i,i+1)
i=2
while i <= 3*(n-1):
qc=sum(i)
i +=3
qc.barrier()
i=1
q=0
while q < n:
qc.measure(i,q)
q +=1
i +=3
qc.barrier()
qc.measure((3*n)-1,n)
qobj = assemble(qc)
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)
