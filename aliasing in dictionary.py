d1={"up":"down","right":"wrong","true":"false"}
d2=d1
d3=d1.copy
#d2['right']="left"
#print("new updated value",d1["right"])

d3["right"]="incorrect"
print("new updated value",d1["right"])
