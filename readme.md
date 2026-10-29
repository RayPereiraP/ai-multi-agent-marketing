# 🤖 Multi-Agent Local Marketing Automator (CrewAI)

Uma aplicação de **Agentic AI** desenvolvida em Python e CrewAI para orquestrar campanhas de marketing hiper-personalizadas para restaurantes parceiros no ecossistema de delivery, de forma 100% autônoma.

## 🎯 Por que isso impressiona (Business Value)
Plataformas logísticas e marketplaces possuem a "cauda longa": centenas de milhares de pequenos parceiros que precisam de ajuda para vender. É impossível ter humanos criando campanhas de CRM (Push/Email) para cada hamburgueria que está com baixo movimento numa noite chuvosa.

**A Solução com Agentic Workflows:**
Em vez de usar um mega-prompt complexo que confunde a IA, este projeto utiliza o conceito de **Sistemas Multi-Agentes**. Criamos funcionários virtuais especializados que trabalham em linha de montagem:
1. 🧠 **Estrategista:** Analisa o clima, público e pratos e decide a melhor promoção.
2. ✍️ **Copywriter:** Recebe a estratégia e redige as notificações push e e-mails com gatilhos mentais.
3. 🛡️ **Revisor de Compliance:** Avalia o texto do copywriter e corta promessas falsas (ex: "Entrega em 5 minutos") garantindo o tom de voz da marca (Brand Safety).

## 🛠️ Stack Tecnológica
- **Orquestrador de Agentes:** CrewAI
- **Modelo de Inferência:** OpenAI `gpt-4o-mini` via LangChain
- **Linguagem:** Python

## 🚀 Como Executar

### 1. Instalação
\`\`\`bash
git clone https://github.com/seu-usuario/ai-multi-agent-marketing.git
cd ai-multi-agent-marketing
pip install -r requirements.txt
\`\`\`

### 2. Configuração e Execução
Insira sua chave da OpenAI no arquivo `src/crew.py` ou exporte no seu terminal:
\`\`\`bash
export OPENAI_API_KEY="sk-..."
\`\`\`

Execute o esquadrão:
\`\`\`bash
python src/crew.py
\`\`\`

### 👁️ O que você verá no console
Ao rodar, você verá literalmente os agentes "conversando" e passando o bastão. O Estrategista faz a análise, repassa para o Copywriter que começa a escrever, que por fim envia ao Revisor que aprova a campanha.