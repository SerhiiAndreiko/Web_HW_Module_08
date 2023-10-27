from random import choice
from faker import Faker
from models import Contact
from connect_db import connect_to_db
from connect_rabbit import channel, connection

def generate_fake_contacts(num_contacts=20):
    fake = Faker("uk-UA")
    notification_options = ['email', 'sms']
    contacts = []

    for _ in range(num_contacts):
        contacts.append({
            'fullname': fake.name(),
            'email': fake.email(),
            'phone_number': fake.msisdn(),
            'choice_for_message': choice(notification_options),
            'send_email': False,
            'send_sms': False
        })

    return contacts

def save_contacts_to_db(contacts):
    for data in contacts:
        contact = Contact(**data)
        contact.save()

        if contact.choice_for_message == 'email' and not contact.send_email:
            channel.basic_publish(exchange='', routing_key='email_queue', body=str(contact.id).encode())

        if contact.choice_for_message == 'sms' and not contact.send_sms:
            channel.basic_publish(exchange='', routing_key='sms_queue', body=str(contact.id).encode())

if __name__ == '__main__':
    try:
        connect_to_db()
        contacts = generate_fake_contacts()
        save_contacts_to_db(contacts)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
