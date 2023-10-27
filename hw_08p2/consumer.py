import time
import logging
from models import Contact
from connect_rabbit import channel

logging.basicConfig(level=logging.INFO)

channel.queue_declare(queue='email_queue')

def send_email(contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        time.sleep(1)
        contact.send_email = True
        contact.save()
        logging.info(f'Successfully sent email for contact ID {contact_id}')
    except Exception as e:
        logging.error(f'Error sending email for contact ID {contact_id}: {e}')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_email(contact_id)

with channel:
    channel.queue_declare(queue='email_queue')

    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)

    print('Waiting for email messages. To exit press CTRL+C')
    channel.start_consuming()
