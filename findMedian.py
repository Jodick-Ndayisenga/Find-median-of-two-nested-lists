class Median:
    def Find(self, list1:list, list2:list) -> float:
        mainList = (list1+list2)
        mainList.sort()
        Length = len(mainList)
        print(f'Your new list is: {mainList}')
        if Length%2==1:
            median = mainList[int((Length-1)/2)]
        else:
            median = (mainList[int(Length/2)] + mainList[int((Length/2)-1)])/2
        return median

firstMedian = Median()
print(firstMedian.Find([1,3,10,9,6,8,7],[2]))
