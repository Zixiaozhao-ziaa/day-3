# day-3

(**) - redo if you 
## SETUP ENVIRONMENT
1. create(**)
>python -m venv .venv
2. active(**)
>source .venv/bin/active

## install dependencies
1. create requirements.txt file
>touch requirements.txt
2. add to requirements.txtx
>openai
>streamlit
>python_dotenv
>chromadb
>pypdf
3. install requirements.txt (and freeze them so you can rely on them [NEXT STEP]) (**)
>pip install -r requirements.txt
4. and freeze the versions (do this everytime you add a new library / package to requirements.txt)
>pip freeze > requirements.txt

## .ENV FILE
1. create our environment file (for secrets)(**)
>touch .env
2. add to .evn file(**)
>OPENAI_API_KEY = ""
>PASSWORD = ""

add pages folder (to use pages in streamlit)
>mkdir pages

add streamlit entrypoint file
>touch home.py

streamlit run home.py