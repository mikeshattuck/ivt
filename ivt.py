#!/usr/bin/python
#Author: Michael Shattuck

import math, sys, getopt

#This function returns the value of x against polynomial p
def pofx(p,x):
   val = 0
   for i in range(len(p)):
      val += p[i]*(x**i)
   return val

def ivt(p,a,b,c,attempts):
   
   an = [a]
   bn = [b]
   i = 0
   converges = False

   while i < attempts and converges == False:

      mid = (an[i]+bn[i])/2

      if pofx(p,mid) <= c:
         a_i_plus_1 = mid
         b_i_plus_1 = bn[i]
      else:
         a_i_plus_1 = an[i]
         b_i_plus_1 = mid

      an.append(a_i_plus_1)
      bn.append(b_i_plus_1)

      converges = math.isclose(an[i], bn[i], rel_tol=1e-10)

      i+= 1

   return an,bn,converges,i

def main(argv):
   a = 0
   b = 0
   c = 0
   attempts = 0
   p = []

   try:
      opts, args = getopt.getopt(argv,"h:p:a:b:c:m:")
   except getopt.GetoptError:
      print('ivt.py -p <poly coefficients> -a <avalue> -b <bvalue> -m <max iterations>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('ivt.py -p <poly coefficients> -a <avalue> -b <bvalue>')
         sys.exit()
      elif opt in ("-a"):
         a = int(arg)
      elif opt in ("-b"):
         b = int(arg)
      elif opt in ("-c"):
         c = int(arg)
      elif opt in ("-m"):
         attempts = int(arg)
      elif opt in ("-p"):
         p = [int(x) for x in arg.split(',')]

   print('IVT bisection method for polynomial with coefficients: ', 
      p, 'on (',a,',',b, ') for some f(x0) =',c)
   print('Attempting to iterate: ', attempts)

   an,bn,converges,i = ivt(p,a,b,c,attempts)
   
   print(f"{'Index' : <10}{'An' : <50}{'Bn' : <50}")
   for i in range(len(an)):
      print(f"{i : <10}{an[i] : <50}{bn[i] : <50}")

   if converges:
      print('Both series converged within a tolerance of 1e-10 after ', i, ' attempts!')
   else:
      print('Both series did not converage within a tolerance of 1e-10 after ', i, ' attempts.')

if __name__ == "__main__":
   main(sys.argv[1:])