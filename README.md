
---

# 📝 Montador de Escopo para Contratos com CNPJ

Este é um aplicativo desktop simples feito com Python e Tkinter que gera automaticamente um escopo de contrato com base em informações extraídas de um CNPJ, utilizando a API da ReceitaWS.

---

## 🚀 Funcionalidades

* Consulta informações de empresas através do **CNPJ**.
* Gera automaticamente um escopo formatado com os dados empresariais.
* Permite **copiar** facilmente o escopo gerado para a área de transferência.

---

## 🖼️ Interface Gráfica

A interface foi construída com o **Tkinter** e apresenta os seguintes campos:

* Campo de entrada para o CNPJ.
* Campo para inserir o modelo de escopo com placeholders.
* Área de saída com o escopo final preenchido.
* Botões para **gerar** e **copiar** o escopo.

---

## 🧠 Como Usar

1. **Digite o CNPJ** da empresa.

2. **Insira o escopo-modelo**, usando chaves `{}` para indicar os campos que deseja preencher.
   Exemplo:

   ```
   A empresa {nome_empresarial}, localizada em {logradouro}, {numero} - {bairro}, {cidade}/{uf}, inscrita sob o CNPJ {cnpj}, será responsável pelo fornecimento dos serviços.
   ```

3. Pressione **Enter** ou clique em **"Gerar Escopo"**.

4. O texto final aparecerá com os dados substituídos.

5. Clique em **"Copiar"** para copiar o escopo para a área de transferência.

---

## 🔄 Placeholders Disponíveis

Você pode utilizar os seguintes placeholders no texto do escopo:

| Placeholder          | Descrição       |
| -------------------- | --------------- |
| `{nome_empresarial}` | Nome da empresa |
| `{logradouro}`       | Rua/Avenida     |
| `{numero}`           | Número          |
| `{bairro}`           | Bairro          |
| `{cep}`              | CEP             |
| `{cidade}`           | Município       |
| `{uf}`               | Estado (UF)     |
| `{cnpj}`             | CNPJ formatado  |

---

## 📦 Requisitos

* Python 3.x
* Módulos:

  * `requests`
  * `tkinter` (incluso por padrão no Python)

Instale o `requests` com:

```bash
pip install requests
```

---

## ⚠️ Observações

* A aplicação utiliza a API pública da ReceitaWS: [https://www.receitaws.com.br/](https://www.receitaws.com.br/)
* A API pode ter **limitações de uso gratuito** por IP.

---

## 📄 Licença

Este projeto é de uso livre para fins educacionais e profissionais. Sinta-se à vontade para modificar e reutilizar.

---

