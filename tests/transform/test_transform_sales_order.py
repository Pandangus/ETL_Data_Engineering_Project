# import moto.core
from moto import mock_s3
import boto3
import pytest
import awswrangler as wr
from src.utils.table_transformations import transform_sales_order
from pprint import pprint


@pytest.fixture
def create_s3_client():
    with mock_s3():
        yield boto3.client('s3', region_name='eu-west-2')


@pytest.fixture
def mock_client(create_s3_client):
        '''
        fixture creates 'test-ingestion-va-052023' bucket in 
        mock aws account and uploads 'test.txt' file to it
        '''
        mock_client = create_s3_client
        ingestion_bucket_name = 'mock-test-ingestion-va-052023'
        processed_bucket_name = 'mock-test-processed-va-052023'
        mock_client.create_bucket(
             Bucket=ingestion_bucket_name, 
             CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'},
             )
        mock_client.create_bucket(
             Bucket=processed_bucket_name, 
             CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'},
             )
        with open('tests/transform/test_data_csv_files/test_sales_order.csv', 'rb') as data:
            mock_client.upload_fileobj(data, ingestion_bucket_name, 'test.csv')
        yield mock_client


def test_transform_sales_order_retrieves_csv_file_from_ingestion_s3_bucket_and_puts_parquet_file_in_processed_s3_bucket(mock_client):

    test_set = set()

    ingestion_bucket_name = 'mock-test-ingestion-va-052023'
    processed_bucket_name = 'mock-test-processed-va-052023'
    transform_sales_order('test', ingestion_bucket_name, processed_bucket_name, test_set)

    assert len(mock_client.list_objects_v2(Bucket=processed_bucket_name)['Contents']) == 1
    assert mock_client.list_objects_v2(Bucket=processed_bucket_name)['Contents'][0]['Key'] == 'dim_sales_order.parquet'


def test_transform_sales_order_transforms_tables_into_correct_parquet_shchema(mock_client):

    test_set = set()

    ingestion_bucket_name = 'mock-test-ingestion-va-052023'
    processed_bucket_name = 'mock-test-processed-va-052023'
    transform_sales_order('test', ingestion_bucket_name, processed_bucket_name, test_set)
    df = wr.s3.read_parquet(path=f's3://{processed_bucket_name}/dim_sales_order.parquet')
    assert len(df) == 3
    assert list(df.columns) == ['sales_record_id', 'sales_order_id', 'created_date', 'created_time', 'last_updated_date', 'last_updated_time', 'sales_staff_id', 'counterparty_id', 'units_sold', 'unit_price', 'currency_id', 'design_id', 'agreed_payment_date', 'agreed_delivery_date', 'agreed_delivery_location_id']


def test_transform_sales_order_raises_exception_when_agruments_invalid(mock_client):

    test_set = set()

    ingestion_bucket_name = 'mock-test-ingestion-va-052023'
    processed_bucket_name = 'mock-test-processed-va-052023'

    with pytest.raises(Exception):
        transform_sales_order('wrong', ingestion_bucket_name, processed_bucket_name, test_set)

    with pytest.raises(Exception):
        transform_sales_order('test', 'wrong', processed_bucket_name, test_set)

    with pytest.raises(Exception):
        transform_sales_order('test', ingestion_bucket_name, 'wrong', test_set)

    with pytest.raises(Exception):
        transform_sales_order('test', ingestion_bucket_name, processed_bucket_name, 'wrong')
