xy=[]
x2=[]
x=[1,2,3,4,5,6,7,8]
y=[7,5,6,3,4,2.6,2,0.6]
sum_x=sum(x)
sum_y=sum(y)
prom_x=(sum_x/len(x))
prom_y=(sum_y/len(y))
for i in range(len(x)):
    xy.append(x[i]*y[i])
sum_xy=sum(xy)
for i in range(len(x)):
    x2.append(x[i]*x[i])
sum_x2=sum(x2)
m=((len(x)*(sum_xy))-(sum_x*sum_y)/((len(x)*sum_x2)-(sum_x*sum_x)))
b=float(prom_y-(m)*(prom_x))
print(f"\n\nLa ecuación de la recta de la regresión lineal es y = {m}x+({b})\n\n")
