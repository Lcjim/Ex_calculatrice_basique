"""cette calculatrice suit la régle mathématique du zero"""
def Calculatrice(nb1,nb2,op):
    if (op == '+'):
        return nb1+nb2
    
    elif(op == '-'):
        return nb1-nb2
    
    elif(op == '*'):
        if nb1 and nb2 == 0:     
            return None
        else:
            return nb1*nb2
    elif(op == '/'):
        return nb1/nb2
nb1=int(input("donner donner le premier nombre"))
nb2=int(input("donner le second nombre"))
op=input("donner l'operateur que tu veux utilier pour le calcul")
print (Calculatrice(nb1,nb2,op))