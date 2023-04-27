# True North Backend Code Challenge

## Run the Program
Open a terminal and navigate to truenorth-backend folder. Execute next command inside truenorth-backend folder:
```
$ uvicorn main:app --reload
```

## Trouble Shooting
Sometimes, you may need to install Python modules that are necessary for the proper functioning of the API. Check the requirements.txt file to see which modules should be installed in the Python environment that you are using. Missing Python modules can be installed as follows::
```
$ pip install -r requirements.txt
```

# Dockerfile
If you are using the backend in a Docker container, just run the next command to build:
```
$ docker build -t true-north-fast-api:latest .
```
After having the image, run de container in background with next command:
```
$ docker run -d -p 8000:8000 true-north-fast-api:latest
```

# Documentation
After having the project running, go to your browser to http://127.0.0.1:8000/docs