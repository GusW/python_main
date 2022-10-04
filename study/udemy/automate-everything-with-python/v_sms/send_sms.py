from time import sleep

from v_sms.constants import TWILIO_PHONE_NUMBER, TWILIO_PHONE_NUMBER_DESTINATION
from v_sms.twilio_client import twilio_client


def send_sms(
    destination: str = TWILIO_PHONE_NUMBER_DESTINATION, msg: str = "Hello World"
) -> None:
    message = twilio_client.messages.create(
        body=msg, from_=TWILIO_PHONE_NUMBER, to=destination
    )

    print(f"{message=}")


def send_sms_periodically(
    destination: str = TWILIO_PHONE_NUMBER_DESTINATION,
    msg: str = "Hello World",
    frequency_seconds: int = 60,
    repeat_amount: int = 0,
):
    print(
        f"\nSMS scheduled for each {frequency_seconds} seconds, repeat {repeat_amount or 'forever'}.\n"
    )
    count = 1
    condition = (
        (lambda x: True) if repeat_amount == 0 else (lambda x: x <= repeat_amount)
    )
    while condition(count):
        text = f"Sending SMS #{count}..."
        print(f"{text}\n")

        send_sms(destination=destination, msg=f"{msg}! {text}")

        sleep(frequency_seconds)
        count += 1


def main() -> None:
    # send_sms()

    send_sms_periodically(frequency_seconds=20, repeat_amount=2)


if __name__ == "__main__":
    main()
