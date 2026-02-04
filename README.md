# book-recommendation-analysis
Análise exploratória e limpeza de dados de um catálogo de livros utilizando Python e Pandas, com foco na identificação de preferências dos leitores.

📋 Sobre o Projeto
Este projeto realiza uma análise detalhada de um conjunto de dados de livros para identificar padrões e preferências dos leitores. Através de técnicas de análise exploratória de dados (EDA) e limpeza de dados, buscamos extrair insights valiosos que podem auxiliar em sistemas de recomendação de livros.

🎯 Objetivos
Realizar análise exploratória de dados (EDA) de um catálogo de livros
Identificar padrões e tendências nas preferências dos leitores
Limpar e preparar os dados para análises futuras
Gerar insights acionáveis sobre o comportamento dos leitores

🛠️ Tecnologias Utilizadas
Python 3.x - Linguagem de programação principal
Pandas - Manipulação e análise de dados
NumPy - Operações numéricas
Matplotlib/Seaborn - Visualização de dados (se aplicável)

📁 Estrutura do Projeto
book-recommendation-analysis/
│
├── books.csv                    # Dataset com informações dos livros
├── preferencia_leitores.py      # Script principal de análise
├── .gitignore                   # Arquivos ignorados pelo Git
└── README.md                    # Documentação do projeto

📊 Dataset
O dataset utilizado neste projeto foi obtido do Kaggle - Goodreads Books, contendo dados reais de livros da plataforma Goodreads.
O arquivo books.csv contém informações sobre diversos livros, incluindo (mas não limitado a):

Título do livro
Autor(es)
Gênero literário
Avaliações dos leitores
Ano de publicação
ISBN
Número de páginas
Avaliação média
Número de avaliações
Outras métricas relevantes

Fonte dos dados: Kaggle - Goodreads Books Dataset

🚀 Como Executar
Pré-requisitos
Certifique-se de ter o Python 3.x instalado em sua máquina. Você pode verificar executando:
bashpython --version
Instalação

Clone o repositório:

bashgit clone https://github.com/rubiamassaud/book-recommendation-analysis.git
cd book-recommendation-analysis

Instale as dependências necessárias:

bashpip install pandas numpy matplotlib seaborn
Execução
Execute o script de análise:
bashpython preferencia_leitores.py

🔍 Análises Realizadas
O projeto inclui as seguintes análises:

Análise Descritiva
Estatísticas básicas do dataset
Identificação de valores ausentes
Distribuição de variáveis


Limpeza de Dados
Tratamento de valores nulos
Remoção de duplicatas
Padronização de formatos


Análise de Preferências
Gêneros mais populares
Autores mais lidos
Tendências de avaliação


Insights
Padrões de comportamento dos leitores
Correlações entre variáveis
Recomendações baseadas em dados



📈 Principais Descobertas
[Os principais insights serão adicionados após a execução completa da análise]
Alguns exemplos de insights que podem ser extraídos:

Gêneros literários mais populares entre os leitores
Relação entre ano de publicação e avaliações
Autores com maior engajamento
Características de livros bem avaliados

🤝 Contribuindo
Contribuições são sempre bem-vindas! Se você tem alguma sugestão para melhorar este projeto, sinta-se à vontade para:

Fazer um fork do projeto
Criar uma branch para sua feature (git checkout -b feature/MinhaFeature)
Commit suas mudanças (git commit -m 'Adiciona MinhaFeature')
Push para a branch (git push origin feature/MinhaFeature)
Abrir um Pull Request

📝 Licença
Este projeto está sob licença livre para uso educacional e pessoal.
👩‍💻 Autora
Rubia Massaud

GitHub: @rubiamassaud

🙏 Agradecimentos

Dataset fornecido por Jealous Leopard via Kaggle
Dados originais da plataforma Goodreads

📧 Contato
Para dúvidas ou sugestões sobre o projeto, sinta-se à vontade para abrir uma issue no repositório.

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório!
