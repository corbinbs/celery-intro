from celery import Celery
import celeryconfig
import requests

celery = Celery()
celery.config_from_object(celeryconfig)

@celery.task
def add(x, y):
    """
        Simple example task to add x and y and return the result
    """
    return x + y


@celery.task
def archive_old_data():
    """
        Archives last month's data
    """
    print("Archiving stuff...")
    #Do actual work required to archive.


@celery.task(max_retries=10, default_retry_delay=4, rate_limit='75/h')
def geocode_address(address):
    """
        Geocode address
    """

    location = None
    geo_info = requests.get('https://maps.googleapis.com/maps/api/geocode/json',
                            params={'address': address, 'sensor': 'true'}).json()
    results = geo_info.get('results')
    if results is not None and len(results) > 0:
        geometry = results[0].get('geometry')
        if geometry is not None:
            location = geometry.get('location')

    #TODO: Update record in datastore, etc?

    return location




