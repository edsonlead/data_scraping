from graph import *

'''
    show values
'''
print(v_presidency)
print(v_science_tech)
print(v_education)
print(v_social_sec)
print(v_health)
print(v_environment)
print(v_sport)

'''
    show single graphs
'''
sinplot(v_presidency, "Presidência da República")
sinplot(v_science_tech, "Ciência e Tecnologia")
sinplot(v_education, "Educação")
sinplot(v_social_sec, "Previdência Social")
sinplot(v_health, "Saúde")
sinplot(v_environment, "Meio Ambiente")
sinplot(v_sport, "Esporte")

'''
    show everything together
'''
mulplot()
