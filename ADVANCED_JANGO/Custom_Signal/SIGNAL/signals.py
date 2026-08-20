from django.dispatch import Signal as signal , receiver


notification = signal()

@receiver(notification)
def show_notification(sender , **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("notification")


# custom_event_triggered = signal()