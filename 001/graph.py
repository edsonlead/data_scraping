import matplotlib.pyplot as plt
import seaborn as sns
from spend import YEARS, get_value

"""
    CODES
    Presidency Republic: 20000
    Science and Technology: 24000
    Education: 26000
    Social Security: 33000
    Health: 36000
    Environment: 44000
    Sport: 51000
"""

v_presidency = get_value(20000)
v_science_tech = get_value(24000)
v_education = get_value(26000)
v_social_sec = get_value(33000)
v_health = get_value(36000)
v_environment = get_value(44000)
v_sport = get_value(51000)

def sinplot(values,name):
    plt.plot(YEARS, values, label=name)
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n")
    plt.xlabel("Anos")
    plt.ylabel("Em bilhões de R$")
    legend = plt.legend()
    plt.savefig(name+".png")
    plt.show()

def mulplot():
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n")
    plt.xlabel("Anos")
    plt.ylabel("Em bilhões de R$")
    plt.plot(YEARS, v_presidency, label="Presidência da República")
    plt.plot(YEARS, v_science_tech, label="Ciência e Tecnologia")
    plt.plot(YEARS, v_education, label="Educação")
    plt.plot(YEARS, v_social_sec, label="Previdência Social")
    plt.plot(YEARS, v_health, label="Saúde")
    plt.plot(YEARS, v_environment, label="Meio Ambiente")
    plt.plot(YEARS, v_sport, label="Esporte")
    legend = plt.legend()
    plt.savefig("mulplot.png")
    plt.show()
