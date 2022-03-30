
# About

Python programming solution for an interview question provided by Kalvad. Co. 

## How it works?  

User must provide a translation key using CLI. Python code, written in `main.py` will access `countries.json` and return official translations under that key. 

## Installing 

 1. First, you need to clone this repository to your local machine. 

```bash
https://github.com/TheRadioDept/Tech-solution
```
2. Access cloned repository to work with it. 

```bash
cd Tech-solution
```

## Executing

To execute program:  
```bash
python3 main.py {{parameter}} 
```
For older pyhton version please use: 
```bash
python main.py {{parameter}}
```
`{{parameter}}` refers to translation key entered by the user. Please find list of supported keys below: 

```
 ['cym','deu','fra','hrv','ita','jpn','nld','por','rus','spa']
 ```

## Code formatting 

Code was formatted using `black` python formatter. If you do not have it installed, please execute this command to install it: 
```bash
pip install black
``` 
You can also enable it inside Visual Studio Code by following these instructions: 
1. Open your VSCode settings, by going 'Code -> Preferences -> Settings'.

2. Search for "python formatting provider" and select "black" from the dropdown menu. 

3. In the settings, search for "format on save" and enable the "Editor: Format on Save" option. 

For more information please see: `https://dev.to/adamlombard/how-to-use-the-black-python-code-formatter-in-vscode-3lo0`










