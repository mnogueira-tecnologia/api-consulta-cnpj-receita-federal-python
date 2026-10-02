# Integração da API CNPJ Receita Federal em Python – Consulta de CNPJ em tempo real

Exemplo de integração em **Python** com a API de Consulta CNPJ da Receita Federal da **ArquivoNfe**, para obtenção automatizada de dados cadastrais de empresas brasileiras.

A API permite consultar informações de empresas por meio do **CNPJ**, com opção de incluir o Quadro de Sócios e Administradores (QSA).

A integração utiliza processamento assíncrono por meio do `request_id`, permitindo enviar solicitações e consultar seus respectivos resultados posteriormente.

## 🔎 Palavras-chave

* API Consulta CNPJ Python
* API CNPJ Receita Federal
* Consulta CNPJ Python
* API Receita Federal
* Consulta CNPJ em tempo real
* API REST CNPJ
* Integração Python API REST
* Consulta dados cadastrais CNPJ
* Consulta QSA
* Consulta quadro societário
* API Fiscal Brasil
* Automação consulta CNPJ

## Benefícios

✔ Consulta de CNPJ com dados cadastrais<br>
✔ Dados provenientes da base da Receita Federal<br>
✔ Retorno de informações cadastrais e CNAE<br>
✔ Opção de consulta do Quadro de Sócios e Administradores (QSA)<br>
✔ Integração simples via API REST (JSON)<br>
✔ Processamento assíncrono utilizando `request_id`<br>
✔ Exemplo prático de integração em Python<br>
✔ Possibilidade de consultas individuais ou em lote

## Casos de uso

✔ Validação cadastral de clientes e fornecedores<br>
✔ Conferência cadastral antes da emissão de notas fiscais<br>
✔ Enriquecimento de bases de dados<br>
✔ Processos de KYC (Know Your Customer)<br>
✔ Automação fiscal e contábil<br>
✔ Integração com sistemas ERP e aplicações próprias<br>
✔ Automatização de processos de validação cadastral

## Diferenciais

✔ Consulta de dados cadastrais da Receita Federal.<br>
✔ Possibilidade de retorno do QSA e informações do Simples Nacional, conforme os dados disponibilizados pela API.<br>
✔ Comunicação segura por HTTPS.<br>
✔ Infraestrutura hospedada na Oracle Cloud no Brasil.<br>
✔ API REST com retorno em JSON.<br>
✔ Painel web para configurações, consultas manuais e acompanhamento das integrações via API.<br>
✔ Exemplo de integração utilizando Python e biblioteca `requests`.

---

## 🚀 Requisitos

* Windows ou Linux
* Python 3.x
* Git (opcional, caso escolha clonar o projeto)
* Biblioteca `requests`

---

## ⚙️ Como utilizar

### 1️⃣ Cadastre-se gratuitamente

Acesse o portal:

https://portal.arquivo-nfe.com

Crie sua conta para obter acesso à API.

---

### 2️⃣ Copie seu Token

Após o login no portal:

1. Acesse o menu **Meu Token**.
2. Copie seu token de acesso.

> ⚠️ **Nunca publique seu token de acesso no GitHub.**

No arquivo `consulta_cnpj_receita.py`, informe seu token apenas localmente:

```python
TOKEN = 'SEU_TOKEN_AQUI'
```

Antes de publicar o código no GitHub, certifique-se de que o token não esteja preenchido.

---

### 3️⃣ Instalação do Python

O exemplo utiliza **Python 3**.

#### Windows

Baixe o Python pelo site oficial:

https://www.python.org/downloads/windows/

Durante a instalação, marque a opção:

**Add python.exe to PATH**

Depois de concluir a instalação, abra o **Prompt de Comando (CMD)** e execute:

```bash
python --version
```

O comando deverá apresentar a versão instalada, por exemplo:

```text
Python 3.13.x
```

#### Linux

Verifique se o Python 3 está instalado:

```bash
python3 --version
```

Caso não esteja instalado, utilize o gerenciador de pacotes da sua distribuição.

Por exemplo, no Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

Depois confirme:

```bash
python3 --version
```

---

### 4️⃣ Baixe o projeto

Você pode baixar o projeto diretamente pelo GitHub ou cloná-lo utilizando o Git.

#### Opção 1 — Baixar ZIP

No GitHub, clique em:

**Code → Download ZIP**

Depois, extraia o arquivo em uma pasta do seu computador.

#### Opção 2 — Clonar com Git

Se o Git estiver instalado, execute:

```bash
git clone https://github.com/mnogueira-tecnologia/api-consulta-cnpj-receita-federal-python.git
```

Depois acesse a pasta do projeto:

```bash
cd api-consulta-cnpj-receita-federal-python
```

---

### 5️⃣ Crie um ambiente virtual Python

É recomendado utilizar um ambiente virtual para manter as dependências do projeto isoladas.

#### Windows

Dentro da pasta do projeto, execute:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

```bash
.venv\Scripts\activate
```

Após a ativação, o terminal deverá apresentar algo semelhante a:

```text
(.venv) C:\Users\seu_usuario\api-consulta-cnpj-receita-federal-python>
```

#### Linux

Crie o ambiente virtual:

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
source .venv/bin/activate
```

---

### 6️⃣ Instale as dependências

Com o ambiente virtual ativado, instale a biblioteca `requests` e as demais dependências do projeto:

#### Windows

```bash
pip install -r requirements.txt
```

#### Linux

```bash
pip3 install -r requirements.txt
```

Você também pode verificar se a biblioteca `requests` foi instalada corretamente:

```bash
pip show requests
```

---

### 7️⃣ Configure seu Token

Abra o arquivo [`consulta_cnpj_receita.py`](consulta_cnpj_receita.py) e informe seu token de acesso:

```python
TOKEN = 'SEU_TOKEN_AQUI'
```

> ⚠️ O token acima é apenas um exemplo. Nunca utilize ou publique tokens reais no GitHub.

Antes de executar o projeto, certifique-se de que o token esteja configurado corretamente.

---

### 8️⃣ Configure os CNPJs para consulta

No arquivo `consulta_cnpj_receita.py`, localize o array `consultas`.

Exemplo:

```python
consultas = [
    {
        "cnpj": "00000000000191",
        "qsa": 0,
        "request_id": None
    },
    {
        "cnpj": "33000167002317",
        "qsa": 1,
        "request_id": None
    }
]
```

Parâmetros:

| Parâmetro    | Descrição                                                        |
| ------------ | ---------------------------------------------------------------- |
| `cnpj`       | CNPJ da empresa que será consultada                              |
| `qsa`        | Indica se deve retornar o Quadro de Sócios e Administradores     |
| `request_id` | Protocolo da solicitação, preenchido automaticamente pelo script |

O parâmetro `qsa` aceita:

* `0` – Não solicitar o QSA.
* `1` – Solicitar o QSA.

O script pode ser adaptado para recuperar os CNPJs diretamente de um banco de dados, permitindo a integração com sistemas próprios.

---

### 9️⃣ Execute o exemplo

Com o ambiente virtual ativado e o token configurado, execute o script.

#### Windows

```bash
python consulta_cnpj_receita.py
```

#### Linux

```bash
python3 consulta_cnpj_receita.py
```

O script realizará as consultas configuradas no exemplo e exibirá os resultados retornados pela API no terminal.

O código demonstra:

* envio de consultas por CNPJ;
* opção de consulta do QSA;
* armazenamento do `request_id` (protocolo da consulta);
* consulta posterior dos resultados;
* novas tentativas quando a consulta ainda está em processamento;
* tratamento das respostas da API;
* exibição dos resultados em formato JSON.

O código-fonte completo está disponível em:

[`consulta_cnpj_receita.py`](consulta_cnpj_receita.py)

---

## 🔄 Como funciona o processamento assíncrono

A integração é realizada em duas etapas:

**Etapa 1 – Envio da consulta**

O script envia o CNPJ e o parâmetro opcional `qsa` para a API.

A API retorna um `request_id`, que identifica a solicitação.

**Etapa 2 – Obtenção do resultado**

O script utiliza o `request_id` para consultar o resultado da solicitação.

Caso o processamento ainda esteja em andamento, são realizadas novas tentativas, respeitando o intervalo e o limite configurados no exemplo.

Quando o resultado estiver disponível, os dados são apresentados no terminal em formato JSON.

Essa estrutura permite adaptar o exemplo para processamento em lote, aplicações empresariais e integração com bancos de dados.

---

## 📄 Exemplo de retorno da API

Após a conclusão do processamento, a API disponibiliza os dados cadastrais da empresa em formato JSON, incluindo informações como:

* CNPJ
* Razão social
* Nome fantasia, quando disponível
* Situação cadastral
* Endereço
* CNAE principal e secundários
* Natureza jurídica
* Informações do Simples Nacional, quando disponibilizadas
* Quadro de Sócios e Administradores (QSA), quando solicitado e disponível

A estrutura e os campos efetivamente retornados dependem dos dados disponibilizados pela Receita Federal e das opções da consulta.

---

## 🔗 Documentação da API

Consulte a documentação completa da API CNPJ Receita Federal:

https://www.arquivo-nfe.com/api-de-consulta-cnpj-receita-federal

**Endpoint:**

```text
POST https://api.arquivo-nfe.com/prod/cnpj_receita
```

Autenticação via Bearer Token.

---

## ⭐ Apoie o projeto

Se este projeto foi útil para você:

⭐ **Deixe uma estrela no repositório.**

Isso ajuda outras pessoas a encontrarem este exemplo de integração.

---

Made with ❤️ by **ArquivoNfe**

https://www.arquivo-nfe.com
