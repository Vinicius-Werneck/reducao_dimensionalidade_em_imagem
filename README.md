# Conversor de Imagem para Tons de Cinza e Binarização

## Descrição
Este projeto implementa um conversor de imagem em Python que realiza duas transformações principais:
1. **Conversão para escala de cinza** (valores de pixel entre 0 e 255).
2. **Binarização** (transforma a imagem em preto e branco, com valores de pixel sendo apenas 0 ou 255).

## Tecnologias Utilizadas
- **Python 3.x**
- **Biblioteca Pillow (PIL)** para manipulação de imagens

## Como Usar
### 1. Instale as dependências
Se ainda não tiver a biblioteca Pillow instalada, execute:
```bash
pip install pillow
```

### 2. Configure o caminho da imagem
No código, altere a variável `path` para apontar para a imagem desejada:
```python
path = r"C:\Users\Local_Do_Arquivo\Imagem.png"
```

### 3. Execute o script
Para rodar o programa, utilize o seguinte comando no terminal:
```bash
python nome_do_arquivo.py
```

## Funcionamento do Código
1. **Carregar a imagem**:
   - O programa utiliza a biblioteca `PIL` para abrir e exibir a imagem original.

2. **Converter para escala de cinza**:
   - Aplica a fórmula: `0.299*R + 0.587*G + 0.114*B` para converter a imagem colorida para tons de cinza.

3. **Binarização da imagem**:
   - Define um limiar padrão de `127` para separar pixels em preto (0) e branco (255).

4. **Exibir as imagens processadas**:
   - Exibe as versões em tons de cinza e binarizada.

## Exemplo de Uso
Imagem original:

![Imagem original](Lena.png)

Imagem em tons de cinza:

![Imagem em tons de cinza](Lena_escala_cinza.png)

Imagem binarizada:

![Imagem binarizada](Lena_preto_branco.png)

## Autor
- **Vinícius Werneck**
- Data: 25/01/2025



