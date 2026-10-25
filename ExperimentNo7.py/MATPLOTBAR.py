import matplotlib.pyplot as plt
categories = ['Python', 'Java', 'C++', 'JavaScript', 'Go'] 
values = [90, 75, 60, 50, 40] 
plt.figure(figsize=(6, 4)) 
plt.bar(categories, values, color=['#1f77b4', '#f28e2b', '#e15759', '#76b7b2'])
plt.title('Popular Programming Languages') 
plt.xlabel('Languages') 
plt.ylabel('Popularity (%)') 
plt.ylim(0, 100) 
plt.show()
