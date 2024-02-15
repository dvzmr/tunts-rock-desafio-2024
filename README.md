# Desafio Dev Training TUNTS.ROCK 2024

Este é um script Python que atualiza automaticamente uma planilha do Google Sheets no formato proposto pelo desafio com o status e as notas necessárias para aprovação no exame final dos alunos com base em critérios predefinidos.

## Funcionalidades

- Calcula o status do aluno (Aprovado, Reprovado, Reprovado por Falta ou Exame Final) com base em suas notas e frequência.
- Calcula nota necessária para aprovação em caso de Exame Final.
- Atualiza a planilha do Google Sheets com os status e notas calculados.

## Como Usar

1.**Instale as dependências necessárias:**

   ```bash
   pip install -r requirements.txt
 ```
2.**Configure as credenciais da API do Google Sheets:**

- Crie um projeto no [**Google Cloud Console**](https://console.cloud.google.com/)
- Ative a API do Google Sheets no projeto, não utilize a versão readonly.
- Crie credenciais OAUTH 2.0 e faça o download do arquivo JSON.
- Renomeie o arquivo JSON como credentials.json e coloque-o no mesmo diretório que o script.

3.**Execute o Script**

   ```bash
   python main.py
 ```
4.**Para executar os testes use o comando no diretório raiz do projeto:**

   ```bash
   pytest test/test_main.py -v
 ```

## Considerações

1.**Os valores informados para as notas na tabela de referência estão seguindo o padrão de 0 à 100 mas as regras da aplicação informadas no corpo do desafio eram no formato 0 a 10. Utilizei os valores da tabela e desenvolvi a aplicação utilizando o padrão 0 à 100 respeitando o a proporcionalidade das regras propostas no corpo do desafio.**

2.**Os valores que foram arredondados e desdobramentos de seus resultados foram considerados no momento do desenvolvimento dessa aplicação.**


## Contato e Autoria
[David Moura](https://www.linkedin.com/in/davidmouraz/) \
[mourazdavid@gmail.com](mailto:mourazdavid@gmail.com)


