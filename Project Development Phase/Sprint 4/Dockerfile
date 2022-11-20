FROM python
WORKDIR /newsapp
COPY . .
RUN pip install -r requirement.txt
CMD ["Python","nta_app.py","-h","0.0.0.0"]
EXPOSE 3000