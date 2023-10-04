import pandas as pd
import matplotlib.pyplot as plt

data = {
        'Name': ['John', 'Bob', 'Valentyn', 'Anna', 'Marks'],
        'Age': [17, 18, 21, 55, 60],
        'Gender': ['Man', 'Man', 'Man', 'Woman', 'Man'],
        'Score': [69, 50, 89, 88, 86]
    }

def first_graph():
    students = pd.DataFrame(data)
    print(students[:5])
    plt.bar(students["Name"], students["Score"])
    plt.xlabel("ім'я учня")
    plt.ylabel("Оцінка")
    plt.title("ОЦІНКИ")
    
    plt.show()
      
def dependence():
    students = pd.DataFrame(data)
    
    plt.scatter(students["Age"], students["Score"], label="Students")
    plt.xlabel("Вік")
    plt.ylabel("Оцінка")
    plt.title("Залежність між віком та оцінкою студентів")
    plt.legend()
    plt.show()
    
    
def categories():
    students = pd.DataFrame(data)
    values = students["Gender"].value_counts()
    print(values.index)
    
    plt.pie(values.values, labels=values.index,  autopct='%1.1f%%')
    plt.title('К-сть жінок та чоловіків')
    plt.legend()
    
    plt.show()
    
#first_graph()
#dependence()
categories()