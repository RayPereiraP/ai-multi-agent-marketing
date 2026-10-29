import os
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

# Configuração da chave de API
os.environ["OPENAI_API_KEY"] = "SUA_CHAVE_AQUI"
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# ==========================================
# 1. CRIANDO OS AGENTES (A EQUIPE)
# ==========================================

# Agente 1: Analista de Estratégia
estrategista = Agent(
    role='Analista Estrategista de Delivery',
    goal='Analisar o perfil do restaurante e o contexto para definir a melhor oferta',
    backstory='Você é um especialista em growth para delivery. Sabe exatamente o que faz as pessoas pedirem comida em dias de baixo movimento.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agente 2: Copywriter Criativo
copywriter = Agent(
    role='Copywriter de CRM',
    goal='Escrever textos persuasivos para Push Notifications e E-mails',
    backstory='Você escreve textos curtos, divertidos e que geram cliques (CTR alto). Você adora usar emojis e gatilhos de urgência sem ser chato.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agente 3: Revisor de Marca (QA)
revisor = Agent(
    role='Revisor de Tom de Voz da Marca',
    goal='Garantir que os textos estejam de acordo com as regras de compliance da plataforma',
    backstory='Você é o guardião da marca. Você não permite propagandas enganosas, promessas falsas de tempo de entrega, nem linguagem ofensiva.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ==========================================
# 2. DEFININDO AS TAREFAS
# ==========================================

dados_restaurante = """
Restaurante: 'Brazza Burger'
Especialidade: Hambúrgueres Artesanais (Smash)
Contexto: Terça-feira chuvosa, vendas 40% abaixo da meta.
Público: Jovens universitários.
Oferta disponível: Entrega Grátis ou Compre 1 Leve 2 no Smash Simples.
"""

tarefa_analise = Task(
    description=f'Analise os dados deste restaurante: {dados_restaurante}. Defina qual das duas ofertas disponíveis tem mais chance de conversão hoje e explique o porquê.',
    expected_output='Um parágrafo definindo a oferta escolhida e a justificativa estratégica.',
    agent=estrategista
)

tarefa_redacao = Task(
    description='Com base na oferta escolhida pelo estrategista, escreva: 1 título para Push Notification (máx 40 caracteres), 1 subtítulo para Push, e 1 Assunto de E-mail.',
    expected_output='Textos persuasivos formatados para Push e E-mail.',
    agent=copywriter
)

tarefa_revisao = Task(
    description='Revise os textos do copywriter. Se prometerem entrega "em 10 minutos" ou usarem palavrões, reescreva. Caso contrário, apenas aprove e retorne a versão final.',
    expected_output='O texto final revisado, polido e pronto para produção.',
    agent=revisor
)

# ==========================================
# 3. MONTANDO A CREW (A ORQUESTRAÇÃO)
# ==========================================

marketing_crew = Crew(
    agents=[estrategista, copywriter, revisor],
    tasks=[tarefa_analise, tarefa_redacao, tarefa_revisao],
    process=Process.sequential # Um trabalha depois do outro (Linha de montagem)
)

if __name__ == "__main__":
    print("🚀 Iniciando a Equipe de Agentes de Marketing...")
    resultado_final = marketing_crew.kickoff()
    
    print("\n\n==========================================")
    print("🎯 RESULTADO FINAL ENTREGUE PELA CREW:")
    print("==========================================")
    print(resultado_final)