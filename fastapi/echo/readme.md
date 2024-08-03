In the main.py directory, run the command below:
```uvicorn main:app --reload```

To test:
`curl -v -X GET http://localhost:8000/echo | jq`
