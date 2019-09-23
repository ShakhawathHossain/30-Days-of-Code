def Total(mealCost,tipPersent,taxPersent):
    tip= (mealCost * (tipPercent / 100))
    tax= (mealCost * (taxPercent / 100))
    totalCost = round(mealCost + tip + tax)
    print(totalCost)



mealCost=float(input())
tipPercent=int(input())
taxPercent=int(input())
Total(mealCost,tipPercent,taxPercent)
