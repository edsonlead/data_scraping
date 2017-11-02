import matplotlib.pyplot as plt
import seaborn as sns
from gastos_governo import ANOS, get_valores

v_presidencia = get_valores(20000)
v_ciencia_tec = get_valores(24000)
v_educacao = get_valores(26000)
v_prev_social = get_valores(33000)
v_saude = get_valores(36000)
v_meio_ambiente = get_valores(44000)
v_esporte = get_valores(51000)

def sinplot(valores,nome):
    plt.plot(ANOS, valores, label=nome)
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n")
    plt.xlabel("Anos")
    plt.ylabel("Em bilhões de R$")
    legend = plt.legend()
    #plt.savefig("sinplot.png")
    plt.show()

def multplot():
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n")
    plt.xlabel("Anos")
    plt.ylabel("Em bilhões de R$")
    plt.plot(ANOS, v_presidencia, label="Presidência da República")
    plt.plot(ANOS, v_ciencia_tec, label="Ciência e Tecnologia")
    plt.plot(ANOS, v_educacao, label="Educação")
    plt.plot(ANOS, v_prev_social, label="Previdência Social")
    plt.plot(ANOS, v_saude, label="Saúde")
    plt.plot(ANOS, v_meio_ambiente, label="Meio Ambiente")
    plt.plot(ANOS, v_esporte, label="Esporte")
    legend = plt.legend()
    #plt.savefig("multplot.png")
    plt.show()
