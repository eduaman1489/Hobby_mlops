# Basic Setup 

1. [Github Account](https://github.com/eduaman1489)
2. [Linkedin Account](https://www.linkedin.com/in/aman-deep-6a3851120)


Create a new environment and some sanity checks 

```
conda create -p mlopsenv python==3.7 -y OR python -m venv mlopsenv
conda activate mlopsenv OR mlopsenv\Scripts\activate
python --version
py -0
python.exe -m pip install --upgrade pip
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Syncing VSCode with github repository  

```
Configure Git CLI with repository to push the files there 
Set registered email id with our Git CLI 
git config  --global user.name "Amandeep"
git config  --global user.email "edu.aman1489@gmail.com"
```

GIT Commands : add commit push  

```
git add . ===> Add all the files 
git add filename ===> Add specific file
git status ===> Check the status of the files 
git commit -m "your message" . ===> Commit the files to the origin (staging)
git push origin main ===> Finally push the files from Origin to Main
```

Streamlit Vs Flask Endpoint  

```
streamlit run streamlit_app.py
python run app.py
```


Docker - Avoids dependency, configuration issue between environments os etc.

```
From the Dockerfile, we will build the Docker Image
That Docker Image we will run in the Docker container which communicate with the kernel of the OS
FROM - select any base image from docker hub
COPY - copy all the code from base repository current location to that base image app folder 
WORKDIR - here we create that app folder mentioned above
RUN - run the dependecies like requirements.txt and install them 
EXPOSE - in order to acces the application inside the container, expose some port $PORT placeholder 
CMD - server like gUnicorn, assign workers , bind the $PORT with local address in the cloud 
```


Github Actions - CI/CD happens as soon as push happens on main branch 

```
Go to the Settings > Action Secrets > Add API_KEY,
Build 2 folders .github\workflows
Insider this folder , create a main.yaml file for the instructions and entire workflow
name - workflow name 
push - as soon as push happens on main branch, entire process will initiate
runs-on - ubuntu latest OS
```