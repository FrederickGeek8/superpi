import sys
import re

pi = 2;
def super_pi(n):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(n):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2

result = EnvironmentError
while result is EnvironmentError:
    try:
        result = big_string.index(sys.argv[1])
    except:
      pi = pi * 2

    	digits = super_pi(pi)
    	pi_list = []
    	my_array = []

    	for i in super_pi(pi):
    		my_array.append(str(i))

    	my_array = my_array[:1] + ['.'] + my_array[1:]
    	big_string = "".join(my_array)
    	pass
arg = sys.argv[1]
line = re.sub(r'((%d))' % int(arg), r' [\1] ', big_string)
print line
