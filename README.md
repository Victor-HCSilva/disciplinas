# Manager

Uma aplicação web simples para gerenciar seu curso, construída com Python e Django.

## Pré-requisitos

*   **Python 3:** Certifique-se de ter o Python 3 instalado. Você pode baixá-lo em [python.org](https://www.python.org/).
    *   Durante a instalação no **Windows**, marque a opção "Add Python to PATH".
*   **Git:** Necessário para clonar o repositório.
*   **Sistema Operacional:** Este guia cobre a instalação e execução em **Linux**, **macOS** e **Windows**.

## Como Configurar e Usar

Siga estes passos para configurar o ambiente e rodar a aplicação localmente.

### 1. Clone o Repositório

Abra seu terminal (Terminal no Linux/macOS, Git Bash, Command Prompt ou PowerShell no Windows) e clone o repositório:

```bash
git clone https://github.com/Victor-HCSilva/disciplinas.git 
cd disciplinas
```

### 2. Crie um Ambiente Virtual

É uma boa prática usar um ambiente virtual para isolar as dependências do projeto. No diretório raiz do projeto, execute:

```bash
python -m venv .venv
```

*Nota: Dependendo da sua configuração, talvez precise usar `python3` em vez de `python`.*

### 3. Ative o Ambiente Virtual

Você precisa ativar o ambiente virtual em cada nova sessão do terminal antes de trabalhar no projeto.

**No Linux ou macOS (usando bash/zsh):**

```bash
source .venv/bin/activate
```

**No Windows:**

*   **Usando Command Prompt (cmd):**
    ```cmd
    .\.venv\Scripts\activate
    ```
*   **Usando PowerShell:**
    ```powershell
    .\.venv\Scripts\Activate.ps1
    ```
    *(Observação: Se você encontrar um erro sobre execução de scripts no PowerShell, pode ser necessário ajustar a política de execução para a sessão atual executando: `Set-ExecutionPolicy RemoteSigned -Scope Process` e tentando ativar novamente.)*

Após a ativação, você deverá ver `(.venv)` no início do prompt do seu terminal.

### 4. Instale as Dependências

Com o ambiente virtual ativado, instale todas as bibliotecas necessárias listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```
*(Certifique-se que o nome do arquivo está correto. O padrão é `requirements.txt`)*

### 5. Aplique as Migrações do Banco de Dados (Se aplicável)

Se o projeto Django utiliza um banco de dados (o que é comum), aplique as migrações:

```bash
python manage.py migrate
```

### 6. Inicie o Servidor de Desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento local do Django:

```bash
python manage.py runserver
```

### 7. Acesse a Aplicação

Abra seu navegador web e acesse o endereço fornecido no terminal. Geralmente será:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

Você deverá ver a aplicação web rodando! Para parar o servidor, volte ao terminal e pressione `Ctrl + C`.

---

Lembre-se de ativar o ambiente virtual (`passo 3`) sempre que abrir um novo terminal para trabalhar no projeto.


