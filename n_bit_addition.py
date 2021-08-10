from qiskit import QuantumCircuit,Aer,assemble
from qiskit.visualization import plot_histogram
from numpy import array
sim=Aer.get_backend('aer_simulator')
q=0
def conv(a,n): # defining a fuction to covert a decimal number into binary codes
  r=array([0,0,0,0,0])
  if a==1: #if the decimal numbe is one the fisrt value in array is made a 1
    r[0]=1
  for i in range(a): #the values in array is made one when the decimal number gives reminder on undergoin continues division by 2 
    if a>=1:
      r[i]=a%2
      a=a/2
    i=i+1
  return r
def sum_circuit(qc,i): #defining a function to add two bits and the carry from previous addition
  qc.ccx(i,i+1,i+3)
  qc.cx(i,i+1)
  qc.ccx(i+1,i+2,i+3)
  qc.cx(i+1,i+2)
  return qc
n= int(input("Enter number of bits used:")) #initializing number of bits to be used
a= int(input("Enter the first number:")) #initializing first input number
b= int(input("Enter the second number:")) #initializing second input number
ar=conv(a,n) #converting input 'a' into binarry
br=conv(b,n)  #converting input 'b' into binarry
qc=QuantumCircuit(3*n,n+1) #creating a quantum circuit 
for i in range(n): 
  if ar[i]==1: # this function converts the state of qubit into |1⟩ when ever there is 1 in the corresponding binary code
    qc.x(q)
  if br[i]==1:
    qc.x(q+1)
  q +=3
  i +=1
i=0
qc.ccx(i,i+1,i+2) #adding the first two qubits
qc.cx(i,i+1)
i=2
while i <= 3*(n-1): #continues addition of the following bits
  qc=sum_circuit(qc,i)
  i +=3
qc.barrier()
i=1
q=0
while q < n:
  qc.measure(i,q) #meassuring the result 
  q +=1
  i +=3
qc.barrier()
qc.measure((3*n)-1,n) #measuring the carry of highest value addition
qobj = assemble(qc) #simulating the circuit
counts = sim.run(qobj).result().get_counts()
plot_histogram(counts)  #plotting histogram
