
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
For older python version please use: 
```bash
python main.py {{parameter}}
```
`{{parameter}}` refers to translation key entered by the user. Please find list of supported keys below: 

```
 ['cym', 'ces', 'deu', 'est', 'fin', 'fra', 'hrv', 'hun', 'ita', 'jpn', 'kor', 'nld', 'per', 'pol', 'por', 'rus', 'slk', 'spa', 'swe', 'urd', 'zho']
 ```

## Requirements 

To install requirements please execute this command within your cloned repository folder: 
```bash
pip install -r requirements.txt
```
