
# 📰 Crawler de Artigos

Este projeto é um crawler de artigos que coleta artigos de um site específico e salva o conteúdo em arquivos de texto.

## 🛠️ Requisitos

- Python 3.x
- `python-dotenv` para carregar variáveis de ambiente de um arquivo `.env`

## 🚀 Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/lopesleo/crawler-artigos.git
   cd crawler-artigos
   ```

2. Crie um ambiente virtual e ative-o:
   ```sh
   python -m venv venv
   venv\Scripts\activate  # No Windows
   # ou
   source venv/bin/activate  # No Linux/Mac
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:
   ```
   URL_ARTIGOS=xxxx
   NOME_PASTA=artigos
   ```

## 📖 Uso

1. Execute o script principal:
   ```sh
   python main.py
   ```

2. O script irá coletar os artigos do site especificado na variável `URL_ARTIGOS` e salvar o conteúdo em arquivos de texto na pasta especificada pela variável `NOME_PASTA`.

## 🗂️ Estrutura do Projeto

- `main.py`: Script principal que executa o crawler.
- `robot.py`: Contém a classe `Robot` que lida com a navegação e coleta de artigos.
- `utils/fileutils.py`: Contém funções utilitárias para manipulação de arquivos e pastas.
- `.env`: Arquivo de configuração com variáveis de ambiente.

## 🤝 Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

