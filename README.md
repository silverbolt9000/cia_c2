# 🛰️ C2 Educacional - Sistema de Comando e Controle (inspirado no Vault 7)

Este projeto tem fins **educacionais** e demonstra como funciona um sistema de **Comando e Controle (C2)** simples, inspirado em ferramentas como **HIVE** da CIA (Vault 7 leaks), com foco em aprendizado de segurança ofensiva, programação cliente-servidor e conceitos de RATs.

> ⚠️ **Aviso legal:** Este projeto é para uso exclusivo em ambientes de teste/laboratórios controlados. **Não deve ser usado para qualquer fim malicioso ou sem autorização.**

---

## 📦 Estrutura do Projeto

```
cia_c2/
├── client/                  # Agente que se conecta ao servidor C2
│   ├── agent.py             # Código principal do agente
│   └── keylogger.py         # Keylogger que envia digitação em tempo real
├── server/                  # Servidor de Comando e Controle
│   ├── c2_server.py         # Backend Flask
│   └── templates/
│       └── dashboard.html   # Interface Web de controle
├── shared/                  # Configurações compartilhadas
│   └── config.py
└── README.md                # Documentação e instruções
```

---

## 🚀 Requisitos

- Python 3.8+
- Bibliotecas:
  ```bash
  pip install flask requests pynput
  ```

---

## ⚙️ Como usar

### 1. Inicie o Servidor C2

```bash
cd server
python c2_server.py
```

- Interface Web disponível em: [http://localhost:5000/dashboard](http://localhost:5000/dashboard)
- Use-a para enviar comandos e monitorar os resultados de cada agente.

### 2. Inicie o Cliente Agente

```bash
cd client
python agent.py
```

- O cliente se conecta ao servidor a cada 5 segundos, busca comandos e executa.
- O keylogger também inicia automaticamente e envia as teclas digitadas a cada 20 caracteres.

---

## 💻 Interface Web (Dashboard)

Acesse via navegador em:

```
http://localhost:5000/dashboard
```

### Funcionalidades:

- 🔍 Selecionar agente conectado
- 🧾 Enviar comando remoto (ex: `whoami`, `dir`, `uname -a`)
- 📄 Visualizar logs dos resultados e keylogs
- 🔄 Atualização automática dos logs a cada 5 segundos

---

## 🧪 Exemplos de Comandos

| Sistema | Comando útil         | Descrição                     |
|---------|----------------------|-------------------------------|
| Linux   | `uname -a`           | Informações do sistema        |
| Linux   | `ls -la`             | Listar arquivos               |
| Windows | `whoami`             | Nome do usuário               |
| Windows | `dir`                | Listar arquivos               |

---

## 🔐 Segurança e Ética

✅ Projeto com propósito **didático e acadêmico**  
❌ **Não usar em redes corporativas, computadores de terceiros ou sem consentimento.**  
✅ Ideal para **testes em VMs, ambientes de laboratório e CTFs.**

---

## 👨‍💻 Autor

Desenvolvido com fins educacionais e inspirado no estudo das ferramentas do Vault 7 liberado pela CIA.  
Implementado com Python + Flask + HTML (Bootstrap) com trabalho de engenharia reversa.

---
