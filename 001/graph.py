import matplotlib.pyplot as plt
from gastos_governo import ANOS

def grafico_individual(valores, nome):
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(ANOS, valores, label=nome)
    legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, fontsize=12, borderaxespad=0.)
    legend.get_frame().set_facecolor('#ffffff')
    plt.show()
'''
def grafico_unificado():
    plt.grid(True, linestyle="--")
    plt.title("Gastos Destinados pelo Governo Federal (2004-2017)\n", fontsize="20")
    plt.xlabel("Ano", fontsize="16")
    plt.ylabel("Em bilhões de R$", fontsize="16")
    plt.plot(ANOS, v_presidencia, label="Presidência da República")
    plt.plot(ANOS, v_ciencia_tec, label="Ciência e Tecnologia")
    plt.plot(ANOS, v_educacao, label="Educação")
    plt.plot(ANOS, v_prev_social, label="Previdência Social")
    plt.plot(ANOS, v_saude, label="Saúde")
    plt.plot(ANOS, v_meio_ambiente, label="Meio Ambiente")
    plt.plot(ANOS, v_esporte, label="Esporte")
    formatacao_legenda = plt.legend(bbox_to_anchor=(1.01, 1), loc=2, fontsize=12, borderaxespad=0.)
    formatacao_legenda.get_frame().set_facecolor('#ffffff')

    #plt.rcParams["figure.figsize"] = [15,7]
    #plt.savefig("educ-sau.png")
    plt.show()
'''
