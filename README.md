# webscraping
webscraping com Python e Chrome DevTools Protocol

## Instalar as dependências do Python 3
```
pip install -r requirements.txt
```

## Inicie o Chrome com suporte ao protocolo de depuração remota
Aqui estão algumas maneiras possíveis de lançar o Chrome com suporte ao protocolo de depuração remota:

1. **No Windows**:
   ```bash
   "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
   ```
   ou
    ```bash
   "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
   ```

3. **No macOS**:
   ```bash
   /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
   ```

4. **No Linux**:
   ```bash
   google-chrome --remote-debugging-port=9222
   ```

5. **Outra opção é usar o caminho completo para o executável do Chrome**:
   Você pode precisar substituir `/path/to/chrome` com o caminho completo para o executável do Chrome no seu sistema.
   ```bash
   /path/to/chrome --remote-debugging-port=9222
   ```

Tente usar um desses comandos, substituindo os caminhos conforme necessário para o seu sistema, para lançar o Chrome com suporte ao protocolo de depuração remota. Se você ainda estiver tendo problemas, pode ser útil verificar a documentação do Chrome ou procurar online para obter instruções específicas para o seu sistema operacional e configuração.

## Executar Script
```bash
python ./main.py
```
