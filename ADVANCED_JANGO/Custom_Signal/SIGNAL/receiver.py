from django.dispatch import receiver
from .signals import custom_event_triggered

@receiver(custom_event_triggered)
def handle_custom_event(sender, **kwargs):
    # Handle the custom event here
    message = kwargs.get('message', '')
    user = kwargs.get('user', 'Anonymous')


    print("\n" + "="*40)
    print(f"signals activated !")
    print(f"Triggered by User: {user}")
    print(f"Payload Data: {message}")
    print("="*40 + "\n")