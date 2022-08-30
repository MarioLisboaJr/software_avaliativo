from setuptools import setup

setup(
      packages=['fourmatt'],
      version='1.0.0',
      description='Pacote para ETL de dados dos clientes da 4Matt Tecnologia',
      author='Mario Lisboa',
      author_email='mario_lisboa123@hotmail.com',
      py_modules=['extract', 'transform'],
      install_requires=['pandas==1.4.3']
      )
