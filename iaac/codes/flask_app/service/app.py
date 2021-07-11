from flask import Flask, jsonify, json, Response, request
from flask_cors import CORS
import boto3
import base64
from botocore.exceptions import ClientError
import psycopg2
import os
from os import path

app = Flask(__name__)
CORS(app)

conn = None
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DATABASE = os.environ["DATABASE"]
DB_USER = ""
DB_PASSWORD = ""

def get_secret():
    global rds_password
    secret_id = "rds"
    region_name = "ap-northeast-1"
    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )
    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_id
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        if 'SecretString' in get_secret_value_response:
            return get_secret_value_response['SecretString']
        else:
            return base64.b64decode(get_secret_value_response['SecretBinary'])

def set_connection():
    rds_secret = get_secret()
    try:
        global conn
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DATABASE,
            user=rds_secret.get('username'),
            password=rds_secret.get('password')
        )
    except (Exception, psycopg2.DatabaseError) as err:
        print(set_connection.__name__, err)
        exit(1)

set_connection()

@app.route("/")
def healthCheckResponse():
    return jsonify({"message" : "Nothing here, used for health check. Try /api instead."})

@app.route("/api")
def getResponse():
    # read the JSON from the listed file.
    response = Response(open("test-data.json", "rb").read())
    response.headers["Content-Type"]= "application/json"
    return response

@app.route("/get")
def getResponse():
    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute("""
                    SELECT *
                    FROM test
                    LIMIT 5;
                """, (return_count,))

                test = []
                row = curs.fetchone()
                while row is not None:
                    test.append(row)
                    row = curs.fetchone()
                return test
    except:
        print('DB Error')

@app.route("/create")
def getResponse():
    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute("""
                    CREATE TABLE test (id INT, name VARCHAR(10));
                    INSERT INTO test VALUES (1, 'test1'), (2, 'test2'), (3, 'test3');
                """, (return_count,))

                test = []
                row = curs.fetchone()
                while row is not None:
                    test.append(row)
                    row = curs.fetchone()
                return test
    except:
        print('DB Error')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
    