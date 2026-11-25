<div align="center">

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=200&color=0:050505,50:6d28d9,100:a855f7&text=GERADOR%20DE%20SENHAS&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=700&size=20&duration=2500&pause=800&color=C084FC&center=true&vCenter=true&width=700&lines=SECRETS+%2B+ARGON2ID;SENHAS+FORTES+EM+UM+COMANDO;SEGURAN%C3%87A+DESDE+O+IN%C3%8DCIO"/>

<img src="https://img.shields.io/badge/Python-3.10+-8A2BE2?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Argon2id-hash-6d28d9?style=for-the-badge"/>
<img src="https://img.shields.io/badge/testes-pytest-a855f7?style=for-the-badge&logo=pytest&logoColor=white"/>

</div>

---

## 🔐 Sobre

CLI e biblioteca em Python para **gerar senhas e frases-senha** com aleatoriedade criptográfica (`secrets`) e para **guardar senhas do jeito certo**, com hash **Argon2id**.

```bash
╭────────────────────────────────╮
│     GERADOR DE SENHAS v1.0     │
╰────────────────────────────────╯

✔ Aleatoriedade criptográfica (secrets)
✔ Um caractere de cada grupo garantido
✔ Embaralhamento Fisher-Yates seguro
✔ Frases-senha fáceis de lembrar
✔ Hash Argon2id (parâmetros OWASP)
✔ Estimativa de entropia

STATUS: PROTEGIDO 🛡️
```

## ⚡ Como usar

```bash
pip install -r requirements.txt

python -m gerador senha                 # 1 senha de 16 caracteres
python -m gerador senha -t 24 -q 5      # 5 senhas de 24 caracteres
python -m gerador senha --sem-ambiguos  # sem I, l, 1, O, 0, o
python -m gerador frase -p 6            # farol-cobre-abacaxi-cinza-ponte-vento-70
python -m gerador hash                  # pede a senha e mostra o hash Argon2id
python -m gerador verificar '<hash>'    # confere a senha contra um hash
python -m gerador forca                 # estima a força de uma senha
```

Como biblioteca:

```python
from gerador import gerar_senha, gerar_hash, verificar_hash

senha = gerar_senha(20)
h = gerar_hash(senha)          # $argon2id$v=19$m=65536,t=3,p=2$...
verificar_hash(h, senha)       # True
```

## 🧠 Por que assim?

| Escolha | Motivo |
|---|---|
| `secrets` em vez de `random` | `random` é previsível; `secrets` usa a fonte criptográfica do sistema |
| Argon2id | Vencedor da Password Hashing Competition, resistente a GPU e a ataques de canal lateral |
| Senha digitada com `getpass` | Não fica no histórico do terminal |
| Hash já inclui o salt | Nada de salt fixo ou guardado à parte |

## 🧪 Testes

```bash
pip install pytest
python -m pytest -q
```

---

<div align="center">

Feito por **[Johnny Lucas](https://github.com/Johnn5527)**

</div>

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&height=120&section=footer&color=0:050505,50:6d28d9,100:a855f7"/>
