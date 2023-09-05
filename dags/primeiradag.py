from airflow import DAG
import pendulum
from airflow.operators.python_operator import PythonOperator
from airflow.providers.jdbc.hooks.jdbc import JdbcHook
from twigo import *


#Definir argumentos padrão da DAG 

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 9, 5),
    'email': ['gabriela.favaro@combioenergia.com.br'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),

#Crie uma instância de DAG
 
    dag = DAG(
        'Olha minha dag', description="Eu sei fazer uma dag "
        schedule_interval=None, start_date=datetime(2023,9,5),
        catchup=False
        tags=['1-testedagabi'],
        )

#Estou definindo uma tarefa com o operador EmailOperator
    
    send_email_task = EmailOperator(
    task_id='enviar_email',
    to=['gabriela.favaro@combioenergia.com.br'],  
    subject='Nós sabemos fazer dags',
    html_content='''
    <html><body><p>Olá Querida, bom dia!</p><p>Voce sabe fazer dags</p><p>voce e demais</p> <br></html>
    '''
    dag=dag,
)







