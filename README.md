# n_bit_addition
## addition of two n_bit numbers using qiskit
This is a qiskit algoritham to add a decimal number with another number.
<br>
libraries needed :-
  1. python3.
  2. qiskit .
  3. qiskit.visualization.
<br>
Two do addtion of two consiqutivebits with carry the following code is used:-
<br>
<code block>
qc.ccx(i,i+1,i+3) 
qc.cx(i,i+1) 
qc.ccx(i+1,i+2,i+3)
qc.cx(i+1,i+2)
</code block>
<br>
The number of bit of the biggest number has to be given as input.
<br>
The total number of bits used **3*n**
