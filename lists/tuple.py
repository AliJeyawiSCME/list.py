print("tuples:")
t1 = ()
t2 = (1,2,3)
t3 = tuple([2 * x for x in range(1, 5)])
t4 = tuple("Ali")
print("t1:", t1,"\nt2:", t2,"\nt3:", t3,"\nt4:", t4)
t5 = t1+t2+t3+t4
print("t1 + t2 + t3 + t4 =", t5)

print("\nsets:")
s1 = set()
s2 = {1,3,5}
s3 = set([1,3,5])
s4 = set([2 * x for x in range(1, 10)])
s5 = set("abac")
print("t1:", s1,"\nt2:", s2,"\nt3:", s3,"\nt4:", s4,"\ns5:", s5)
print("sum of s4 values:",sum(s4))
print("length of s4:", len(s4))
print("s2 union t2:",s2.union(t2))
print("s2 intersection t2:",s2.intersection(t2))