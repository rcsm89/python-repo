cDelator = str(input())
valDelatado = 0

if(cDelator != "roubo") and (cDelator!="homicídio") and (cDelator!="tráfico"):
    print("Crime inválido.")
else:

    if (cDelator == "roubo") or (cDelator == "tráfico"):
        valDelator = (int(input()))

    cDelatado = str(input())

    if(cDelatado != "roubo") and (cDelatado!="homicídio") and (cDelatado!="tráfico"):
        print("Crime inválido.")
    else:

        if (cDelatado == "roubo") or (cDelatado== "tráfico"):
            valDelatado = (int(input()))


        if(cDelator == "homicídio"):
            if(cDelatado=="homicídio"):
                print("Delação concedida.")
            elif(cDelatado == "roubo") or (cDelatado=="tráfico"):
                print("Delação rejeitada.")


        elif(cDelator == "roubo"):
            if(cDelatado == "roubo"):
                if(valDelatado > 5* valDelator):
                    print("Delação concedida.")
                else:
                    print("Delação rejeitada.")
            elif (cDelatado == "tráfico"):
                if(valDelatado > 3*valDelator):
                    print("Delação concedida.")
                else:
                    print("Delação rejeitada.")
            elif(cDelatado=="homicídio"):
                print("Delação concedida.")


        elif(cDelator == "tráfico"):
            if(cDelatado == "tráfico"):
                if(valDelatado > 5*valDelator):
                    print("Delação concedida.")
                else:
                    print("Delação rejeitada.")
            elif(cDelatado == "homicídio"):
                print("Delação concedida.")





