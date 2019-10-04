class Difference:
    def __init__(self, a):
        self.__elements = a
    def computeDifference(self):
        l=len(self.__elements)
        maxDiff=0
        for i in range(l):
            for j in range(l):
                if abs(self.__elements[i]-self.__elements[j])>maxDiff:
                    maxDiff=self.__elements[i]-self.__elements[j]

        self.maximumDifference=maxDiff


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
