# Count Bank
 Esse é um projeto pessoal simples para auxiliar no gerenciamento de finanças pessoais. 

 ## Sobre o CountBank
 O CountBank é uma aplicação simples que lhe permite adcionar recibos e despesas, podendo gerenciar
 da melhor forma o seu dinheiro. É valido destacar que para a criação de cada arquivo .csv por mês, 
 ele também leva em conta o balanço total do mes anterior, que será adcionado no novo arquivo.

 ## Funcionalidades
 [1] - CRIAR TABELAS .CSV PARA ARMAZENAR OS RECIBOS E DESPESAS CONFORME FOR ADCIONANDO.

 [2] - ADCIONAR RECIBOS (SÁLARIO, MESADA, DINHEIRO EXTRA, ETC).

 [3] - ADCIONAR DESPESAS (CONTAS, DIVÍDAS, ETC).

 [4] - VIZUALIZAR O BALANÇO FINAL ENTRE OS RECIBOS E DESPEZAS.
 

 # Como funciona
 O programa é rodado no terminal de forma interativa (ele executa os comandos que o usuário digitar) conforme
 seus comandos e utilizades. Para manter uma certa estetica visual, utiliza-se ASCII arts.

 # Como rodar o Count Bank
 [1] - Tenha o python 3.12 instalado na sua máquina.

 [2] - Baixe esse repositorio e extraia ele.

 [3] - Entre no diretório onde os arquivos foram extraidos

 [4] - Crie e ative seu ambiente virtual por meio dessas linhas de codigo (os codigos funcionaram para Linux/MAC, mas são similares para Windows também): 
 ```
    python3 -m  venv CountBank (Criar ambiente virtual)
    source CountBank/bin/activate (ativar ambiente virtual)
 ```
 [5] - Com o ambiente virtual ativado, instale as dependencias necessárias:
```
    pip install -r requirements.txt
```
 [6] Execute o seguinte script para poder rodar a aplicação:
 ```
    python3 main.py
 ```

 OBS: Esse projeto tem um cunho mais educativo/pessoal, apesar de ter sido criado por uma
 necessidade administrativa e financeira. Apesar de simples, ele se faz o que se propoe a 
 fazer.