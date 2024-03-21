import pandas as pd
import matplotlib.pyplot as plt

#importing data from a csv file into a DataFrame

df=pd.read_csv("D:\AIandDSEngineering\Labs\Python\Plus2Python\Project\ipl.csv")
x=df["Team"]
y=df["Most Sixes"]
x1=df["Overall Rating"]
y1=df["Progress"]
x2=df["Won"]
y2=df["Loss"]
y3=df["Highest Runs"]
x4=df["Total Runs"]
y4=df["Team"]

def mainmenu():
    choice=0
    while choice!=4:
        print("\n----------------------------------------------------------------------------") 
        print(" ************************************IPL-MAIN MENU*************************** ")
        print("------------------------------------------------------------------------------")
        print("1. Display Data")
        print("2. Data Analysis")
        print("3. Data visualization")
        print("4. exit")
        choice=int(input("\nChoose an option from the Menu:"))
        if choice==1:
            print("Display Data")
            print(df)
            print(df.columns)
        elif choice==2:
            submenu2() 
        elif choice==3:
            submenu3()
        if choice==4:
            print("Thank You for using IPL Project ")
            break
        else:
            print(" Your Input is Wrong - Retry ")
               
    
#Sub Menu 2 for Data Analysis    

def submenu2():
    ch1=0
    while ch1!=7:       
        print("*************************DATA ANALYSIS***********************")
        print("-------------------------------------------------------------")
        print("1. Total Matches played in this season ")
        print("2. The team that was victorious in this season")
        print("3. The team that scored most runs in this season")
        print("4. Which team has more Netrunrate")
        print("5. Average sixes scored in this season")
        print("6. The team with Least run rate")
        print("7. Back to Main Menu ") 
                
        ch1=int(input("\nChoose an option for Data Analysis:"))
        if ch1==1:
            print()
            print("1.Total Matches played in the season ::",df["Match Played"].max())
            print()
            
        elif ch1==2:
            print()
            print("2.The team that was victorious in this season")
            print()
            print("The team that was victorious in this season is::",df["Team"].loc[0])
            print()
            print("------------------------------------------------------------------------------------")

        elif ch1==3: 
            print()
            print("3.  ****** The team that scored most runs in this season ******")
            print()
            df1=df.sort_values(by=["Total Runs"],ascending=False).head(1)
            print("The team that scored most runs in this season is :: \n",df1)
            print()
            print("------------------------------------------------------------------------------------")
        
        elif ch1==4:
            print()
            print("4.Which team has more Netrunrate")
            print()
            df2=df.sort_values(by=["Net run rate"],ascending=False).head(1)
            print("The team that has the most Net run rate is :: \n",df2)
            print()
            print("-----------------------------------------------------------------------------------")
        
        elif ch1==5:
            print()
            print("5.Average sixes scored in this season")
            print()
            print("The Average sixes scored in this season is ::",df["Most Sixes"].mean())
            print("------------------------------------------------------------------------------------")
        
        elif ch1==6:   
            print()
            print("6.The team with Least run rate")
            print()
            df3=df.sort_values(by=["Team"],ascending=True).head(1)
            print("The team with least run rate is:: \n",df3)
            print()
            print("------------------------------------------------------------------------------------")

        elif ch1==7:
            break
           
        else:
            print("Your Input is Wrong Retry ")
            
#Sub Menu 3 for Data Analysis

def submenu3():    
    ch2=0
    while ch2!=6:
        print("*******************DATA VISUALIZATION*******************")
        print("--------------------------------------------------------")
        print("1. SCATTER CHART for visualizing most sixes scored by different Teams")
        print("2. LINE PLOT for visualising the progress of different Teams")
        print("3. BAR PLOT for win-loss analysis of different Teams")
        print("4. HISTOGRAM for visualizing highest runs scored by different team")
        print("5. PIE CHART for visualizing total runs scored by different teams")
        print("6. Back to Main Menu ") 

        
        ch2=int(input("\nChoose an option for Data Visualization:"))
        if ch2==1:
            print("1.SCATTER CHART for visualizing most sixes scored by different Teams ::")
            plt.scatter(x,y,color="red")
            plt.xlabel("Team")
            plt.ylabel("Most Sixes")
            plt.title("MOST SIXES SCORED BY THE TEAMS")
            plt.show()
            print()
            print("------------------------------------------------------------------------------------")    
        
        elif ch2==2:             
            print("2.LINE PLOT for visualising the progress of different Teams ::")
            plt.plot(x1,y1,color="red",linestyle="--")
            plt.xlabel("Overall Rating")
            plt.ylabel("Progress")
            plt.title("PROGRESS OF DIFFERENT TEAMS")
            plt.legend()
            plt.show()
            print()
            print("------------------------------------------------------------------------------------")
    
        elif ch2==3:
            print("3.BAR PLOT for win-loss analysis of different Teams ::")
            plt.bar(x2,y2,color="blue")
            plt.xlabel("Won")
            plt.ylabel("Loss")
            plt.xticks(x2,x)
            plt.title("BAR PLOT FOR WIN-LOSS ANALYSIS OF DIFFERENT TEAMS ::")
            plt.show()
            print()
            print("------------------------------------------------------------------------------------")
    
        elif ch2==4:
            print("4.HISTOGRAM for visualizing highest runs scored by different team::")
            plt.hist(y3,10,edgecolor="r",facecolor="y")
            plt.xlabel("Team")
            plt.ylabel("Highest Runs")
            plt.title("HIGHEST RUNS SCORED BY DIFFERENT TEAMS")
            plt.xticks(y3,x)
            plt.show()
            print()
            print("------------------------------------------------------------------------------------")
            
        elif ch2==5:   
            print("5.PIE CHART for visualizing total runs scored by different teams ::")
            plt.pie(x4,labels=y4,explode=[0,0.1,0,0,0,0,0,0,0,0],shadow=True)
            plt.show()
            print()
            print("------------------------------------------------------------------------------------")
      
        elif ch2==6:
            break
    
        else:
            print("Your Input is Wrong Retry")
    
mainmenu()
