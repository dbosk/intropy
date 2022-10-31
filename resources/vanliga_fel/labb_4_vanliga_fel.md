Laboration 4 - Vanliga Fel
===========================

Efter att ha kollat igenom era inlämningar i labb 4 har vi nedan sammanställt en lista över diverse olika fel som återkommer. 

Uppdelning i funktioner/metoder
-----------------------
Vi har kommit en bit in i kursen nu, och det börjar bli dags att vi blir duktiga på att dela upp programmet i lämpliga funktioner. En bra tumregel att ha i åtanke är att det ska finnas en funktion för varje sak som dit programm *gör*. Namnet på funktionen bör därmed rimligen beskriva vad det är funktionen gör. 

Antag nu att vi ska skriva ett program som gör följande:
1. Låter användaren välja hur många tal som ska läggas till i en lista.
2. Beräkna talens aritmetiska medelvärde
3. Beräkna talens varians
4. Beräkna talens standardavvikelse
5. Jämföra variansen och standardavvikelsen genom att printa ut det största talet.

Vad som ofta händer är att programmet ser ut som nedan:

```python
def main():
    n = int(input("Choose an amount of numbers to examine: ")) # Step 1 done here
    
    nums = []
    for i in range(n):
        nums.append(float(input("Choose number " + str(i + 1) + ": ")))
    numsSum = 0
    for number in nums:
        numsSum += number
    mean = (1/n)*numsSum # Step 2 done here

    squareDevFromAvg = 0 
    for number in nums:
        squareDevFromAvg += (number - mean)**2
    variance = (1/(n - 1))*squareDevFromAvg # Step 3 done here

    standardDev = sqrt(variance) # Step 4 done here

    if standardDev > Variance:
        print("The standard deviation: " + str(standardDev) + ", is larger than the variance")
    elif standardDev > Variance:
        print("The variance: " + str(variance) + ", is larger than the standard deviation")
    else standardDev > Variance:
        print("The standard deviation: " + str(standardDev) + ", is equal to the variance")
    # Step 5 done here
main()
```

Nu kanske du undrar vad som är fel med det som står ovan. Jag gick ju igenom samtliga steg, och allt jag gjorde låg inom en funktion. Jo, men problemet är att massvis med olika saker ligger i *samma* funktion. Ett avsevärt lämpligare sätt att hantera problemet hade varit att definiera funktioner för de flesta steg i funktionen ovan. 

```python
def createNumList(amtOfNums):
    nums = []
    for i in range(amtOfNums):
        nums.append(float(input("Choose number " + str(i + 1) + ": ")))
    return nums 

def calcArithmeticMean(numList):
    numsSum = 0
    for number in nums:
        numsSum += number
    mean = (1/n)*numsSum
    return mean

def calcVariance(numList):
    mean = calcArithmeticMean(numList) 
    squareDevFromMean = 0 
    for number in nums:
        squareDevFromAvg += (number - mean)**2
    variance = (1/(n - 1))*squareDevFromMean

def compareVarianceToStandardDev(variance, standardDev):
    if standardDev > Variance:
        print("The standard deviation: " + str(standardDev) + ", is larger than the variance")
    elif standardDev > Variance:
        print("The variance: " + str(variance) + ", is larger than the standard deviation")
    else standardDev > Variance:
        print("The standard deviation: " + str(standardDev) + ", is equal to the variance")

def main():
    n = int(input("Choose an amount of numbers to examine: ")) # There's no need for a new function for this step ;)
    nums = createNumList(n)
    mean = calcArithmeticMean(nums)    
    variance = calcVariance(nums)
    standardDev = sqrt(variance) # Since the standard deviation is the square root of the variance this may still be okay. 
    compareVarianceToStandardDev(variance, standardDev)

main()
```

Notera hur mycket lättare det blir att följa vad det är som händer i vårt huvudprogram ovan. Om vi skulle vilja ändra i vårt huvudprogram blir detta också avsevärt lättare när vi delat upp det i funktioner som ovan.
