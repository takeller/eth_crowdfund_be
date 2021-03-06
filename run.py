import os
from src.seeds.seed import add_seeds
from src.app import create_app

env_name = os.getenv('FLASK_ENV')
app = create_app(env_name)

if __name__ == '__main__':
  port = os.getenv('PORT')
  # run app
  app.run(host='127.0.0.1', port=port)
  # app.run()

