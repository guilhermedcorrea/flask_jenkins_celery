from app import create_app

app = create_app()


if __name__ == "__main__":
    app.run(host='0.0.0.0', 
        threaded=True, port=5000, debug=True)

#RUN docker run --network flask-bridge --name database -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=admin -e POSTGRES_DB=teste -p 5434:5432 postgres:15



'''



  #RUN docker run --network flask-bridge --name database -e POSTGRES_PASSWORD=123 -e POSTGRES_USER=admin -e POSTGRES_DB=teste -p 5434:5432 postgres:15

    container_name: database3
    networks:
      - flask-bridge
  app:
    image: flaskapp_newapp
    container_name: app
    networks:
      - flask-bridge
    ports:
      - 5000:5000
    depends_on:
      - postgresql

networks:
  flask-bridge:
    driver: bridge

'''