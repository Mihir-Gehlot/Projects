import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("E:\\StatewiseTestingDetails.csv")
print("_"*120)
print()
print('\t','\t','\t',"COVID-19 DETAILS")
print()
print("_"*120)
print()
print("PRESS 1 TO ACCESS THE CSV FILE")
print("PRESS 2 TO ACCESS THE GRAPHS")
print()
choice=int(input("ENTER YOUR CHOICE :- "))
print()
if choice==1:## CSV MANUPLATION ##
    print("THESE OUR THE THINGS YOU CAN DO WITH OUR CSV :-  ")
    print()
    print("1. TO ACCESS ONLY THE STATE WITH TOTAL SAMPLES")
    print("2. TO ACCESS ONLY THE STATE WITH POSITIVE")
    print("3. TO ACCESS ONLY THE STATE WITH NEGATIVE")
    print("4. TO ACCESS THE WHOLE CSV")
    print()
    choice=int(input("ENTER YOUR CHOICE :- "))
    if choice==1:
        db=pd.read_csv("E:\\StatewiseTestingDetails.csv",usecols=['State','TotalSamples'])
        db.to_csv("E:\\StateWithTotalsamples.csv")
        print(db.groupby('State').sum())
    elif choice==2:
        db=pd.read_csv("E:\\StatewiseTestingDetails.csv",usecols=['State','Positive'])
        db.to_csv("E:\\StateWithPositive.csv")
        print(db.groupby('State').sum())
    elif choice==3:
        db=pd.read_csv("E:\\StatewiseTestingDetails.csv",usecols=['State','Negative'])
        db.to_csv("E:\\StateWithNegative.csv")
        print(db.groupby('State').sum())
    elif choice==4:
        db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
        print(db)
    else:

        print("INVALID CHOICE")
elif choice==2:## MATPLOTLIB ##
    print("THESE OUR THE GRAPH YOU CAN ACCESS IN OUR PROGRAM :- ")
    print()
    print("1.TO ACCESS THE LINE GRAPH")
    print("2.TO ACCESS THE BAR GRAPH")
    print("3.TO ACCESS THE HISTOGRAM GRAPH")
    choice=int(input("ENTER THE CHOICE:"))
    print()
    if choice==1:## LINE GRAPH ##
        print("1.TO MAKE A LINE GRAPH OF STATE WITH POSITIVE")
        print("2.TO MAKE A LINE GRAPH OF STATE WITH NEGATIVE")
        print("3.TO MAKE A LINE GRAPH OF STATE WITH TOTAL SAMPLES")
        choice=int(input("ENTER YOUR CHOICE :- "))
        if choice==1:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR line :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['Positive']
            plt.plot(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("POSITIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==2:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR line :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=range(1,7313)
            plt.plot(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("NEGATIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==3:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR line :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['TotalSamples']
            plt.plot(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("SAMPLES PER STATE")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        else:
            print("INVALID")
    elif choice==2:## BAR GRAPH ##
        print("1.TO MAKE A BAR GRAPH OF STATE WITH POSITIVE")
        print("2.TO MAKE A BAR GRAPH OF STATE WITH NEGATIVE")
        print("3.TO MAKE A BAR GRAPH OF STATE WITH TOTAL SAMPLES")
        choice=int(input("ENTER YOUR CHOICE :- "))
        if choice==1:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['Positive']
            plt.bar(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("POSITIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==2:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=y=range(1,7313)
            plt.bar(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("NEGATIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==3:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['TotalSamples']
            plt.bar(x,y,color=a)
            plt.xlabel("STATE")
            plt.ylabel("SAMPLES PER STATE")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        else:
            print("INVALID")
    else:## HISTOGRAM GRAPH ##
        print("1.TO MAKE A HISTOGRAM OF STATE WITH POSITIVE")
        print("2.TO MAKE A HISTOGRAM OF STATE WITH NEGATIVE")
        print("3.TO MAKE A HISTOGRAM OF STATE WITH TOTAL SAMPLES")
        choice=int(input("ENTER YOUR CHOICE :- "))
        if choice==1:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['Positive']
            plt.hist(x,bins=35,ec='black',color=a)
            plt.xlabel("STATE")
            plt.ylabel("POSITIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==2:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['Negative']
            plt.hist(x,bins=35,ec='black',color=a)
            plt.xlabel("STATE")
            plt.ylabel("NEGATIVE PATIENT")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        elif choice==3:
            a=input("ENTER THE COLOR OF YOUR CHOICE FOR BAR :- ")
            db=pd.read_csv("E:\\StatewiseTestingDetails.csv")
            x=db['State']
            y=db['TotalSamples']
            plt.hist(x,bins=35,ec='black',color=a)
            plt.xlabel("STATE")
            plt.ylabel("SAMPLES PER STATE")
            plt.xticks(db['State'],rotation=90)
            plt.title("COVID 19 GRAPH")
            plt.show()
        else:
            print("INVALID")
else:
    print("INVALID CHOICE")


            
        
            
            
            
            
            
        
