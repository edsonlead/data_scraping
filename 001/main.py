from gastos_governo import get_valores
#from graph import grafico_individual, grafico_unificado
from graph import grafico_individual

# Obtendo os valores
v_presidencia = get_valores(20000)
v_ciencia_tec = get_valores(24000)
v_educacao = get_valores(26000)
v_prev_social = get_valores(33000)
v_saude = get_valores(36000)
v_meio_ambiente = get_valores(44000)
v_esporte = get_valores(51000)

grafico_individual(v_presidencia, "Presidência da República")
grafico_individual(v_ciencia_tec, "Ciência e Tecnologia")
grafico_individual(v_educacao, "Educação")
grafico_individual(v_prev_social, "Previdência Social")
grafico_individual(v_saude, "Saúde")
grafico_individual(v_meio_ambiente, "Meio Ambiente")
grafico_individual(v_esporte, "Esporte")

#grafico_unificado()
